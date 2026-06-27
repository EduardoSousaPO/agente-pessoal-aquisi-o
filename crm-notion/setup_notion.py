#!/usr/bin/env python3
"""
setup_notion.py — cria as 3 bases do CRM do Motor de Prospecção LDC via Notion API.

Idempotente: rodar de novo NÃO duplica bases (procura por título na página-pai e
reaproveita). Lê credenciais de variáveis de ambiente; FALHA com mensagem clara
(BLOQUEIO explícito) se faltarem — nunca cria silenciosamente o errado.

Uso:
    python -m pip install -r crm-notion/requirements.txt
    export NOTION_TOKEN=ntn_...                 # (Windows PowerShell: $env:NOTION_TOKEN="ntn_...")
    export NOTION_PARENT_PAGE_ID=...            # ID da página-pai compartilhada com a integração
    python crm-notion/setup_notion.py

Referência de esquema: crm-notion/MODELO-DADOS.md
Referência de fórmulas/views: crm-notion/SETUP-NOTION.md

LIMITAÇÕES da Notion API (tratadas, não escondidas):
  - A API NÃO cria propriedade do tipo `status` → `Estágio` é criado como `select`
    com as mesmas 8 opções. As fórmulas usam `.name`, que funciona igual para
    select e status. (Opcional: converter para Status na UI depois.)
  - Criação de `rollup` e `formula` via API pode ser rejeitada dependendo da versão
    do workspace. O script TENTA criá-las e, se a API recusar, avisa exatamente o
    que finalizar à mão (SETUP-NOTION.md §2.4/§4) — sem falhar o resto.
"""
import json
import os
import sys
import urllib.error
import urllib.request

# Console Windows costuma ser cp1252 e quebra com emoji/box-drawing → força UTF-8.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass

NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"


# --------------------------------------------------------------------------- #
# Infra HTTP (stdlib, sem dependência de SDK além do requests opcional)
# --------------------------------------------------------------------------- #
def _request(method: str, path: str, token: str, body: dict | None = None) -> dict:
    url = f"{API}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise NotionError(f"HTTP {e.code} em {method} {path}: {detail}") from None


class NotionError(RuntimeError):
    pass


# --------------------------------------------------------------------------- #
# Helpers de schema (DRY para opções de select)
# --------------------------------------------------------------------------- #
def select(*names: str) -> dict:
    return {"select": {"options": [{"name": n} for n in names]}}


def title() -> dict:
    return {"title": {}}


def rich_text() -> dict:
    return {"rich_text": {}}


def number(fmt: str = "number") -> dict:
    return {"number": {"format": fmt}}


def checkbox() -> dict:
    return {"checkbox": {}}


def date() -> dict:
    return {"date": {}}


def formula(expr: str) -> dict:
    return {"formula": {"expression": expr}}


# --------------------------------------------------------------------------- #
# Definições das 3 bases (espelham MODELO-DADOS.md)
# --------------------------------------------------------------------------- #
ESTAGIO_OPCOES = [
    "Suspect (aquecimento)", "Lead pré-qualificado", "Reunião agendada",
    "Reunião feita", "Qualified prospect", "Nurturing", "Cliente", "Perdido / Inativo",
]
MAP_OPCOES = [
    "1 · Médicos quentes", "2 · Médicos frios", "3 · Mercado natural (Santander)",
    "4 · Empresários", "5 · Executivos / pré-aposentados",
]
TRILHA_OPCOES = ["❄️ Frio", "📩 Inscrito (opt-in news)", "🔆 Engajado", "✅ Pronto"]

# Fórmulas canônicas (Formula 2.0; Status/Select usam .name) — SETUP-NOTION.md §4
F_QUALIFICADO = (
    'if(prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") '
    'and prop("Gate ✓ Receptivo (stay engaged)"), "✅ Qualified", "⛔ Ainda não (falta gate)")'
)
F_GATE_STATUS = (
    'if((prop("Estágio").name == "Qualified prospect" or prop("Estágio").name == "Nurturing") '
    'and not (prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") '
    'and prop("Gate ✓ Receptivo (stay engaged)")), "🚨 Qualified sem os 3 ✓ — revisar", "")'
)
F_ENGAJAMENTO = (
    'if(empty(prop("Aberturas recentes (news)")), "❄️ sem dado", '
    'if(prop("Aberturas recentes (news)") >= 4, "🔥 Pronto? (abriu " + format(prop("Aberturas recentes (news)")) + "/6)", '
    'if(prop("Aberturas recentes (news)") >= 2, "🟡 Morno (" + format(prop("Aberturas recentes (news)")) + "/6)", '
    '"❄️ Frio (" + format(prop("Aberturas recentes (news)")) + "/6)")))'
)
F_ESFRIANDO = (
    'if(prop("Estágio").name == "Suspect (aquecimento)", "—", '
    'if(empty(prop("Último toque")), "⚠️ nunca tocado", '
    'if(dateBetween(now(), prop("Último toque"), "days") > 14, '
    '"🥶 Esfriando (" + format(dateBetween(now(), prop("Último toque"), "days")) + "d)", "🔥 Em dia")))'
)


def leads_props_base() -> dict:
    """Propriedades de Leads SEM relações/rollups/fórmulas dependentes (1ª passada)."""
    return {
        "Nome": title(),
        "Contato": rich_text(),
        "Origem": select("Newsletter LDC", "Ex-Santander", "Indicação",
                         "Campanha Goiânia", "Scraping/lista", "Evento", "Outro"),
        "MAP / Nicho": select(*MAP_OPCOES),
        # API não cria `status` → select com as mesmas opções (.name funciona igual)
        "Estágio": select(*ESTAGIO_OPCOES),
        "Trilha de aquecimento": select(*TRILHA_OPCOES),
        "Aberturas recentes (news)": number(),
        "Cliques recentes (news)": number(),
        "Gate ✓ Reunião feita": checkbox(),
        "Gate ✓ Patrimônio R$1mi+": checkbox(),
        "Gate ✓ Receptivo (stay engaged)": checkbox(),
        "Patrimônio estimado (R$)": number("real"),
        "Perfil de interesse": rich_text(),
        "Banco / assessor atual": rich_text(),
        "Datas pessoais": date(),
        "Profissão / Especialidade": rich_text(),
        "Faixa etária": select("até 35", "36-45", "46-55", "56-65", "65+"),
        "Produtos atuais": rich_text(),
        "Próximo toque (data)": date(),
        # Fórmulas que NÃO dependem de rollup já entram na 1ª passada:
        "Qualificado?": formula(F_QUALIFICADO),
        "Gate · status": formula(F_GATE_STATUS),
        "Sinal de engajamento": formula(F_ENGAJAMENTO),
    }


def toques_props() -> dict:
    return {
        "Resumo": title(),
        "Data": date(),
        "Tipo": select("Áudio", "Mensagem", "Ligação", "Reunião", "Artigo",
                      "Research", "Convite evento", "Reconhecimento"),
        "Tema": select("Macro BR", "Internacional", "Ativos/empresas",
                      "Planejamento/datas", "Pessoal"),
        "Canal": select("WhatsApp", "Telefone", "Presencial", "E-mail"),
        "Enviado por Eduardo?": checkbox(),
    }


def gatilhos_props() -> dict:
    return {
        "Descrição": title(),
        "Data": date(),
        "Tipo": select("Troca de emprego", "Herança/inventário",
                      "Venda de empresa/IPO/vesting", "Insatisfação c/ assessor",
                      "Aposentadoria", "Divórcio/viuvez", "Venda de imóvel",
                      "Saída do assessor atual", "PJ médica (virada)"),
        "Efeito": select("Subir à prioridade #1"),
    }


# --------------------------------------------------------------------------- #
# Idempotência: achar database existente por título dentro da página-pai
# --------------------------------------------------------------------------- #
def find_existing_databases(token: str, parent_id: str) -> dict:
    """Mapeia {titulo: database_id} dos child_database já existentes na página-pai."""
    found, cursor = {}, None
    while True:
        path = f"/blocks/{parent_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        res = _request("GET", path, token)
        for block in res.get("results", []):
            if block.get("type") == "child_database":
                t = block["child_database"].get("title", "")
                found[t] = block["id"]
        if res.get("has_more"):
            cursor = res.get("next_cursor")
        else:
            break
    return found


def create_database(token: str, parent_id: str, name: str, props: dict) -> str:
    body = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "title": [{"type": "text", "text": {"content": name}}],
        "properties": props,
    }
    res = _request("POST", "/databases", token, body)
    return res["id"]


def ensure_database(token: str, parent_id: str, existing: dict, name: str,
                    props: dict) -> tuple[str, bool]:
    if name in existing:
        print(f"  ↺ '{name}' já existe ({existing[name][:8]}…) — reaproveitando.")
        return existing[name], False
    db_id = create_database(token, parent_id, name, props)
    print(f"  ✓ '{name}' criada ({db_id[:8]}…).")
    return db_id, True


def patch_database(token: str, db_id: str, props: dict, label: str) -> bool:
    """Adiciona/atualiza propriedades. Best-effort: avisa se a API recusar."""
    try:
        _request("PATCH", f"/databases/{db_id}", token, {"properties": props})
        print(f"  ✓ {label}.")
        return True
    except NotionError as e:
        print(f"  ⚠️  {label} — a API recusou. Finalize à mão (SETUP-NOTION.md).")
        print(f"      Detalhe: {str(e)[:240]}")
        return False


# --------------------------------------------------------------------------- #
# Validação de ambiente — BLOQUEIO explícito
# --------------------------------------------------------------------------- #
def require_env() -> tuple[str, str]:
    token = os.environ.get("NOTION_TOKEN", "").strip()
    parent = os.environ.get("NOTION_PARENT_PAGE_ID", "").strip()
    faltando = []
    if not token:
        faltando.append("NOTION_TOKEN")
    if not parent:
        faltando.append("NOTION_PARENT_PAGE_ID")
    if faltando:
        print("─" * 70)
        print("⛔ BLOQUEIO: faltam credenciais de ambiente: " + ", ".join(faltando))
        print()
        print("   Estas credenciais só Eduardo gera (ver crm-notion/SETUP-NOTION.md §1):")
        print("     • NOTION_TOKEN          — segredo da integração interna do Notion")
        print("     • NOTION_PARENT_PAGE_ID — página compartilhada com a integração")
        print()
        print("   Linux/macOS:  export NOTION_TOKEN=ntn_...")
        print('   PowerShell:   $env:NOTION_TOKEN="ntn_..."')
        print("─" * 70)
        sys.exit(2)  # 2 = bloqueio por credencial ausente (não é erro de código)
    return token, parent


# --------------------------------------------------------------------------- #
# Orquestração
# --------------------------------------------------------------------------- #
def main() -> None:
    print("Motor de Prospecção LDC — setup do CRM Notion")
    token, parent = require_env()

    try:
        existing = find_existing_databases(token, parent)
    except NotionError as e:
        print("⛔ Não consegui ler a página-pai. Verifique se ela foi COMPARTILHADA")
        print("   com a integração (SETUP-NOTION.md §1, passo 5) e se o ID está certo.")
        print(f"   Detalhe: {str(e)[:240]}")
        sys.exit(1)

    print("\n[1/4] Bases sem relação (Gatilhos, Toques, Leads):")
    gatilhos_id, _ = ensure_database(token, parent, existing, "Gatilhos", gatilhos_props())
    toques_id, _ = ensure_database(token, parent, existing, "Toques", toques_props())
    leads_id, _ = ensure_database(token, parent, existing, "Leads", leads_props_base())

    print("\n[2/4] Relações em Leads → Toques / Gatilhos:")
    rel_ok = patch_database(token, leads_id, {
        "Toques": {"relation": {"database_id": toques_id, "single_property": {}}},
        "Gatilhos": {"relation": {"database_id": gatilhos_id, "single_property": {}}},
    }, "relações criadas")

    print("\n[3/4] Rollups em Leads (Último toque / Tem gatilho ativo?):")
    if rel_ok:
        patch_database(token, leads_id, {
            "Último toque": {"rollup": {
                "relation_property_name": "Toques",
                "rollup_property_name": "Data",
                "function": "latest_date",
            }},
            "Tem gatilho ativo?": {"rollup": {
                "relation_property_name": "Gatilhos",
                "rollup_property_name": "Efeito",
                "function": "count",
            }},
        }, "rollups criados")
    else:
        print("  ⚠️  pulado: relações não criadas. Crie relações+rollups à mão (§2.4).")

    print("\n[4/4] Fórmula dependente de rollup (Esfriando?):")
    patch_database(token, leads_id, {"Esfriando?": formula(F_ESFRIANDO)},
                   "fórmula Esfriando? criada")

    print("\n" + "─" * 70)
    print("✅ Setup concluído (o que a API permitiu).")
    print("   Próximos passos manuais:")
    print("   • Se algum ⚠️ apareceu acima, finalize aquela parte na UI (SETUP-NOTION.md).")
    print("   • Crie as VIEWS e o painel de metas (SETUP-NOTION.md §5 — não há API p/ views).")
    print("   • (Opcional) converta 'Estágio' de Select para Status na UI.")
    print("   • Rode novamente sem medo: o script é idempotente.")
    print("─" * 70)


if __name__ == "__main__":
    main()

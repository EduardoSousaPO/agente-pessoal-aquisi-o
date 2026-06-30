#!/usr/bin/env python3
"""
crm.py — helper rápido e confiável do CRM Notion do Motor de Prospecção LDC.

O agente (Tutor) usa isto para gravar/ler no CRM SEM redescobrir a API toda vez.
Lê NOTION_API_KEY/NOTION_TOKEN do ~/.hermes/.env. IDs das 3 bases fixos abaixo.

USO (exemplos):
  python crm.py list-leads
  python crm.py find-lead "Teste"
  python crm.py add-lead --nome "Dr. Teste Silva" --map A --estagio "Lead pré-qualificado" \
      --origem "Newsletter LDC" --patrimonio 1500000 --perfil "internacional; PJ médica" \
      --banco "Itaú" --profissao "Cardiologia"
  python crm.py add-toque --lead-id <id> --resumo "Mandei research FII" --tipo Áudio --tema Internacional --canal WhatsApp
  python crm.py add-gatilho --lead-id <id> --descricao "Vendeu clínica" --tipo "Venda de empresa/IPO/vesting"

Valores de select aceitos (normalização tolerante por prefixo/substring):
  --map:     A|B|C|D|Empresários|Executivos  (A·Reativação, B·Médicos frios, C·COI-âncora, D·Autoridade/Conteúdo)
  --estagio: Suspect | Lead pré-qualificado | Reunião agendada | Reunião feita | Qualified prospect | Nurturing | Cliente | Perdido
  --trilha:  Frio | Inscrito | Engajado | Pronto
"""
import argparse, json, os, sys, urllib.request, urllib.error

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

API = "https://api.notion.com/v1"
NV = "2022-06-28"
DB = {
    "leads":    "38f62514-7d75-8183-8b92-d5982c746e61",
    "toques":   "38f62514-7d75-814c-8eeb-da64a8eb9baf",
    "gatilhos": "38f62514-7d75-8149-ae8f-e7768cae250a",
}
MAP_OPC   = ["A · Reativação","B · Médicos frios","C · COI-âncora","D · Autoridade/Conteúdo","Empresários (pausado)","Executivos (pausado)"]
EST_OPC   = ["Suspect (aquecimento)","Lead pré-qualificado","Reunião agendada","Reunião feita","Qualified prospect","Nurturing","Cliente","Perdido / Inativo"]
TRILHA_OPC= ["❄️ Frio","📩 Inscrito (opt-in news)","🔆 Engajado","✅ Pronto"]


def load_token():
    for k in ("NOTION_API_KEY", "NOTION_TOKEN"):
        if os.environ.get(k): return os.environ[k].strip()
    envp = os.path.join(os.environ.get("HERMES_HOME", os.path.expanduser("~/.hermes")), ".env")
    if not os.path.exists(envp):
        envp = os.path.expanduser("~/AppData/Local/hermes/.env")
    try:
        for line in open(envp, encoding="utf-8"):
            line = line.strip()
            for k in ("NOTION_API_KEY=", "NOTION_TOKEN="):
                if line.startswith(k) and line[len(k):]:
                    return line[len(k):].strip()
    except Exception: pass
    sys.exit("ERRO: NOTION_API_KEY/NOTION_TOKEN não encontrado no ambiente nem no .env")


def req(method, path, token, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(API + path, data=data, method=method)
    r.add_header("Authorization", f"Bearer {token}")
    r.add_header("Notion-Version", NV)
    r.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(r) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERRO Notion HTTP {e.code}: {e.read().decode('utf-8','replace')[:400]}")


def match(val, opcoes):
    """Normaliza um valor para a opção de select mais próxima (prefixo/substring, case-insensitive)."""
    if not val: return None
    v = val.strip().lower()
    for o in opcoes:
        if o.lower() == v: return o
    for o in opcoes:                       # prefixo da letra (A/B/C/D) ou início
        if o.lower().startswith(v) or v == o.split(" · ")[0].lower(): return o
    for o in opcoes:                       # substring
        if v in o.lower(): return o
    return val                              # deixa passar (Notion valida)


def link_child(token, lead_id, rel_name, child_id):
    """Vincula um toque/gatilho ao lead. A relação é one-way (definida no lado Leads),
    então atualizamos a propriedade `rel_name` do LEAD adicionando o novo id."""
    lead = req("GET", f"/pages/{lead_id}", token)
    cur = (lead["properties"].get(rel_name, {}) or {}).get("relation") or []
    ids = [{"id": r["id"]} for r in cur] + [{"id": child_id}]
    req("PATCH", f"/pages/{lead_id}", token, {"properties": {rel_name: {"relation": ids}}})


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list-leads")
    p = sub.add_parser("find-lead"); p.add_argument("termo")
    p = sub.add_parser("add-lead")
    for a in ("nome","map","estagio","trilha","origem","perfil","banco","profissao","proxima","datas"):
        p.add_argument(f"--{a}", default=None)
    p.add_argument("--patrimonio", type=float, default=None)
    p.add_argument("--aberturas", type=int, default=None)
    p.add_argument("--gate-reuniao", action="store_true")
    p.add_argument("--gate-patrimonio", action="store_true")
    p.add_argument("--gate-receptivo", action="store_true")
    p = sub.add_parser("add-toque")
    for a in ("lead-id","resumo","tipo","tema","canal","data"):
        p.add_argument(f"--{a}", default=None)
    p.add_argument("--enviado", action="store_true")
    p = sub.add_parser("add-gatilho")
    for a in ("lead-id","descricao","tipo","data"):
        p.add_argument(f"--{a}", default=None)
    args = ap.parse_args()
    token = load_token()

    if args.cmd == "list-leads":
        d = req("POST", f"/databases/{DB['leads']}/query", token, {"page_size": 50})
        rows = d.get("results", [])
        print(f"{len(rows)} leads:")
        for pg in rows:
            nome = "".join(t["plain_text"] for t in (pg["properties"].get("Nome", {}).get("title", []) or []))
            est = (pg["properties"].get("Estágio", {}).get("select") or {}).get("name", "?")
            print(f"  - {nome}  [{est}]  id={pg['id']}")
        return

    if args.cmd == "find-lead":
        d = req("POST", f"/databases/{DB['leads']}/query", token,
                {"filter": {"property": "Nome", "title": {"contains": args.termo}}})
        for pg in d.get("results", []):
            nome = "".join(t["plain_text"] for t in (pg["properties"].get("Nome", {}).get("title", []) or []))
            print(f"  - {nome}  id={pg['id']}")
        if not d.get("results"): print("(nenhum)")
        return

    if args.cmd == "add-lead":
        if not args.nome: sys.exit("ERRO: --nome obrigatório")
        props = {"Nome": {"title": [{"text": {"content": args.nome}}]}}
        if args.map:       props["MAP / Nicho"] = {"select": {"name": match(args.map, MAP_OPC)}}
        if args.estagio:   props["Estágio"] = {"select": {"name": match(args.estagio, EST_OPC)}}
        if args.trilha:    props["Trilha de aquecimento"] = {"select": {"name": match(args.trilha, TRILHA_OPC)}}
        if args.origem:    props["Origem"] = {"select": {"name": args.origem}}
        if args.perfil:    props["Perfil de interesse"] = {"rich_text": [{"text": {"content": args.perfil}}]}
        if args.banco:     props["Banco / assessor atual"] = {"rich_text": [{"text": {"content": args.banco}}]}
        if args.profissao: props["Profissão / Especialidade"] = {"rich_text": [{"text": {"content": args.profissao}}]}
        if args.patrimonio is not None: props["Patrimônio estimado (R$)"] = {"number": args.patrimonio}
        if args.aberturas is not None:  props["Aberturas recentes (news)"] = {"number": args.aberturas}
        if args.proxima:   props["Próximo toque (data)"] = {"date": {"start": args.proxima}}
        if args.datas:     props["Datas pessoais"] = {"date": {"start": args.datas}}
        if args.gate_reuniao:    props["Gate ✓ Reunião feita"] = {"checkbox": True}
        if args.gate_patrimonio: props["Gate ✓ Patrimônio R$1mi+"] = {"checkbox": True}
        if args.gate_receptivo:  props["Gate ✓ Receptivo (stay engaged)"] = {"checkbox": True}
        d = req("POST", "/pages", token, {"parent": {"database_id": DB["leads"]}, "properties": props})
        print(f"OK lead criado: {args.nome}  id={d['id']}")
        return

    if args.cmd == "add-toque":
        if not args.resumo: sys.exit("ERRO: --resumo obrigatório")
        props = {"Resumo": {"title": [{"text": {"content": args.resumo}}]}}
        if args.tipo:  props["Tipo"]  = {"select": {"name": args.tipo}}
        if args.tema:  props["Tema"]  = {"select": {"name": args.tema}}
        if args.canal: props["Canal"] = {"select": {"name": args.canal}}
        if args.data:  props["Data"]  = {"date": {"start": args.data}}
        if args.enviado: props["Enviado por Eduardo?"] = {"checkbox": True}
        d = req("POST", "/pages", token, {"parent": {"database_id": DB["toques"]}, "properties": props})
        if getattr(args, "lead_id", None): link_child(token, args.lead_id, "Toques", d["id"])
        print(f"OK toque criado  id={d['id']}" + (f" (ligado ao lead {args.lead_id[:8]}…)" if getattr(args, "lead_id", None) else ""))
        return

    if args.cmd == "add-gatilho":
        if not args.descricao: sys.exit("ERRO: --descricao obrigatório")
        props = {"Descrição": {"title": [{"text": {"content": args.descricao}}]}}
        if args.tipo: props["Tipo"] = {"select": {"name": args.tipo}}
        if args.data: props["Data"] = {"date": {"start": args.data}}
        props["Efeito"] = {"select": {"name": "Subir à prioridade #1"}}
        d = req("POST", "/pages", token, {"parent": {"database_id": DB["gatilhos"]}, "properties": props})
        if getattr(args, "lead_id", None): link_child(token, args.lead_id, "Gatilhos", d["id"])
        print(f"OK gatilho criado  id={d['id']}" + (f" (ligado ao lead {args.lead_id[:8]}…)" if getattr(args, "lead_id", None) else ""))
        return


if __name__ == "__main__":
    main()

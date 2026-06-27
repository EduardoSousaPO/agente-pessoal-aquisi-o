# NOTION-MCP.md — Notion MCP para o Tutor

> Como o Tutor (Hermes) **lê e escreve** nas 3 bases do CRM via **Notion MCP**.
> Server escolhido, instalação, **permissões mínimas** e o mapeamento
> comportamento→ferramenta. Token: a **mesma** integração do CRM
> (`crm-notion/SETUP-NOTION.md` §1) — `<<<PREENCHER>>>`, só Eduardo gera, nunca git.

---

## 1. Server escolhido: **Notion MCP oficial** (`makenotion/notion-mcp-server`)

- Repo oficial: **github.com/makenotion/notion-mcp-server** · pacote npm
  **`@notionhq/notion-mcp-server`**.
- Por que este: é o **oficial da Notion** (mantido pela própria), roda em **stdio**
  (combina com o `hermes mcp`), e autentica com o **mesmo token de integração
  interna** que já criamos para o CRM — sem OAuth extra, sem segundo cadastro.
- Transporte: **stdio** (padrão). Há modo HTTP (`--transport http`, porta 3000),
  desnecessário aqui.

---

## 2. Instalação no Hermes

Caminho A — pelo picker do Hermes (recomendado):
```bash
hermes mcp add notion        # instala e pede as credenciais no fluxo interativo
hermes mcp                    # confirma status = conectado
```

Caminho B — declarativo em `~/.hermes/config.yaml` (ver `config.exemplo.yaml`):
```yaml
mcp_servers:
  notion:
    command: "npx"
    args: ["-y", "@notionhq/notion-mcp-server"]
    env:
      NOTION_TOKEN: "${NOTION_TOKEN}"     # lido do ~/.hermes/.env (recomendado pela doc)
```
> **`NOTION_TOKEN` é o método recomendado** pela doc oficial (mais simples que
> `OPENAPI_MCP_HEADERS`). O valor real fica no `.env`; aqui só a referência.

**Pré-requisito de Node:** o `npx` exige Node.js instalado (LTS). Se não tiver:
instale o Node antes (`node -v` para checar).

> ⚠️ **Windows (caso do Eduardo) — issue conhecido #291:** em alguns clientes a
> env `NOTION_TOKEN` não é lida quando o server é spawnado no Windows. Se o MCP
> subir mas responder "unauthorized", use a variante `OPENAPI_MCP_HEADERS` (abaixo)
> ou defina a env no escopo do sistema. Não é bug do nosso setup.

Variante de fallback (header explícito):
```yaml
    env:
      OPENAPI_MCP_HEADERS: '{"Authorization":"Bearer ${NOTION_TOKEN}","Notion-Version":"2025-09-03"}'
```

---

## 3. Permissões mínimas (princípio do menor privilégio)

### 3.1 Na integração do Notion (lado Notion)
Na página **my-integrations** → sua integração `Motor Prospecção LDC`:
- **Capabilities:** `Read content`, `Update content`, `Insert content`. **Não**
  habilite "Read user information" (não precisamos de dados de usuários).
- **Access (aba Access):** conecte **apenas** a página-pai do CRM (ou as 3 bases).
  Assim o MCP enxerga só o CRM, nada mais do workspace. (Sem isso → `object_not_found`.)

### 3.2 No MCP (lado Hermes) — expor só as ferramentas necessárias
O server expõe muitas ferramentas; restrinja com `tools.include` no `config.yaml`.
Precisamos só de: **buscar**, **ler base/itens**, **criar item**, **atualizar item**.

```yaml
    tools:
      include:
        - search            # localizar as bases Leads/Toques/Gatilhos
        - fetch             # ler um item (lead/toque/gatilho)
        - create-pages      # criar lead / registrar toque / registrar gatilho
        - update-page       # mudar estágio, marcar gate, mover trilha
    prompts: false
    resources: false
```

> ⚠️ **Confirme os nomes exatos das tools** com `hermes mcp` (ou a doc da versão do
> server) **depois de conectar** — o Notion MCP teve duas gerações de nomes
> (`API-post-search`/`API-post-page`… na geração OpenAPI; `search`/`fetch`/
> `create-pages`/`update-page` na geração 2025-09-03). Use os que aparecerem no seu
> server; **não decore daqui sem verificar**. O `config.exemplo.yaml` traz a lista
> da geração OpenAPI como alternativa.

---

## 4. Como o Tutor usa o MCP (comportamento → ação no CRM)

Mapeia os **5 comportamentos** (`PROMPT-SISTEMA.md`) nas bases (`MODELO-DADOS.md`):

| Comportamento do Tutor | Ação MCP | Base / campos |
|---|---|---|
| **Registra lead** ("conheci o Dr. X") | `create-pages` | `Leads`: Nome, Origem, MAP, Estágio, Trilha, Perfil de interesse |
| **Aplica o gate / muda estágio** | `update-page` | `Leads`: 3 checkboxes do Gate, `Estágio` |
| **Registra toque** | `create-pages` | `Toques`: Resumo, Data, Tipo, Tema, Canal, relação→Lead |
| **Registra gatilho** | `create-pages` | `Gatilhos`: Descrição, Data, Tipo, Efeito, relação→Lead |
| **Guia o dia / mostra números** | `search` + `fetch` (views) | lê metas semanais, pipeline, `Esfriando?`, `Tem gatilho` |
| **Traz ganchos** (curadoria) | `fetch` | lê `Perfil de interesse` de cada lead p/ cruzar com os 4 temas |

**Fluxo de leitura típico (digest da manhã):**
1. `search` → resolve os IDs das bases `Leads`/`Toques` (cacheia).
2. `fetch`/query → leads com `Esfriando? = 🥶` e `Trilha = ✅ Pronto` e `Tem gatilho`.
3. Monta o digest no tom de Eduardo (rascunho) — **não envia** (envio é dele).

**Fluxo de escrita típico (intake):** para cada lead, `create-pages` no `Leads` com
estágio classificado + gate; `update-page` se o lead já existir (idempotência por
nome/contato — o Tutor confere antes de duplicar).

---

## 5. Comportamento de falha [spec §9]
- **Escrita falha** (timeout/unauthorized) → o Tutor **não perde o dado**: guarda em
  buffer na memória e avisa "não gravei no CRM agora, te lembro de sincronizar".
- **`object_not_found`** → a integração não tem acesso à base. Reconecte a página na
  aba **Access** (§3.1).
- **Tool não existe** com o nome do config → rodou a outra geração do server; ajuste
  o `tools.include` para os nomes reais (§3.2).

---

## 6. Checklist
- [ ] Node.js (LTS) instalado (`node -v`).
- [ ] `NOTION_TOKEN` no `~/.hermes/.env` (mesma integração do CRM) — **depende de Eduardo**.
- [ ] Integração com capabilities mínimas + **Access** só na página/bases do CRM.
- [ ] `hermes mcp` mostra `notion` conectado.
- [ ] `tools.include` ajustado aos nomes reais do server (verificados, não decorados).
- [ ] Teste: pedir ao Tutor "liste os leads esfriando" → ele lê via MCP e responde.

## Fontes
- [Notion MCP Server oficial — makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)
- [Hermes — MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Issue #291 — NOTION_TOKEN no Windows (stdio)](https://github.com/makenotion/notion-mcp-server/issues/291)

# PROGRESS — Motor de Prospecção LDC

> Estado das tarefas do loop de implementação. Fonte de verdade do progresso.
> Status possíveis: `PENDENTE` · `CONCLUÍDA` · `BLOQUEADA`.
> Regra: a cada iteração, pegar a 1ª tarefa `PENDENTE` cujas dependências estão `CONCLUÍDA`,
> implementar por completo, marcar `CONCLUÍDA` (1 linha), commitar, e parar.

**Última atualização:** 2026-06-27 — F3.1 concluída (curadoria-diaria/SKILL.md: 4 temas, fila por gatilho/esfriando, match com perfil de interesse, digest 2-3/dia, registra toque ao confirmar). Próxima: F3.2.

---

## FASE 0 — Constituição (autônoma)

| ID | Tarefa | Depende de | Status |
|----|--------|------------|--------|
| F0.1 | Criar estrutura de pastas (`tutor/skills/`, `tutor/memoria/`, `tutor/hermes/`, `crm-notion/`, `runbooks/`) | — | CONCLUÍDA |
| F0.2 | `tutor/skills/metodo-mullen/SKILL.md` (gate, estágios, metas, Avis, catálogo, regras de correção, auto-correção) | F0.1 | CONCLUÍDA |
| F0.3 | `tutor/memoria/USER.md` (contexto Eduardo + placeholders) | F0.1 | CONCLUÍDA |
| F0.4 | `tutor/skills/metodo-mullen/talk-tracks.md` (scripts `[RECONSTR.]` no tom de Eduardo) | F0.2 | CONCLUÍDA |
| F0.5 | `tutor/PROMPT-SISTEMA.md` (system prompt do Tutor + intake) | F0.2, F0.3 | CONCLUÍDA |

## FASE 1 — CRM Notion

| ID | Tarefa | Depende de | Status |
|----|--------|------------|--------|
| F1.1 | `crm-notion/MODELO-DADOS.md` (3 bases, props, fórmulas "esfriando" + gate) | F0.1 | CONCLUÍDA |
| F1.2 | `crm-notion/SETUP-NOTION.md` (runbook bases + views + token) | F1.1 | CONCLUÍDA |
| F1.3 | `crm-notion/setup_notion.py` (script idempotente via Notion API) | F1.1 | CONCLUÍDA |
| F1.4 | `crm-notion/seed-exemplo.md` (2-3 leads fictícios) | F1.1 | CONCLUÍDA |

## FASE 2 — Hermes + Telegram + Notion

| ID | Tarefa | Depende de | Status |
|----|--------|------------|--------|
| F2.1 | `tutor/hermes/SETUP-HERMES.md` (runbook instalação + skills + Telegram + Notion MCP) | F0.2, F1.1 | CONCLUÍDA |
| F2.2 | `tutor/hermes/config.exemplo.*` (configs exemplo sem segredos) | F2.1 | CONCLUÍDA |
| F2.3 | `tutor/hermes/NOTION-MCP.md` (Notion MCP server + permissões + leitura/escrita) | F2.1 | CONCLUÍDA |

## FASE 3 — Curadoria diária

| ID | Tarefa | Depende de | Status |
|----|--------|------------|--------|
| F3.1 | `tutor/skills/curadoria-diaria/SKILL.md` (4 temas, cruzamento, esfriando, digest) | F0.2, F0.3 | CONCLUÍDA |
| F3.2 | `tutor/skills/curadoria-diaria/AGENDAMENTO.md` (agendar digest + fallbacks) | F3.1 | PENDENTE |
| F3.3 | `tutor/skills/curadoria-diaria/templates-digest.md` (2-3 formatos) | F3.1 | PENDENTE |

## FASE 4 — Intake + operação

| ID | Tarefa | Depende de | Status |
|----|--------|------------|--------|
| F4.1 | `tutor/skills/intake-interview/SKILL.md` (roteiro, gate, gravação, resumo) | F0.2, F0.3, F1.1 | PENDENTE |
| F4.2 | `runbooks/ROTINA-DIARIA.md` (rotina 1-2h/dia + ritual semanal) | F3.1, F4.1 | PENDENTE |
| F4.3 | `docs/plans/CHECKLIST-GO-LIVE.md` (todos os bloqueios humanos consolidados) | F2.1, F1.2 | PENDENTE |

---

## ⛔ PRECISO DE VOCÊ

> Itens que só Eduardo fornece. Serão preenchidos via marcador `<<<PREENCHER: ...>>>`
> nos artefatos e listados aqui conforme as tarefas os encontrarem.

Estes 3 inputs (§2.1 da spec) estão como `<<<PREENCHER>>>` em `tutor/memoria/USER.md`.
A constituição roda com placeholders; o Tutor opera com a ressalva até travarem:

1. **Patamar de patrimônio (R$)** — o número que separa *suspect* de *qualified*
   (gate critério #2). Pode ser 1 valor ou 1 por nicho. → `USER.md` §3.1.
2. **MAPs adicionais (~4 além de médicos)** — nicho + lead-time + threshold + fonte
   da lista de cada um. → `USER.md` §3.2.
3. **Amostras reais de tom de voz (2-3 mensagens)** — sem PII (nomes/contatos), só
   o fraseado, pra calibrar os rascunhos. → `USER.md` §4.1.

**Credenciais (Fase 1-2) — só Eduardo gera, vão pro `.env` (nunca git):**
4. **`NOTION_TOKEN`** + **`NOTION_PARENT_PAGE_ID`** — integração interna do Notion
   e página-pai compartilhada com ela. Destrava o script F1.3 e o Notion MCP.
   Passo a passo em `crm-notion/SETUP-NOTION.md` §1.
5. **Provedor de modelo (BYO)** — chave de API do modelo escolhido (Nous Portal /
   `OPENROUTER_API_KEY` / outro). Vai em `~/.hermes/.env`. Ver `SETUP-HERMES.md` §2.
6. **`TELEGRAM_BOT_TOKEN`** (BotFather) + **`TELEGRAM_ALLOWED_USERS`** (seu user ID
   numérico, p/ travar o bot só p/ você). Ver `SETUP-HERMES.md` §4.

---

## ✅ PRONTO ATÉ AQUI

_(resumo final — preenchido quando todas as tarefas estiverem CONCLUÍDA ou BLOQUEADA)_

# CHECKLIST-GO-LIVE.md — Ligar o Motor de Prospecção

> **Para Eduardo.** Tudo que depende de você (credenciais + execução) num só lugar.
> A engenharia (constituição, CRM, skills, runbooks) está **pronta no repo**; falta
> plugar as credenciais e rodar os setups. Marque cada `[ ]` ao concluir.
>
> Os **valores de conteúdo já foram travados** (patrimônio R$ 1mi+, 5 MAPs, tom de
> voz — `tutor/memoria/USER.md`). O que falta é **credencial e execução**.

---

## ⛔ Parte 1 — Credenciais que só você gera
Guarde todas no `~/.hermes/.env` (e o token do Notion também serve ao script).
**Nenhuma vai pro git.** Template: `tutor/hermes/.env.exemplo`.

| # | Credencial | Onde gerar | Vai em | Runbook |
|---|---|---|---|---|
| [ ] 1 | **`NOTION_TOKEN`** | notion.so/my-integrations → New integration (Internal) | `.env` | `crm-notion/SETUP-NOTION.md` §1 |
| [ ] 2 | **`NOTION_PARENT_PAGE_ID`** | URL da página-pai do CRM (compartilhada c/ a integração) | `.env` | idem §1 |
| [ ] 3 | **Chave do provedor de modelo** (ex.: `OPENROUTER_API_KEY` / Nous Portal) | painel do provedor escolhido | `.env` | `tutor/hermes/SETUP-HERMES.md` §2 |
| [ ] 4 | **`TELEGRAM_BOT_TOKEN`** | Telegram → @BotFather → /newbot | `.env` | `SETUP-HERMES.md` §4.1 |
| [ ] 5 | **`TELEGRAM_ALLOWED_USERS`** | seu user ID via @userinfobot (trava o bot só p/ você) | `.env` | `SETUP-HERMES.md` §4.2 |

> ⚠️ Sem o #5 o bot fica aberto a qualquer um que o encontrar. **Não pule.**

---

## 🔧 Parte 2 — Execução (na ordem)

### A. CRM Notion
- [ ] Criar a integração e **compartilhar a página-pai** com ela (§1 do SETUP-NOTION).
- [ ] Criar as 3 bases — **escolha um caminho**:
  - [ ] Manual: `crm-notion/SETUP-NOTION.md` §2, **ou**
  - [ ] Script: `pip install -r crm-notion/requirements.txt` → setar `NOTION_TOKEN`
        e `NOTION_PARENT_PAGE_ID` → `python crm-notion/setup_notion.py`.
- [ ] Finalizar o que a API não cria: **rollups** (`Último toque`, `Tem gatilho`),
      converter `Estágio` p/ Status (opcional), e **colar as 4 fórmulas** (versão
      `.name`, `SETUP-NOTION.md` §4).
- [ ] Criar as **6 views + painel de metas** (`SETUP-NOTION.md` §5 — não há API p/ views).
- [ ] Inserir o **seed fictício** (`crm-notion/seed-exemplo.md`) e validar as fórmulas
      pelo checklist do próprio seed. **Apague o seed antes de entrar dados reais.**

### B. Hermes + Telegram
- [ ] Instalar o Hermes (`SETUP-HERMES.md` §1) e configurar o **modelo** (§2).
- [ ] Copiar as **3 skills** para `~/.hermes/skills/ldc/` (`metodo-mullen`,
      `curadoria-diaria`, `intake-interview`) e confirmar em `hermes skills browse`.
- [ ] Apontar **`PROMPT-SISTEMA.md`** como system prompt e carregar **`USER.md`** na
      memória (§3).
- [ ] Criar o bot, setar `TELEGRAM_*` no `.env`, subir `hermes gateway` e testar a
      resposta no Telegram (§4).

### C. Notion via MCP
- [ ] `hermes mcp add notion` (ou config declarativa) com `NOTION_TOKEN`
      (`tutor/hermes/NOTION-MCP.md`).
- [ ] Garantir **Access** da integração só nas bases do CRM (permissão mínima).
- [ ] Ajustar `tools.include` aos **nomes reais** das tools (verificar com `hermes mcp`).
- [ ] Teste: *"liste os leads esfriando"* → o Tutor lê via MCP e responde.

### D. Curadoria + primeira operação
- [ ] Agendar o digest: *"Todo dia útil às 7h, rode a `curadoria-diaria` e me manda
      o digest"* (`curadoria-diaria/AGENDAMENTO.md`).
- [ ] Rodar o **intake** da base real: *"vamos organizar minha lista"* → cole os
      nomes → o Tutor classifica e grava (`intake-interview/SKILL.md`). Resultado
      esperado: resumo "X qualified, Y prospects, Z suspects; comece por estes 3".
- [ ] Operar 1 dia pela `runbooks/ROTINA-DIARIA.md` e fazer o **ritual semanal** na
      sexta.

---

## ✅ Critérios de "motor ligado" (spec §12)
- [ ] Toda a base organizada via intake numa sessão.
- [ ] Nenhum lead Qualified sem os 3 ✓ do gate (Tutor bloqueia/alerta).
- [ ] Digest diário entrega ≥2 ganchos personalizados e acionáveis.
- [ ] Painel mostra a qualquer hora: ritmo da semana, pipeline total, leads esfriando.
- [ ] Você opera em ≤1-2h/dia e mantém a cadência por ≥4 semanas.
- [ ] Conversão e lead time medidos por MAP.

---

## 🧭 Mapa do que já está pronto no repo (referência)
| Quer… | Abra |
|---|---|
| O método embutido (gate, metas, correção) | `tutor/skills/metodo-mullen/SKILL.md` |
| Os scripts de conversa | `tutor/skills/metodo-mullen/talk-tracks.md` |
| Quem é Eduardo / valores travados | `tutor/memoria/USER.md` |
| A persona do Tutor | `tutor/PROMPT-SISTEMA.md` |
| O modelo de dados do CRM | `crm-notion/MODELO-DADOS.md` |
| Subir Hermes/Telegram/MCP | `tutor/hermes/SETUP-HERMES.md` · `NOTION-MCP.md` |
| O digest diário | `tutor/skills/curadoria-diaria/` |
| Organizar a base | `tutor/skills/intake-interview/SKILL.md` |
| A rotina do dia a dia | `runbooks/ROTINA-DIARIA.md` |
| O estado das tarefas | `PROGRESS.md` |

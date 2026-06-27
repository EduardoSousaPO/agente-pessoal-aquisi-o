# SETUP-HERMES.md — Subir o Tutor no Hermes Agent

> Runbook para colocar o **Tutor** (constituição da Fase 0) rodando no **Hermes
> Agent** (NousResearch) com **Telegram** + **Notion via MCP**. Passos citados da
> doc oficial — ver **Fontes** no fim. Onde houver credencial, é
> `<<<PREENCHER>>>` e **só Eduardo gera** (registrado em `PROGRESS.md > PRECISO DE
> VOCÊ`). Nada de segredo no git.
>
> O que já temos prontos para carregar:
> - `tutor/PROMPT-SISTEMA.md` — persona + 5 comportamentos + intake.
> - `tutor/skills/metodo-mullen/` — skill `metodo-mullen` (+ `talk-tracks.md`).
> - `tutor/skills/curadoria-diaria/` e `tutor/skills/intake-interview/` — Fases 3-4.
> - `tutor/memoria/USER.md` — memória do Eduardo.

---

## 0. Visão do que vamos ligar
```
Telegram (você) ⇄ Hermes gateway ⇄ Hermes Agent (modelo BYO)
                                     ├─ system prompt = PROMPT-SISTEMA.md
                                     ├─ skills = metodo-mullen, curadoria-diaria, intake-interview
                                     ├─ memória = USER.md
                                     └─ MCP "notion" ⇄ CRM (3 bases)  → ver NOTION-MCP.md
```

---

## 1. Instalar o Hermes Agent

> Pré-requisitos (doc): modelo com **≥64.000 tokens** de contexto; SO suportado
> (macOS, **Windows**, Linux, WSL2, Android/Termux).

**Windows (PowerShell) — o caso do Eduardo:**
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
*(Alternativa: baixar o **Hermes Desktop** installer em hermes-agent.nousresearch.com.)*

**Linux/macOS/WSL2:**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc   # ou ~/.zshrc
```

Verifique:
```bash
hermes --version
```

**Onde o Hermes guarda config (importante p/ os próximos passos):**
- Segredos/tokens → `~/.hermes/.env`
- Configurações → `~/.hermes/config.yaml`
- Skills → `~/.hermes/skills/` *(fonte de verdade das skills)*

---

## 2. Escolher o provedor de modelo (BYO) `<<<PREENCHER>>>`

A spec pede **bring-your-own** (Nous Portal / OpenRouter). Setup interativo:
```bash
hermes model
```
ou OAuth rápido pelo Portal:
```bash
hermes setup --portal
```

Definir manualmente (exemplos da doc — escolha **um** provedor):
```bash
hermes config set model anthropic/claude-opus-4.6
hermes config set OPENROUTER_API_KEY sk-or-...      # <<<PREENCHER: chave do provedor>>>
```
> Padrões de env aceitos: `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`,
> `DEEPSEEK_API_KEY`, `GOOGLE_API_KEY`/`GEMINI_API_KEY`, `XAI_API_KEY`, etc.
> Recomendação: um modelo forte em instrução/ferramentas (o Tutor usa MCP +
> seguimento de regras `[WP]`). Guarde a chave no `~/.hermes/.env`.

**Teste rápido no terminal antes do Telegram:**
```bash
hermes --tui
```

---

## 3. Carregar a constituição (system prompt + skills + memória)

### 3.1 Skills — copiar para `~/.hermes/skills/`
As skills do Hermes vivem em `~/.hermes/skills/<categoria>/<skill>/SKILL.md`. Copie
as nossas três pastas para lá:

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse tutor\skills\metodo-mullen      "$env:USERPROFILE\.hermes\skills\ldc\metodo-mullen"
Copy-Item -Recurse tutor\skills\curadoria-diaria   "$env:USERPROFILE\.hermes\skills\ldc\curadoria-diaria"
Copy-Item -Recurse tutor\skills\intake-interview   "$env:USERPROFILE\.hermes\skills\ldc\intake-interview"
```
**Linux/macOS:**
```bash
cp -r tutor/skills/metodo-mullen    ~/.hermes/skills/ldc/metodo-mullen
cp -r tutor/skills/curadoria-diaria ~/.hermes/skills/ldc/curadoria-diaria
cp -r tutor/skills/intake-interview ~/.hermes/skills/ldc/intake-interview
```
Confirme que aparecem:
```bash
hermes skills browse          # lista as instaladas
```
Cada skill vira um slash-command automaticamente (ex.: `/metodo-mullen`,
`/curadoria-diaria`, `/intake-interview`).

> **Manter sincronizado:** este repo é a fonte de verdade. Ao editar uma skill
> aqui, recopie para `~/.hermes/skills/ldc/`. (Opcional: symlink em vez de cópia.)

### 3.2 System prompt — `PROMPT-SISTEMA.md`
Aponte o system prompt do agente para o nosso arquivo. Conforme sua versão do
Hermes, via config:
```bash
hermes config set system_prompt_file "<caminho-absoluto>/tutor/PROMPT-SISTEMA.md"
```
*(Se a sua build não expuser essa chave, cole o conteúdo de `PROMPT-SISTEMA.md` no
campo de instruções de sistema do `~/.hermes/config.yaml`. Verifique a chave exata
em `hermes config` / doc da sua versão antes — não inventar nome de chave.)*

### 3.3 Memória — `USER.md`
O Hermes mantém um modelo persistente do usuário. Carregue o nosso `USER.md`:
- Copie o conteúdo para a memória/`MEMORY` do Hermes (ou aponte o arquivo, se a sua
  versão suportar `memory_file`), **ou**
- Na 1ª conversa, peça ao Tutor para "ler e internalizar `USER.md`" e salvar como
  memória persistente.
> `USER.md` tem itens `TRAVADO` (fonte de verdade) e a janela "esfriando". Sem PII
> de leads — esses ficam só no Notion.

---

## 4. Conectar o Telegram

### 4.1 Criar o bot (BotFather) `<<<PREENCHER>>>`
1. No Telegram, abra **@BotFather** → `/newbot`.
2. Nome de exibição: ex. "Tutor Prospecção LDC".
3. Username único terminando em `bot` (ex.: `tutor_ldc_bot`).
4. Copie o **token** (formato `123456789:ABC...`). **Segredo** — não versionar.

### 4.2 Seu user ID (restringir acesso só a você)
- Mande mensagem a **@userinfobot** → ele devolve seu **ID numérico** (ex.: `123456789`).

### 4.3 Configurar e subir o gateway
Em `~/.hermes/.env`:
```
TELEGRAM_BOT_TOKEN=<<<PREENCHER: token do BotFather>>>
TELEGRAM_ALLOWED_USERS=<<<PREENCHER: seu user ID numérico>>>
```
> `TELEGRAM_ALLOWED_USERS` trava o bot só para você (vírgula separa múltiplos).
> **Crucial p/ privacidade** — sem isso qualquer um que achar o bot conversa com ele.

Suba o gateway:
```bash
hermes gateway          # ou: hermes gateway setup  (wizard, escolha Telegram)
hermes gateway status   # checar online
```
Mande uma mensagem ao bot no Telegram para validar (responde em segundos).

---

## 5. Plugar o Notion (MCP)

Resumo aqui; **passo a passo e permissões mínimas em `NOTION-MCP.md` (F2.3)** e o
exemplo de YAML em `config.exemplo.yaml` (F2.2).

```bash
hermes mcp add notion        # picker interativo: instala e pede as credenciais
hermes mcp                    # status dos servers MCP
```
O server `notion` precisa de `NOTION_TOKEN` (a mesma integração do CRM — ver
`crm-notion/SETUP-NOTION.md` §1) e da página/bases compartilhadas com ela.

---

## 6. Agendar o digest diário (curadoria)
O Hermes aceita **agendamento em linguagem natural**. Depois do gateway no ar:
> "Todo dia útil às 7h, rode a skill `curadoria-diaria` e me manda o digest no
> Telegram."

Detalhe, fallbacks e o texto exato em `tutor/skills/curadoria-diaria/AGENDAMENTO.md`
(F3.2).

---

## 7. Checklist de "Tutor no ar"
- [ ] `hermes --version` ok (instalado).
- [ ] Provedor de modelo configurado (`hermes model`) — **chave depende de Eduardo**.
- [ ] 3 skills em `~/.hermes/skills/ldc/` e aparecendo em `hermes skills browse`.
- [ ] `PROMPT-SISTEMA.md` como system prompt; `USER.md` na memória.
- [ ] Bot criado (BotFather) + `TELEGRAM_BOT_TOKEN` + `TELEGRAM_ALLOWED_USERS` no `.env` — **depende de Eduardo**.
- [ ] `hermes gateway status` = online; bot responde no Telegram.
- [ ] MCP `notion` conectado (`NOTION_TOKEN`) — lê/escreve as 3 bases (ver NOTION-MCP.md).
- [ ] Digest agendado (curadoria-diaria).

---

## Fontes (doc oficial, jun/2026)
- [Hermes Agent — Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Telegram gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)
- [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Repo NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

> ⚠️ Onde a doc da sua versão divergir (nome de chave de system prompt/memória),
> **confie na doc/`hermes config` da versão instalada** — este runbook não inventa
> nomes de config que não confirmou.

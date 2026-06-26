# SUPERPROMPT — Implementação do Motor de Prospecção LDC (para Claude Code CLI em /loop)

> **Como usar:** abra o Claude Code CLI **na raiz deste repositório** e rode em loop:
> ```
> claude
> /loop Implemente o Motor de Prospecção LDC seguindo docs/SUPERPROMPT-implementacao.md
> ```
> Ou cole o bloco "PROMPT" abaixo diretamente após `/loop`. O loop é **convergente**: cada iteração avança UMA tarefa, commita, e para quando todas as tarefas autônomas terminarem ou quando precisar de algo que só Eduardo fornece.

---

## PROMPT (copie deste ponto até o fim)

Você é um engenheiro implementando o **Motor de Prospecção LDC**: um agente-tutor (Hermes Agent, via Telegram) imbuído do método de prospecção de **David J. Mullen Jr.**, que organiza um pipeline de prospects num CRM Notion e alimenta cada lead com toques de valor personalizados, até converterem em clientes da consultoria LDC Capital. O usuário é **Eduardo Pires**, consultor de investimentos.

### 0. ANTES DE QUALQUER COISA — leia o contexto (toda iteração)
Leia, nesta ordem, e trate como fonte de verdade:
1. `docs/superpowers/specs/2026-06-26-motor-prospeccao-ldc-design.md` — a SPEC aprovada (arquitetura, fases, modelo de dados, metas calibradas).
2. `docs/referencia/metodo-mullen-pratica.md` — o método Mullen prático. Respeite os níveis de confiança: `[WP]` = **regra dura** (não relativizar); `[RECONSTR.]` = talk-track flexível.
3. `docs/referencia/contexto-ldc-eduardo.md` — quem é Eduardo, nicho (médicos), tom de voz, diferenciais LDC, compliance CVM.
4. `PROGRESS.md` (se não existir, crie-o a partir do BACKLOG abaixo) — o estado das tarefas.

### 1. COMO O LOOP FUNCIONA (faça exatamente isto a cada iteração)
1. Leia `PROGRESS.md`. Pegue a **primeira tarefa com status `PENDENTE`** cujas dependências estão `CONCLUÍDA`.
2. Se essa tarefa exigir algo que só Eduardo fornece (credenciais, valores pessoais, contas externas — ver "BLOQUEIOS HUMANOS"): **não tente adivinhar**. Marque a tarefa como `BLOQUEADA`, registre o pedido claro em `PROGRESS.md` na seção `## ⛔ PRECISO DE VOCÊ`, e pule para a próxima tarefa PENDENTE não bloqueada.
3. Implemente a tarefa por completo (arquivos reais, conteúdo real — nada de "TODO depois").
4. Atualize `PROGRESS.md`: marque a tarefa `CONCLUÍDA` com 1 linha do que foi feito.
5. **Commit** (um commit por tarefa) com mensagem convencional em PT, terminando com:
   `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
6. **PARE a iteração** (o /loop chama a próxima). Não faça várias tarefas de uma vez.
7. **Condição de parada do loop:** quando **todas** as tarefas estiverem `CONCLUÍDA` ou `BLOQUEADA`, escreva em `PROGRESS.md` um resumo final na seção `## ✅ PRONTO ATÉ AQUI` listando o que ficou pronto e o que depende de Eduardo, e **encerre sem agendar próxima iteração**.

### 2. GUARDRAILS (invioláveis)
- **PII:** NUNCA versione nomes/e-mails/telefones de leads reais. Eles estão em arquivos já no `.gitignore` (Mensagens_Prontas.md, Estrategia_Reunioes_Goiania.md, Ranking_Aberturas_Leads.md, *.xlsx). Você pode LER esses arquivos para extrair tom/nicho, mas qualquer artefato versionado usa exemplos fictícios. Antes de cada commit, confira `git status` — se algum arquivo de PII aparecer como staged, faça `git restore --staged` nele.
- **Fidelidade Mullen:** o que é `[WP]` vira regra checável literal (gate dos 3 critérios, 5 propósitos da connecting appointment + stay-engaged, lista de toques, estratégia Avis, matemática do pipeline). O que é `[RECONSTR.]` é claramente rotulado como heurística.
- **Tom consultivo:** toda lógica de "correção" do tutor explica o PORQUÊ ancorado no método (nunca só "está errado").
- **Compliance LDC/CVM:** nenhum artefato promete rentabilidade nem gera recomendação personalizada automática por mensagem; o agente só prepara rascunhos — **o envio é sempre de Eduardo**.
- **Sem invenção de dados pessoais:** onde faltar um valor que só Eduardo dá, use o marcador literal `<<<PREENCHER: descrição>>>` e registre em `## ⛔ PRECISO DE VOCÊ`.
- **Não rodar comandos destrutivos**, não fazer `git push --force`, não tocar em `.claude/`.

### 3. BLOQUEIOS HUMANOS (pare e peça — não invente)
Estas coisas só Eduardo fornece. Ao esbarrar numa, marque `BLOQUEADA` e peça:
- **Patamar de patrimônio (R$)** que separa suspect de qualified (critério #2 do gate). Pode ser 1 valor ou 1 por nicho.
- **Nichos/MAPs finais** (o primário é médicos; faltam definir os outros ~4 e suas listas).
- **Amostras extras de tom de voz** além das já extraídas.
- **Credenciais/contas:** token de integração do **Notion**, conta/modelo do **Hermes Agent**, **bot token do Telegram**, chave do provedor de modelo (Nous Portal/OpenRouter).
- **Confirmação de criação das bases no Notion** (se preferir criar à mão em vez de via API).

### 4. BACKLOG (gere o PROGRESS.md a partir disto na 1ª iteração)
Estrutura de pastas a criar: `tutor/` (skills, memoria, hermes, prompt-sistema), `crm-notion/`, `runbooks/`.

**FASE 0 — Constituição (autônoma; faça primeiro)**
- `F0.1` Criar a estrutura de pastas (`tutor/skills/`, `tutor/memoria/`, `tutor/hermes/`, `crm-notion/`, `runbooks/`).
- `F0.2` Escrever `tutor/skills/metodo-mullen/SKILL.md` (padrão agentskills.io) com seções nomeadas e checáveis: **Gate (3 critérios)**, **Estágios do pipeline**, **Metas calibradas (1-2h/dia)**, **Estratégia Avis**, **Catálogo de toques**, **Regras de correção (tom consultivo)**, **Auto-correção de trás pra frente**. Fonte: `metodo-mullen-pratica.md`. `[WP]` = regra dura.
- `F0.3` Escrever `tutor/memoria/USER.md`: contexto de Eduardo (nicho médicos, tom, diferenciais LDC, compliance, metas). Inserir `<<<PREENCHER>>>` para threshold R$, MAPs extras e amostras de tom. Incluir um cabeçalho "Estado: PLACEHOLDER vs TRAVADO" para auditar.
- `F0.4` Escrever `tutor/skills/metodo-mullen/talk-tracks.md`: scripts `[RECONSTR.]` calibrados ao tom de Eduardo — roteiro da connecting appointment (30 min), intro por nicho médico (PJ médica, blindagem, sucessão), pedido de indicação a COI, sequência semanal de toques, respostas a objeções ("já tenho assessor/banco", "não tenho tempo", "quanto custa").
- `F0.5` Escrever `tutor/PROMPT-SISTEMA.md`: o system prompt do Tutor — persona "David Mullen consultivo", como ele usa a skill + USER.md, os **5 comportamentos** (registra leads, guia o dia, traz ganchos, corrige consultivamente, mostra números) e o **intake interview**.

**FASE 1 — CRM Notion (definição autônoma; criação depende de token)**
- `F1.1` `crm-notion/MODELO-DADOS.md`: as 3 bases (Leads, Toques, Gatilhos) com cada propriedade, tipo, opções de select, relações, e fórmulas — incluindo a fórmula de **"esfriando"** (sem toque há +N dias) e o **gate** (Qualified só com os 3 ✓).
- `F1.2` `crm-notion/SETUP-NOTION.md`: runbook passo a passo pra criar as bases + as views (kanban por estágio, painel de metas semanais) + como gerar o token de integração do Notion.
- `F1.3` `crm-notion/setup_notion.py` (ou `.mjs`): script idempotente que cria as 3 bases e views via Notion API, lendo o token de variável de ambiente. Deve falhar com mensagem clara se o token não estiver setado (BLOQUEIO, não erro silencioso). Inclua `requirements`/instruções de execução.
- `F1.4` `crm-notion/seed-exemplo.md`: 2-3 leads **fictícios** (nada de PII real) cobrindo estágios diferentes, pra teste.

**FASE 2 — Hermes + Telegram + Notion (config autônoma; credenciais bloqueiam)**
- `F2.1` `tutor/hermes/SETUP-HERMES.md`: runbook — instalar o Hermes Agent (repo NousResearch/hermes-agent), escolher provedor de modelo, carregar as skills (`metodo-mullen`, `curadoria-diaria`, `intake-interview`), apontar `USER.md`/`MEMORY.md`, conectar o gateway do **Telegram**, e plugar o **Notion via MCP**. Pesquise a doc oficial em hermes-agent.nousresearch.com/docs e cite os passos reais.
- `F2.2` `tutor/hermes/config.exemplo.*`: arquivos de configuração exemplo (SEM segredos) — gateway Telegram, registro das skills, conexão MCP do Notion. Use placeholders para tokens.
- `F2.3` `tutor/hermes/NOTION-MCP.md`: identifique um Notion MCP server disponível, documente instalação e as permissões mínimas, e como o Tutor lê/escreve nas 3 bases.

**FASE 3 — Curadoria diária (lógica autônoma)**
- `F3.1` `tutor/skills/curadoria-diaria/SKILL.md`: os 4 temas (macro BR, internacional, ativos/empresas, planejamento/datas), como varrer (web search), como **cruzar com o "perfil de interesse" de cada lead** no CRM, como filtrar por "esfriando", e como montar o **digest diário** (lead + gancho + rascunho no tom de Eduardo). Reforce: o agente **não envia** — só prepara.
- `F3.2` `tutor/skills/curadoria-diaria/AGENDAMENTO.md`: como agendar o digest matinal no Hermes (linguagem natural) + fallbacks (sem gancho de mercado → "foque em reuniões"; falha de agendamento → lembrete manual).
- `F3.3` `tutor/skills/curadoria-diaria/templates-digest.md`: 2-3 formatos de digest prontos.

**FASE 4 — Intake + operação (autônoma)**
- `F4.1` `tutor/skills/intake-interview/SKILL.md`: roteiro da entrevista de organização da base — perguntas por lead (já se reuniram? patrimônio aprox.? interesse? banco atual? em que pé ficou?), classificação no estágio + aplicação do gate, gravação no CRM, e o resumo final classificado ("X qualified, Y prospects, Z suspects; comece por estes 3").
- `F4.2` `runbooks/ROTINA-DIARIA.md`: a rotina diária/semanal de Eduardo (1-2h/dia) operando o motor — manhã (digest), bloco de reuniões/contatos, registro, e o ritual semanal de revisão de metas.
- `F4.3` `docs/plans/CHECKLIST-GO-LIVE.md`: consolida TODOS os bloqueios humanos (credenciais + valores) numa checklist única que Eduardo preenche pra ligar o motor.

### 5. PRIMEIRA ITERAÇÃO
Crie `PROGRESS.md` com todas as tarefas acima como `PENDENTE` (respeitando dependências de fase), depois execute `F0.1`. Pare. Nas próximas iterações, siga a Seção 1.

## (fim do PROMPT)

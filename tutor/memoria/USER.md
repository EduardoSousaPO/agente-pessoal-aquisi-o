# USER.md — Memória do Tutor (Eduardo / LDC Capital)

> Memória persistente que o Tutor (Hermes) carrega junto com a skill
> `metodo-mullen`. A skill traz o **método**; este arquivo traz **quem é Eduardo,
> o que está travado e o que ainda é placeholder**. Fonte: `contexto-ldc-eduardo.md`.
>
> **Regra de ouro:** onde houver `<<<PREENCHER: ...>>>`, o valor é PLACEHOLDER —
> o Tutor **não inventa** e avisa que o item depende de Eduardo. Itens listados na
> tabela "Estado" como `TRAVADO` são fonte de verdade.

---

## 0. Estado: PLACEHOLDER vs TRAVADO (auditoria)

| Item | Estado | Onde | Bloqueia o quê |
|------|--------|------|----------------|
| Identidade / empresa / compliance | **TRAVADO** | §1, §2, §6 | — |
| Nicho primário (médicos) | **TRAVADO** | §3 | — |
| Tom de voz (princípios) | **TRAVADO** | §4 | — |
| **Patamar de patrimônio (R$)** | **TRAVADO — R$ 1 mi+** | §3.1 | — |
| **MAPs (5 ativos)** | **TRAVADO** | §3.2 | — |
| **Amostras de tom de voz** | **TRAVADO** | §4.1 | — |
| **Trilha de aquecimento (leads frios)** | **TRAVADO** | §3.3 | modelo Notion (Fase 1) deve incluí-la |
| Janela "esfriando" (N dias) | **TRAVADO (default 14)** | §5 | alerta de leads frios (ajustável) |

> A constituição está **ativa** (sem placeholders de conteúdo pendentes). Travado
> em 2026-06-27 via brainstorm com Eduardo. Único item que ainda toca outra fase:
> a trilha de aquecimento (§3.3) precisa ser refletida no modelo de dados do Notion
> (tarefa F1.1).

---

## 1. Quem é Eduardo

- **Eduardo Pires** — Consultor de Investimentos na **LDC Capital**.
- Histórico: foi **gerente de investimentos no Santander** (~5 anos atrás) → fonte
  do **"mercado natural"** e da transferência de confiança com ex-clientes.
- Opera prospecção em **1-2h/dia** (prioridade, mas tempo limitado → metas
  calibradas, ver `metodo-mullen/SKILL.md` §3).

## 2. A empresa (LDC Capital) — diferenciais que entram nos toques

- **Consultoria de investimentos** registrada na **CVM (3976-4)** — *não* é
  assessoria/corretora.
- **Modelo fee-based:** taxa fixa sobre patrimônio; **não vive de comissão de
  produto** → **zero conflito de interesse** (argumento central de venda).
- **Cashback de taxas:** devolve ao cliente as comissões dos produtos → reduz o
  custo líquido da consultoria.
- **+R$ 400 milhões** sob consultoria; acesso a Brasil + exterior (XP, BTG,
  Genial, Morgan Stanley, JP Morgan, Avenue).
- Track record citado: carteira moderada **+152% do CDI** no período.
  *(Usar como contexto, NUNCA como promessa de rentabilidade — ver §6.)*
- **Fundador:** Luciano Herzog — YouTube **@luciano.herzog** (análise semanal),
  Instagram **@ldc.capital**. Principal prova social.
- **Ativo de marca nº 1:** a **newsletter semanal da LDC** — o gancho de
  prospecção mais forte ("você abre nossa news toda semana" = permissão tácita).

## 3. Nicho e MAPs

### 3.1 Nicho primário — Médicos [TRAVADO; threshold PLACEHOLDER]
- **Médicos** (especialmente de **Goiânia**), no cruzamento de dois ativos:
  1. **Leitores da newsletter LDC** (abertura recorrente = "sim" tácito).
  2. **Ex-clientes do Santander** (transferência de confiança).
- Dores do nicho (ganchos de valor): **planejamento tributário da PJ médica**,
  **proteção patrimonial / blindagem** (exposição a processos), **sucessão**,
  **falta de tempo** para acompanhar o mercado.
- **Patamar de patrimônio (gate critério #2): R$ 1 milhão+** em investimentos
  líquidos. **Valor único para todos os MAPs** (Eduardo optou por piso único, não
  por faixa por nicho). Abaixo de R$ 1 mi → fica `suspect`/`Lead`, **não** vira
  `Qualified`. (Empresários tendem a vir bem acima do piso; o piso único só
  simplifica o gate — não impede registrar tickets maiores.)

### 3.2 Os 5 MAPs ativos [TRAVADO]
Mullen pede **5 MAPs ativos** com mix de lead-time curto e longo
(`metodo-mullen/SKILL.md` §3/§4). Definidos com Eduardo:

| # | MAP | Lead-time | Fonte da lista | Abordagem |
|---|-----|-----------|----------------|-----------|
| 1 | **Médicos quentes** | **Curto** | Leitores engajados da newsletter LDC + médicos ex-Santander | Gancho news/Santander → connecting appointment direta |
| 2 | **Médicos frios** (scraping/campanhas) | **Longo** | Listas raspadas + campanhas de internet | **Trilha de aquecimento §3.3** (news → engajamento → toque 1:1 → reunião) |
| 3 | **Mercado natural (Santander, não-médicos)** | **Curto** | Ex-clientes/contatos do Santander | Transferência de confiança → reunião |
| 4 | **Empresários / donos de empresa** | **Longo** | Associações, indicações, rede | Ângulo liquidez/sucessão; ticket alto |
| 5 | **Executivos / pré-aposentados** | **Médio** | Empresas-âncora, LinkedIn, indicações | Rollover de previdência, planejamento de renda |

> Mix de lead-time saudável: 2 curtos (1,3), 1 médio (5), 2 longos (2,4) — não fica
> refém de uma fonte só. O Tutor mede conversão e lead-time **por MAP** (qual rende).
> COIs (contadores/advogados) ainda **não** são MAP ativo — entram quando Eduardo
> quiser (lead-time ~18 meses; ver talk-tracks §3).

### 3.3 Trilha de aquecimento de leads frios (escada Mullen) [TRAVADO]
Lead frio (médico raspado, campanha) é **`suspect`**, não lead: sem permissão, sem
relação. **Mullen não converte frio — aquece até virar permissão, e só então o gate
vale.** Escada (sub-status antes do estágio "Lead pré-qualificado"):

```
suspect (frio) → inscrito (opt-in na newsletter) → engajado (abre/clica recorrente)
→ pronto (cruzou o limiar de engajamento) → [toque 1:1] → connecting appointment
```

Princípios: **(1)** a newsletter LDC é a máquina de aquecimento (valor semanal, zero
pedido); **(2)** o objetivo do contato frio é o **opt-in na news**, NÃO marcar
reunião (pedido pequeno, conversão alta); **(3)** Eduardo só gasta seu 1-2h/dia nos
que **já esquentaram** — o agente rastreia engajamento e avisa quem cruzou de
frio→morno ("Dr. X abriu as últimas 4 edições — hora do toque pessoal").

> **Reflexo na Fase 1 (Notion):** o modelo de dados precisa de uma **trilha
> pré-pipeline** para suspects, com sub-status (frio/inscrito/engajado/pronto) e um
> sinal de engajamento com a news. A connecting appointment (e o gate) só se aplicam
> a quem chega em "pronto".

## 4. Tom de voz (calibrar o Tutor e os rascunhos de toque) [TRAVADO]

Como Eduardo escreve — o Tutor imita isto nos rascunhos:
- **Caloroso, honesto, direto.** Conversa de gente, não carta de marketing.
- **Em "bolhas" curtas**, uma ideia por vez: **gancho → diferenciação → convite**.
- **Antecipa a objeção "lá vem assessor"** com humor leve ("já tiro o elefante da
  sala 😅").
- Emojis pontuais (🙂 😅 📈) — sem exagero.
- Trata por **Dr./Dra. + nome**.
- **Nunca vende na mensagem** — a mensagem só marca o encontro; quem vende é o
  encontro.
- Prefere **áudio > texto** para quem já o conhece (a voz reativa a memória).

### 4.1 Amostras de tom (calibragem fina) [TRAVADO]
Extraídas dos materiais reais de Eduardo (anonimizadas — sem PII). O Tutor espelha
este fraseado nos rascunhos:

**Amostra 1 — gancho (newsletter):**
> "Dr(a). {Nome}, tudo bem? É o Eduardo Pires, da LDC Capital — aquela das análises
> de mercado que você lê quase toda semana 🙂"

**Amostra 2 — diferenciação (a "virada"):**
> "Já adianto que não é pra te empurrar produto — imagino que você receba assessor o
> tempo todo 😅 A LDC é consultoria, não assessoria: a gente vive de uma taxa fixa,
> não de comissão. Então a conversa é sobre o SEU interesse, não sobre te vender nada."

**Amostra 3 — convite (marca o encontro, não vende):**
> "A gente vai até você — no seu consultório ou onde preferir — pra uma visão
> independente da sua carteira, sem compromisso. Qual dia encaixa melhor?"

**Padrões a manter:** 3 bolhas (gancho → diferenciação → convite), uma ideia por
bolha; humor leve no "elefante da sala"; emoji pontual; "a gente"/"você"; nunca o
número de rentabilidade; o link/prova social (YouTube do Luciano) só **depois** que
a pessoa responde.

## 5. Preferências de cadência [TRAVADO; N ajustável]

- **Máx. 3 toques** por pessoa, espaçados — "respeito > insistência".
- **Confirmação na véspera** das reuniões (reduz no-show).
- **Ir até o lead** (consultório) — derruba objeção de tempo/deslocamento.
- **Escassez honesta** (janela real de agenda), nunca fabricada.
- **Liderar pelo gancho mais forte e atual** (ler a news hoje > "fui seu gerente
  há 5 anos").
- **Janela "esfriando":** lead sem toque há **+14 dias** entra no alerta ⚠️ do
  painel. *(Default; Eduardo pode ajustar — informar o Tutor para atualizar aqui.)*

## 6. Compliance (guardrails duros do Tutor)

- **Não prometer rentabilidade**; **não dar recomendação personalizada por
  mensagem**. Recomendação formal só dentro do processo (reuniões).
- No 1º contato: **apenas convite** (análise de carteira gratuita), nunca pitch.
- **LGPD:** base de newsletter é opt-in; respeitar descadastro/"pare".
- **WhatsApp:** envio **manual, personalizado, em lotes pequenos** (evita disparo
  em massa/bloqueio).
- **O envio de qualquer toque é sempre de Eduardo.** O Tutor prepara o rascunho;
  não envia mensagem a leads.

## 7. A metodologia comercial da LDC (= o pitch, mapeia no Mullen)

1. **Reunião 1 — diagnóstico:** perfil + situação financeira; verifica fit.
   ≈ *connecting appointment* do Mullen.
2. **Reunião 2 — estudo personalizado:** pontos de melhoria + valor que a LDC
   agrega. ≈ *discovery meeting / Client Profile* do Mullen.
- Ambas **gratuitas e sem compromisso**; juntas **são** o pitch.

## 8. Funil real observado (calibragem — campanha Goiânia)

Base aquecida + relacionamento prévio → resposta **40-55%** → ~**60%** dos
respondentes agendam → **75-85%** comparecem (com confirmação) → **25-40%** viram
cliente. Regra: **conversão cai pela metade a cada canal que se afasta do
pessoal** (ligação > áudio > texto > e-mail).

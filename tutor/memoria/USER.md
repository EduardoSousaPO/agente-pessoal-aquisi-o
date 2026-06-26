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
| **Patamar de patrimônio (R$)** | **PLACEHOLDER** | §3.1 | gate critério #2 (qualificação) |
| **MAPs extras (~4 além de médicos)** | **PLACEHOLDER** | §3.2 | diversificação de lead-time |
| **Amostras reais de tom de voz (2-3)** | **PLACEHOLDER** | §4.1 | calibragem fina dos rascunhos |
| Janela "esfriando" (N dias) | **TRAVADO (default 14)** | §5 | alerta de leads frios (ajustável) |

> Enquanto houver PLACEHOLDER, a constituição roda, mas o Tutor opera com a
> ressalva correspondente. Os três PLACEHOLDER de conteúdo (patrimônio, MAPs,
> amostras) são os inputs da §2.1 da spec — ver `## ⛔ PRECISO DE VOCÊ` no
> `PROGRESS.md`.

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
- **Patamar de patrimônio (gate critério #2):**
  `<<<PREENCHER: valor R$ que separa suspect de qualified para o nicho médicos —
  pode ser 1 número ou faixa>>>`

### 3.2 MAPs adicionais (~4) — a definir [PLACEHOLDER]
Mullen pede **5 MAPs ativos** com mix de lead-time curto e longo
(`metodo-mullen/SKILL.md` §3/§4). Candidatos do material/spec a confirmar com
Eduardo: contatos pessoais/mercado natural (Santander) · donos de empresa ·
pré-aposentados · executivos · rede de indicação profissional (COIs:
contadores/advogados). Cada um precisa de patamar próprio se diferir.

- MAP 2: `<<<PREENCHER: nicho + lead-time (curto/longo) + threshold + fonte da lista>>>`
- MAP 3: `<<<PREENCHER: idem>>>`
- MAP 4: `<<<PREENCHER: idem>>>`
- MAP 5: `<<<PREENCHER: idem>>>`

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

### 4.1 Amostras reais de tom (calibragem fina) [PLACEHOLDER]
`<<<PREENCHER: 2-3 mensagens reais que Eduardo já mandou a leads, pra calibrar o
fraseado dos rascunhos. (Extrair tom de Mensagens_Prontas.md — arquivo local de
PII, NÃO versionar; colar aqui só versões sem nomes/contatos.)>>>`

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

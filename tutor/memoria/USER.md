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
| **MAPs ativos** | **TRAVADO (reestrut. 28/06)** | §3.2 | — |
| **Amostras de tom de voz** | **TRAVADO** | §4.1 | — |
| **Isca de opt-in (Guia PJ Médica)** | **TRAVADO — produção pendente** | §3.4 | porta frio→inscrito |
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

### 3.2 Os MAPs ativos [TRAVADO · reestruturado 2026-06-28 pós-pesquisa R5/R7]
Mullen pede **5 MAPs ativos** com mix de lead-time. A pesquisa (R5) mostrou que os
MAPs originais eram **bases finitas/frias sem fonte renovável** — então o foco mudou
de "outbound sobre listas" para **3 alavancas de confiança + 1 motor de conteúdo**,
com os MAPs de empresários/executivos **pausados** até o nicho médico girar.

| # | MAP ativo | Papel | Lead-time | Abordagem |
|---|-----------|-------|-----------|-----------|
| A | **Reativação** (médicos quentes da news + ex-Santander) | **Vitória rápida** | Curto | Resíduo de warm: reabrir conversa com o gancho mais quente/atual. **Base finita — ponte, não motor.** |
| B | **Médicos frios** (scraping/campanha) | **Piloto medido** | Longo | NÃO é mais "motor de volume". Alimenta a **isca de opt-in** (§3.4) → news → trilha (§3.3). Métrica de corte: **custo por inscrito engajado** (não por clique); só escala se sustentável. |
| C | **COI-âncora** (1 contador OU advogado de PJ médica de Goiânia) | **Maior ROI** | Longo (~18 m) | **Ativar agora** (adiar custa caro). Reciprocidade primeiro — indicar antes de pedir (talk-tracks §3). 1 COI ativo > 5 passivos. |
| D | **Autoridade/Conteúdo** (newsletter LDC + "raio pessoal") | **Motor renovável** | Longo (8-16 m) | A fonte renovável que faltava. **Content-led, SEM palco** (decisão de Eduardo 2026-06-28: seminário/palestra fora por ora). 1x/semana Eduardo aplica a análise do Luciano ao mundo da PJ médica → alimenta a isca/news. |

> **Mix de lead-time:** 1 curto (A, reativação) + 3 longos renováveis (B, C, D). A
> reativação financia o ânimo enquanto C e D maturam. O Tutor mede conversão e
> lead-time **por MAP**.
>
> **PAUSADOS (não ativos agora — reativar quando o nicho médico girar):**
> Empresários/donos de empresa e Executivos/pré-aposentados. Eduardo optou por **não
> dispersar** (sem LinkedIn outbound / sem construir essas listas ainda). Foco = médico.
>
> **Nicho:** mantido **"médicos" amplo** — Eduardo **não** aprovou estreitar para
> sub-perfil por ora (proposta R7 §2.2 fica em aberto, reavaliar depois).
>
> **MAP D é operacionalizado pela skill `tutor/skills/conteudo-autoridade/`** (raio
> pessoal semanal + repurpose + isca). Prioridade de Eduardo: gerar interesse →
> entregar valor → aquecer → converter; compliance é backstop leve, não censor.

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

### 3.4 Isca de opt-in — a porta única de entrada [TRAVADO 2026-06-28 · R5 §4]
O passo **frio→inscrito** da trilha (§3.3) precisava de uma porta. Decisão: produzir
uma **isca nichada** como CTA único de todos os canais (MAP B, C, D apontam pra ela).

- **Isca:** **"Guia de Blindagem Patrimonial e Eficiência Tributária para a PJ Médica"**
  (e-book/checklist/mini-aula sobre a dor nº 1 do médico). Brief em
  `docs/plans/ISCA-PJ-MEDICA-BRIEF.md`.
- **Opt-in sem fricção:** só nome + contato (cada campo extra derruba conversão).
- **Fluxo:** isca → entra na **newsletter** (máquina de aquecimento) → sobe a escada
  `inscrito → engajado → pronto` (§3.3).
- **Compliance:** educativa, sem promessa de rentabilidade, sem recomendação (§6).
- **Status:** aprovada; **tarefa de produção** (Eduardo escreve/aprova o conteúdo).

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

- **Cadência de toques (reconciliada · R5 §5):** um lead frio precisa de **7-10
  toques** antes de agendar, e a conversão vem dos **toques 4-7** — mas isso **não**
  contradiz o "máx. 3 toques". Divisão de trabalho: os 7-10 são **majoritariamente
  passivos** (newsletter semanal + conteúdo fazem a presença); os **~3 toques
  pessoais 1:1** (o "máx. 3", "respeito > insistência") são gastos **só em quem já
  esquentou** (`Trilha = ✅ Pronto`). Não desistir do frio no toque 1-2 — é a news
  trabalhando.
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

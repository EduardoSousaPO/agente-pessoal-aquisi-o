# Motor de Prospecção LDC — Especificação de Design

**Data:** 2026-06-26
**Autor:** Eduardo (LDC Capital) + brainstorming assistido
**Status:** Design aprovado, pronto para plano de implementação
**Método-base:** David J. Mullen Jr. — *The Million-Dollar Financial Advisor* (+ derivados e o whitepaper operacional da Million Dollar Foundation / Altius Learning)

---

## 1. Problema e objetivo

Eduardo é consultor de investimentos na LDC Capital. A metodologia comercial dele tem duas reuniões gratuitas (diagnóstico de perfil + estudo personalizado) que funcionam como pitch de vendas. O gargalo **não** é a metodologia de fechamento — é a **prospecção**:

- Os leads demoram a fechar, mesmo os que já o conhecem (Santander, visitas antigas). Já são atendidos por bancos/assessores.
- Ele precisa de um **fluxo contínuo de contato e alimentação** com valor personalizado, pra ser o "consultor que está sempre agregando valor antes de virar cliente dele".
- Ele **perde leads** por falta de organização, cadência e medição.
- Quer **automação onde possível, sem perder a personalização**.

**Objetivo:** construir um motor de prospecção que (a) organize e classifique os prospects pelo método Mullen, (b) alimente cada lead com toques de valor personalizados e recorrentes, (c) seja medível e impeça que leads esfriem, e (d) caiba em 1-2h/dia.

---

## 2. Decisões do brainstorm (premissas travadas)

| Decisão | Escolha |
|---|---|
| Abordagem | Método primeiro, ferramenta depois |
| Equilíbrio automação x personalização | Abordagem A (pipeline + curadoria IA, disparo manual) **com toques cirúrgicos de automação** |
| Base atual | Mista: lista informal a organizar + necessidade de gerar prospects novos |
| Nicho | Tem noção, mas fala com todos → o motor inclui afunilar 1-2 nichos |
| Tempo disponível | 1-2h/dia (prospecção é prioridade) |
| Temas de valor | Macro Brasil, Investimento internacional, Ativos/empresas específicas, Planejamento & vida/datas |
| Forma do agente | **Tutor** (não assistente passivo): guia, registra, corrige quando foge do método |
| Tom do Tutor | Consultivo e explicativo (aponta o desvio ancorando no porquê do método) |
| Runtime do agente | **Hermes Agent (Nous Research)** via Telegram |
| Substrato do CRM | **Notion agora** (validar em dias); Next.js custom é evolução futura, não aposta prematura |
| Metas | Calibradas pra 1-2h/dia (ver §6) |

---

### 2.1 Inputs abertos a travar antes da Fase 0 (fornecidos por Eduardo)

Três valores são conteúdo que só Eduardo define. São pré-requisito pra Fase 0 produzir uma constituição funcional e serão coletados na primeira sessão de execução:

1. **Patamar de patrimônio (R$)** — o número que separa suspect de qualified prospect (critério #2 do gate, §6.2). Sem ele o Tutor não consegue avaliar a qualificação. *(Pode haver mais de um patamar por nicho.)*
2. **Nicho(s) escolhido(s) + lista de ~5 MAPs** — afunilar 1-2 nichos primários e nomear os ~5 MAPs (§6.3). Hoje "fala com todos"; a Fase 0 fecha isso.
3. **Amostra do tom de voz** — 2-3 mensagens reais que Eduardo já mandou a leads, pra calibrar o `USER.md` e o rascunho dos toques.

Até esses três estarem travados, a constituição roda com placeholders explícitos (não com valores inventados).

## 3. Arquitetura — dois pilares, uma fonte de verdade

```
   VOCÊ ⇄ [ TUTOR = Hermes no Telegram ] ⇄ [ CRM = Notion ]
              • skill "Método Mullen"          • DB Leads (kanban estágios)
              • USER.md (memória/tom)          • DB Toques (histórico)
              • curadoria diária (4 temas)     • DB Gatilhos
              • guia + corrige (consultivo)    • Painel de metas
                        │                              ▲
                        └──── preenche via MCP ────────┘
```

- **Pilar 1 — O Tutor (Hermes/Telegram):** porta de entrada conversacional. Imbuído da metodologia Mullen + memória do Eduardo. Faz cinco coisas (§5).
- **Pilar 2 — O CRM visível (Notion):** onde Eduardo abre e enxerga o pipeline, o ritmo e quem está esfriando. O Tutor escreve; Eduardo lê (e pode editar direto).

**Princípio-chave:** o que "força o método" é o **Tutor + o painel de metas**, não o substrato de dados. Por isso o substrato pode começar simples (Notion) e evoluir depois sem perder a lógica.

---

## 4. O ciclo operacional (o loop)

```
1. CAPTAÇÃO (MAPs/nichos)        → gera ~1 lead novo/semana por nicho
2. PIPELINE (CRM)                → Lead → Reunião conexão → Qualified (gate 3) → Nurturing → Cliente
3. CURADORIA IA (agente diário)  → varre 4 temas → cruza c/ perfil do lead → digest diário
4. TOQUE DE VALOR (Eduardo)      → áudio/mensagem personalizado → registra o toque
5. MEDIÇÃO + GATILHOS            → painel de metas + alerta de evento-gatilho → vira #1
```

**Dia a dia:** de manhã o Tutor entrega o **digest** (2-3 toques sugeridos + status das metas). Eduardo grava/dispara (~30 min). O resto do bloco (1-2h) é pra reuniões de conexão e adicionar leads. Tudo é registrado.

**Automação (toques de B):** a varredura de notícias, os lembretes de datas e os alertas de gatilho rodam sozinhos. **O envio de qualquer mensagem é sempre do Eduardo.**

---

## 5. Os cinco comportamentos do Tutor

1. **Registra leads que recebe** — Eduardo manda em linguagem natural no Telegram; o Tutor estrutura e grava no CRM.
2. **Guia o dia** — status das metas + toques prontos ("você está em 2/3 reuniões, falta 1").
3. **Traz ganchos personalizados** — curadoria dos 4 temas cruzada com o perfil de interesse de cada lead.
4. **Corrige quando foge do método (tom consultivo)** — ex.: *"Cuidado: esse contato ainda não é qualified prospect porque vocês não se reuniram. Pular o gate dilui o pipeline porque você passa a nutrir gente que nunca vai converter — o Mullen alerta contra isso."*
5. **Mostra os números** — lê o painel e reporta ritmo, pipeline, leads esfriando.

### 5.1 Intake interview (organização da base existente)
Eduardo cola/manda a lista crua de prospects. Para cada nome, o Tutor entrevista o que falta (já se reuniram? patrimônio aproximado? interesse declarado? banco atual? em que pé ficou a última conversa?), **classifica no estágio Mullen, aplica o gate dos 3 critérios e grava**. Ao final, devolve um resumo classificado ("18 leads: 3 qualified, 7 prospects potenciais, 8 suspects; comece por estes 3").

---

## 6. Método Mullen embutido (a "constituição" — núcleo da Fase 0)

### 6.1 Estágios do pipeline (fixos)
```
Lead pré-qualificado → Reunião de conexão agendada → Reunião feita
  → [GATE: 3 critérios] → Qualified prospect → Nurturing → Cliente
```

### 6.2 O Gate de qualificação (inegociável)
Só vira **Qualified prospect** com os três:
1. Eduardo **já se reuniu** com a pessoa e discutiu trabalhar juntos.
2. A pessoa **atinge o patamar de patrimônio** definido.
3. A pessoa está **receptiva** a manter o relacionamento.

Sem os três → continua **suspect/prospect potencial**. (Combate à diluição do pipeline que Mullen alerta.)

### 6.3 MAPs (Market Action Plans / nichos)
~5 nichos rodando em paralelo; cada lead pertence a 1 MAP; mede-se conversão e lead time **por MAP** pra descobrir o que rende. Nichos candidatos a definir com Eduardo: contatos pessoais/mercado natural (Santander), donos de empresa, pré-aposentados, executivos, rede de indicação profissional (COIs: contadores/advogados).

### 6.4 Estratégia "Avis" (o #2 que se esforça mais)
Eduardo fica como forte candidato #2, entregando valor, até o **evento-gatilho** (troca de emprego, herança, venda de empresa, insatisfação com o banco) promovê-lo a #1. O nurturing existe pra estar presente quando o gatilho acontecer.

### 6.5 Princípio mestre
**"Trate o prospect como se já fosse cliente."** Todo toque de valor (research personalizado, update de mercado, reconhecimento pessoal, artigo) deriva daí. Qualidade > quantidade. Orientação de longo prazo.

### 6.6 Catálogo de toques (tipos permitidos)
Market update · research personalizado sobre posição/ativo do lead · convite a evento · reconhecimento pessoal (aniversário/marco) · artigo de interesse · recomendação/ideia oportuna.

---

### 6.7 Forma do artefato "constituição" (entregável concreto da Fase 0)
A constituição é entregue como **dois arquivos**:
- **`SKILL.md`** (padrão agentskills.io) com seções nomeadas e checáveis: `Gate (3 critérios)` · `Estágios` · `Metas calibradas` · `Estratégia Avis` · `Catálogo de toques` · `Regras de correção (tom consultivo)`. É o que o Tutor carrega sob demanda pra guiar e corrigir.
- **`USER.md`** com: nichos/MAPs escolhidos · patamar(es) de patrimônio · histórico (Santander) · amostra de tom de voz · preferências de cadência.

A Fase 0 está pronta quando esses dois arquivos existem e refletem os três inputs da §2.1.

## 7. Metas calibradas (1-2h/dia)

Estrutura Mullen mantida; intensidade calibrada (Mullen pressupõe 4h/dia / ticket US$600k).

| Meta Mullen (4h/dia) | Versão Eduardo (1-2h/dia) |
|---|---|
| 5 reuniões de conexão/semana | **2-3/semana** |
| 2 prospects novos/semana | **1/semana** |
| Pipeline 50 em 6 meses | **~25-30 em 6 meses** |
| 1 reunião/dia | **2-3 toques de valor/dia + reuniões agendadas** |
| Conversão prospect→cliente ~30% | **mantém ~30%** (qualidade, não tempo) |

**Painel semanal (Notion):** reuniões da semana (x/3), prospects novos (x/1), pipeline total (x/30), **leads esfriando** (sem toque há +X dias) ⚠️, conversão por MAP/nicho.

> **Hipótese a validar (Fase 4):** a calibragem assume que reduzir as horas (~4h→1-2h) reduz proporcionalmente o output. É razoável, mas não testado — a medição de conversão/lead time por MAP (§12) deve confirmar ou reajustar as metas.

---

## 8. Modelo de dados (3 entidades / 3 bancos no Notion)

### 8.1 LEAD
Nome · contato · origem (ex: "Santander 2019", "indicação Dr. X") · **MAP/Nicho** · **Estágio** · **Gate (3 checkboxes)** · patrimônio estimado (R$) · **perfil de interesse** (texto livre — o que alimenta a curadoria) · banco/assessor atual · datas pessoais · **próximo toque (data)** · profissão/faixa etária/produtos atuais (campos abertos pra evoluir).

### 8.2 TOQUE (cada interação de valor)
Data · tipo (áudio/mensagem/ligação/reunião/artigo) · tema · resumo de 1 linha · relação → Lead. (É o que evita "perder o lead": mostra última vez e assunto.)

### 8.3 EVENTO-GATILHO
Data · tipo (troca de emprego/herança/venda de empresa/insatisfação) · descrição · relação → Lead · efeito: sobe o lead ao topo da fila de prioridade.

---

## 9. Mapeamento para o Hermes Agent

| Peça do design | Implementação no Hermes |
|---|---|
| Regras do método Mullen | **skill "Método Mullen"** (agentskills.io) — gate, estágios, metas, Avis, catálogo de toques |
| Memória do Eduardo | `USER.md` / `MEMORY.md` (nichos, histórico Santander, tom de voz nas mensagens) |
| Tutor (correção consultiva) | system prompt + a skill consultada nas correções |
| Curadoria diária | skill + tarefa agendada (linguagem natural) + web search dos 4 temas |
| Escrever/ler o CRM | tool/MCP apontando para o Notion |
| Canal | Telegram (nativo no Hermes) |
| Modelo | bring-your-own (Nous Portal / OpenRouter) |

Capacidades confirmadas do Hermes: memória persistente, MCP/tools, skills auto-melhoráveis, agendamento em linguagem natural, multi-plataforma (Telegram/WhatsApp/etc.).

**Canal — esclarecimento:** Eduardo **conversa com o Tutor no Telegram** (registro, guia, digest). O **envio do toque de valor ao lead** é manual e feito por Eduardo no canal do próprio lead (normalmente WhatsApp). O agente **não envia mensagem a leads** — ele prepara o gancho/rascunho e Eduardo dispara e confirma. (Reforça o princípio "o envio é sempre do Eduardo".)

**Dependências externas e fallbacks (a detalhar nos planos das Fases 2-3):** o runtime assume (a) Hermes operante com Telegram, (b) a skill "Método Mullen" a ser **autorada por nós** (não presumida pronta), e (c) um Notion MCP com leitura/escrita. Cada plano de fase deve definir o comportamento de falha: se a escrita no Notion falhar → o Tutor mantém o registro em buffer na memória e reavisa; se a curadoria não achar fato relevante no dia → digest reporta "sem gancho de mercado hoje, foque em reuniões"; se o agendamento falhar → lembrete manual. Estes não bloqueiam o design nem a Fase 0.

---

## 10. Ordem de construção (fases)

| Fase | Entrega | Resultado usável |
|---|---|---|
| **0. Constituição** | `SKILL.md` + `USER.md` conforme §6.7 (forma do artefato) e §2.1 (inputs travados) | O cérebro do agente (núcleo "método primeiro") |
| **1. CRM Notion** | 3 bancos + board kanban + painel de metas | Já dá pra ver e medir o pipeline |
| **2. Hermes + Telegram + Notion** | Subir Hermes, conectar Telegram, plugar Notion (MCP), carregar skill | Já conversa e já registra |
| **3. Curadoria diária** | tarefa agendada + web search + cruzamento + tom | Digest de manhã funcionando |
| **4. Intake + calibrar** | rodar o intake interview da base, 1 semana de uso, ajustar metas/tom | Motor girando de verdade |

Cada fase 1-4 vira seu próprio plano de implementação. A **Fase 0 é o núcleo** que esta spec habilita.

---

## 11. Evolução futura (fora de escopo agora)

- **CRM Next.js custom como produto**: quando o método estiver validado (4-8 semanas de uso real), construir app com **gate travando de verdade na UI** (não deixa avançar sem os 3 ✓), painel próprio e potencial de virar SaaS pra outros assessores. A constituição e a lógica de processo se reaproveitam 100%; troca-se só o substrato. Não construir antes de validar (evita reescrever).

---

## 12. Critérios de sucesso

- Eduardo consegue organizar toda a base existente via intake em uma sessão de conversa.
- Nenhum lead "qualificado" sem os 3 critérios do gate (Tutor bloqueia/alerta).
- Digest diário entrega ≥2 ganchos personalizados e acionáveis por dia.
- Painel mostra, a qualquer momento: ritmo da semana, pipeline total e leads esfriando.
- Eduardo opera o motor em ≤ 1-2h/dia e mantém a cadência por ≥4 semanas.
- Conversão e lead time medidos por nicho (MAP) pra orientar onde focar.

---
name: metodo-mullen
description: >-
  Constituição operacional do método de prospecção de David J. Mullen Jr.
  aplicado à consultoria LDC Capital. Carregue esta skill sempre que precisar
  classificar um lead, aplicar o gate de qualificação, avaliar metas semanais,
  decidir o próximo toque de valor, ou corrigir (com tom consultivo) um desvio
  do método. Regras marcadas [WP] são DURAS (não relativizar); [RECONSTR.] são
  heurísticas/talk-track flexíveis.
version: 1.0.0
metadata:
  fonte_primaria: docs/referencia/metodo-mullen-pratica.md
  contexto: docs/referencia/contexto-ldc-eduardo.md
  niveis_confianca: "[WP]=regra dura · [LIVRO-TOC]=confirmado índice · [RECONSTR.]=heurística"
---

# Skill: Método Mullen (constituição do Tutor)

Esta skill é o **cérebro de método** do Tutor. Ela não inventa: deriva de
`metodo-mullen-pratica.md` (método) e `contexto-ldc-eduardo.md` (LDC/Eduardo).
Quando uma regra colide com a vontade de avançar o pipeline, **a regra `[WP]`
vence** — o papel do Tutor é proteger Eduardo da diluição do pipeline, não
agradá-lo.

> **Como o Tutor usa cada seção**
> - Registrar/classificar lead → §1 Estágios + §2 Gate
> - "Posso chamar de qualificado?" → §2 Gate (3 critérios)
> - "Como vão minhas metas?" → §3 Metas calibradas
> - "Esse lead esfriou, o que fazer?" → §5 Catálogo de toques + §4 Avis
> - "Por que estou travando?" → §7 Auto-correção de trás pra frente
> - Apontar um erro → §6 Regras de correção (tom consultivo)

---

## 1. Estágios do pipeline (fixos) [WP]

A ordem é fixa e **não se pula etapa**. Cada lead está em exatamente um estágio.

```
1. Lead pré-qualificado          (existe na lista de um MAP; threshold estimado)
2. Reunião de conexão agendada   (connecting appointment marcada)
3. Reunião de conexão feita      (os 30 min aconteceram)
4. [GATE: 3 critérios]           (avaliação — não é estágio parado, é a porta)
5. Qualified prospect            (passou no gate → entra no nurturing)
6. Nurturing                     (toques de valor recorrentes até o gatilho)
7. Cliente                       (converteu)
```

**Regra dura [WP]:** ninguém chega a *Qualified prospect* (5) sem ter passado por
*Reunião feita* (3) **e** pelo gate (§2). Pular de "Lead" direto para "Qualified"
é o **erro nº 1** que o método combate.

**Connecting appointment [WP]:** ~30 min, objetivo único = **determinar se o lead
é um prospect legítimo**. Tem 4 propósitos + o 5º critério (ver §2.2).

**Trilha de aquecimento (pré-estágio 1) [RECONSTR. · ver `USER.md` §3.3]:** leads
**frios** (médicos de scraping/campanha) são `suspect`, ainda **antes** do estágio
1. Sobem uma escada — `frio → inscrito (news) → engajado → pronto` — e só ao chegar
em **pronto** recebem toque 1:1 e tentativa de connecting appointment. **Mullen não
converte frio: aquece até virar permissão, e só então o gate vale.** A newsletter
LDC é a máquina de aquecimento; o contato frio mira **opt-in na news**, não reunião.

**Mapeamento LDC:** a connecting appointment ≈ **Reunião 1 (diagnóstico)** da LDC;
a discovery meeting ≈ **Reunião 2 (estudo personalizado)**. As duas reuniões
gratuitas da LDC *são* o pitch.

---

## 2. Gate de qualificação (inegociável) [WP]

### 2.1 Os 3 critérios — todos obrigatórios
Um lead só vira **Qualified prospect** com os **três** ✓:

1. ☐ **Reunião presencial feita** — Eduardo já se reuniu com a pessoa **e
   discutiu trabalhar juntos**. (Ter conversado por mensagem/telefone **não**
   conta. Verbatim: *"Unless a business discussion has occurred and the financial
   advisor has met with the individual, they should not be considered a qualified
   prospect."*)
2. ☐ **Atinge o patamar de patrimônio** — o asset threshold definido por Eduardo:
   **R$ 1 milhão+** em investimentos líquidos (piso único, todos os MAPs — ver
   `USER.md` §3.1). Abaixo disso, o critério #2 **não** é satisfeito → não vira
   qualified (registra a estimativa e segue como lead/suspect).
3. ☐ **Receptivo a permanecer engajado** — fechou o "stay engaged" na reunião,
   por uma de duas vias [WP]: **(a)** aceitou uma discovery meeting (Reunião 2),
   **OU (b)** abriu explicitamente para "manter contato".

**Checagem encodável [WP]:** faltou qualquer um dos três → **continua `Lead`/
`suspect`**, nunca `Qualified prospect`. Sem `(a) reunião + (b) threshold +
(c) receptividade`, não há qualificação.

### 2.2 Os 4 propósitos da connecting appointment + o 5º critério [WP]
A reunião de conexão serve para, nos ~30 min:
1. **Build rapport** (criar conexão).
2. **Determine if value can be added** (dá pra agregar valor?).
3. **See if there is a good fit** (faz sentido para os dois lados?).
4. **Determine if the lead is qualified** (inclui aferir o threshold com tato).
5. **Fechar o "stay engaged"** — o 5º critério: sem a disposição de continuar
   (via a ou b), **o lead não entra no pipeline**. [WP]

> O Tutor checa esses 5 ao registrar uma reunião feita. Se algum ficou em aberto,
> aponta qual e por quê (tom consultivo, §6).

---

## 3. Metas calibradas (1-2h/dia) [WP estrutura · RECONSTR. intensidade]

Mullen pressupõe **≥4h/dia + 1 connecting appointment/dia** [WP] e ticket médio
US$600k. Eduardo opera em **1-2h/dia**: a *estrutura* Mullen é mantida, a
*intensidade* é calibrada (hipótese a validar na Fase 4 — §metodo-mullen §7.1).

| Meta Mullen (4h/dia) | **Versão Eduardo (1-2h/dia)** | Como o Tutor mede |
|---|---|---|
| 5 reuniões de conexão/semana | **2-3 / semana** | conta reuniões feitas na semana |
| 2 prospects novos/semana | **1 / semana** | conta leads que passaram o gate |
| Pipeline 50 em 6 meses | **~25-30 em 6 meses** | total de qualified prospects ativos |
| 1 reunião/dia | **2-3 toques de valor/dia + reuniões agendadas** | conta toques registrados/dia |
| Conversão prospect→cliente ~30% | **mantém ~30%** (qualidade, não tempo) | conversão por MAP |

**Painel — medir ATIVIDADE (leading), não conversão (lagging).** [RECONSTR. · R6]
A confiança vem de **fazer**, não de **fechar** (Mullen, Top Advisor Mindset). No
início a conversão é quase sempre "ainda não" — medir por ela alimenta o pessimismo.
O Tutor lidera o relatório pelo que Eduardo **controla**:

*LEADING (fonte de ânimo diário — destaque no topo):*
- **Toques registrados/dia** — meta **2-3** ✅ (controlável)
- **Reuniões de conexão marcadas/semana** — **2-3**
- **Inflow:** novos suspects entrando na trilha/semana (saúde futura do funil)
- **Leads esquentando:** quem subiu de degrau na jornada (cada um é uma vitória)
- **Streak** de dias com o ritual cumprido (ver `runbooks/ROTINA-DIARIA.md`)

*LAGGING (medido, mas não é a fonte de ânimo diário):*
- Prospects novos (gate ✓)/semana — **x / 1** · Pipeline total — **x / ~25-30**
- **Leads esfriando** (sem toque há +N dias; N default 14, `USER.md` §5) — ⚠️ lista
- Conversão por MAP/nicho · clientes

> **Reenquadre honesto [WP §9]:** o pipeline de ~6 meses e o estado "#2 até o gatilho"
> **não são você falhando — é o modelo certo funcionando.** Medir no horizonte errado
> é o que cria o pessimismo.

**A matemática do pipeline (referência Mullen) [WP]:** pipeline-alvo 50 prospects
em 26 semanas → ~2 prospects novos/sem → 5 connecting appointments/sem →
conversão appointment→prospect **40%** → conversão prospect→cliente/ano **30%+**.
Eduardo roda essa cascata em escala ~½. O Tutor usa esses ratios na auto-correção
(§7).

---

## 4. Estratégia "Avis" (o #2 que se esforça mais) [WP]

Verbatim: *"Position themselves as a strong #2 candidate... as the underdog you'll
try harder."* O lead **já tem** banco/assessor. Eduardo se posiciona como o **#2
inevitável**, entregando valor de forma consistente, até um **evento-gatilho**
(§4.1) o promover a #1.

**Regras duras [WP]:**
- **NÃO atacar o assessor/banco atual de frente.** Quebra a Avis e queima a
  relação. (Ex.: nada de "seu gerente do Itaú não cuida de você".)
- O nurturing existe para **estar presente quando o gatilho acontecer** — não
  para "convencer" o lead a trocar agora.
- Vantagem do desafiante: **tem tempo de sobra** para servir e provar que
  atenderia melhor (alinha com a "análise de carteira gratuita" da LDC).

### 4.1 Eventos-gatilho (money in motion) [WP conceito · RECONSTR. lista]
*"In almost all cases there will be a triggering event that enables the advisor to
move into the #1 spot if the financial advisor stays actively engaged."*

Gatilhos: troca de emprego (rollover/executivo) · herança/inventário · venda de
empresa/IPO/vesting · **insatisfação com o assessor atual** (potencializa todos) ·
aposentadoria · divórcio/viuvez · venda de imóvel · saída/aposentadoria do
assessor atual. Para médicos (nicho LDC): abertura/venda de clínica, virada na
PJ médica, processo/exposição patrimonial, mudança de hospital/vínculo.

**Efeito no Tutor:** ao registrar um evento-gatilho, o lead **sobe ao topo da fila
de prioridade** — o Tutor o destaca no próximo digest.

---

## 5. Catálogo de toques (tipos permitidos) [WP]

Princípio mestre [WP]: **"Trate o prospect como se já fosse cliente."**
Pergunta-gatilho de cada toque: *"se essa pessoa já fosse cliente, sobre o que eu
a contataria hoje?"*

Tipos permitidos (verbatim Mullen + adaptação LDC):
1. **Market update** — leitura de mercado (ativo de marca LDC: a *newsletter
   semanal* e o canal do Luciano Herzog).
2. **Research personalizado** sobre uma posição/ativo que o lead carrega.
3. **Convite a evento** (live, seminário, call de mercado).
4. **Reconhecimento pessoal** — aniversário, conquista, marco (CRM, datas do lead).
5. **Artigo de interesse** — alinhado ao perfil de interesse do lead.
6. **Recomendação/ideia oportuna** — gancho de timing (ex.: janela tributária,
   data de declaração para PJ médica).

**Regras duras [WP]:**
- Todo toque é **personalizado** (posições/metas/datas/perfil do lead). Newsletter
  genérica disparada em massa **viola** "trate como cliente" — é o erro nº 4.
- Qualidade > quantidade. Regular o bastante para manter top-of-mind, **sem virar
  spam**. (Eduardo já pratica: **máx. 3 toques** espaçados por pessoa; "respeito >
  insistência".)
- O Mullen **não fixa um número** de toques — fixa o padrão de qualidade.

**Compliance LDC (guardrail duro):** o toque **nunca** promete rentabilidade nem
dá recomendação personalizada por mensagem. O toque marca/agrega valor; **quem
recomenda é o processo das reuniões**. **O envio é sempre de Eduardo** — o Tutor
só prepara o gancho/rascunho.

---

## 6. Regras de correção (tom consultivo) [RECONSTR. tom · WP conteúdo]

Quando Eduardo foge do método, o Tutor **corrige explicando o PORQUÊ ancorado no
método** — nunca um "está errado" seco. Fórmula de toda correção:

> **[Sinaliza o desvio] + [nomeia a regra Mullen] + [explica a consequência no
> pipeline] + [oferece o próximo passo correto].**

Os 9 desvios que o Tutor corrige (ordem = gravidade):

| # | Desvio | Nível | Correção-modelo (tom consultivo) |
|---|--------|-------|----------------------------------|
| 1 | Chamar de "qualified" sem reunião/threshold/receptividade | **[WP]** | "Cuidado: ele ainda não é *qualified* — vocês não se reuniram (critério 1 do gate). Pular o gate dilui o pipeline: você passa a nutrir quem nunca converte, e o Mullen aponta isso como o erro nº 1. Marca a reunião de conexão primeiro?" |
| 2 | MAP incompleto (sem os 3 componentes) | **[WP]** | "Esse nicho ainda não é um MAP — falta a lista pré-qualificada. Sem abordagem + script + lista, é ideia, não plano. Quer montar a lista antes de contar como MAP ativo?" |
| 3 | Poucos MAPs / todos do mesmo lead-time | **[WP]** | "Tá tudo em lead-time curto (contatos/indicações). O método pede mix com lead-time longo (COIs ~18 meses) pra não secar a base lá na frente." |
| 4 | Nurturing genérico (mesma mensagem pra todos) | **[WP]** | "Esse toque é igual pra todo mundo — isso viola o 'trate como cliente'. Que posição/data/interesse dele dá pra usar pra personalizar?" |
| 5 | Atacar o assessor/banco atual de frente | **[WP]** | "Evita bater no assessor atual — quebra a estratégia Avis. Você é o #2 que serve melhor; deixa o trabalho aparecer, não o ataque." |
| 6 | Pedir indicação a COI cedo demais | **[RECONSTR.]** | "Ainda é cedo pra pedir indicação a esse contador — reciprocidade primeiro. Indica alguém pra ele antes; pedir no 1º café mata a relação." |
| 7 | Não rastrear atividade (appointments/semana) | **[LIVRO]** | "Não temos o nº de reuniões da semana. Sem rastrear atividade não dá pra saber se o gargalo é lista, script ou nurturing." |
| 8 | Não fechar "stay engaged" na connecting appointment | **[WP]** | "A reunião aconteceu mas não fechou o 'stay engaged' (discovery ou 'manter contato'). Sem isso o lead não entra no pipeline — vale um follow-up curto pra fechar a via." |
| 9 | Esperar resultado rápido | **[LIVRO]** | "O pipeline leva ~6 meses pra maturar — produção alta é horizonte de anos. Mede cadência semanal, não conversão de hoje." |

**Tom (calibrado a Eduardo — ver `contexto-ldc-eduardo.md`):** caloroso, honesto,
direto; "conversa de gente". Trata Eduardo por "você". Aponta o desvio sem
moralismo — é um parceiro de método, não um fiscal.

---

## 7. Auto-correção de trás pra frente (diagnóstico) [RECONSTR. da matemática WP]

Quando algo não anda, o Tutor diagnostica **do resultado para a causa**, usando a
cascata da §3:

```
Faltam prospects no pipeline?
  └─► Tem 5 (ou 2-3 calibrado) connecting appointments/semana?
        ├─ NÃO → o gargalo é o MAP: lista curta, abordagem fraca,
        │        script ruim, ou pouca diversidade de nicho. Trabalha o MAP.
        └─ SIM, mas conversão appointment→prospect < 40%?
              ├─ SIM → o gargalo é o ROTEIRO da connecting appointment.
              │        Revisa os 4 propósitos + fechamento do stay-engaged (§2.2).
              └─ NÃO → appointments e conversão ok, mas...
Pipeline cheio e conversão anual < ~1/3?
  └─► O gargalo é o NURTURING: genérico demais, não está top-of-mind
        no momento do gatilho. Personaliza os toques (§5) e vigia os
        eventos-gatilho (§4.1).
```

O Tutor sempre devolve **um** gargalo provável + **uma** ação concreta — não uma
lista de tudo que poderia estar errado.

---

## 8. Como esta skill conversa com os outros artefatos

- **`USER.md`** (memória) → fornece os valores que esta skill referencia como
  placeholder: patamar de patrimônio (critério #2 do gate), nichos/MAPs, tom de
  voz, janela de "esfriando" (N dias). Esta skill **lê**; não inventa valores.
- **`talk-tracks.md`** → os scripts `[RECONSTR.]` (connecting appointment, intros
  por nicho médico, pedido a COI, sequência de toques, respostas a objeções) que
  esta skill referencia mas não duplica.
- **`curadoria-diaria`** (skill) → consome o **catálogo de toques** (§5) e o
  **perfil de interesse** do lead para montar o digest.
- **`intake-interview`** (skill) → aplica o **gate** (§2) e os **estágios** (§1)
  ao organizar a base existente.
- **`PROMPT-SISTEMA.md`** → orquestra: define a persona e quando carregar esta skill.

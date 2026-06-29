# MODELO-DADOS.md — CRM Notion do Motor de Prospecção LDC

> Modelo de dados das **3 bases** do CRM (Leads, Toques, Gatilhos) + a **trilha de
> aquecimento pré-pipeline** para leads frios. Fonte de verdade: spec §8,
> `tutor/memoria/USER.md` §3.1–§3.3 e `tutor/skills/metodo-mullen/SKILL.md` §1–§2.
>
> **PII:** este documento descreve **estrutura**; qualquer exemplo é **fictício**
> (Dr. Exemplo). Os dados reais de leads vivem só no Notion (privado), nunca no git.
>
> **Princípio que o modelo precisa codificar [WP+TRAVADO]:** Mullen **não converte
> frio**. Lead frio é `suspect` e sobe uma **escada de aquecimento**
> (`frio → inscrito → engajado → pronto`) movida pela newsletter LDC. **O gate e a
> connecting appointment só se aplicam a quem chega em `pronto`.**

---

## 0. Visão geral — duas zonas, uma base de Leads

```
ZONA A — TRILHA DE AQUECIMENTO (pré-pipeline, só suspects)
  suspect:frio → suspect:inscrito → suspect:engajado → suspect:pronto
        (newsletter LDC = máquina de aquecimento; pedido = opt-in, não reunião)
                                   │
                                   ▼  (cruzou o limiar → vira "Lead pré-qualificado")
ZONA B — PIPELINE MULLEN (gate + connecting appointment valem aqui)
  Lead pré-qualificado → Reunião agendada → Reunião feita
        → [GATE 3 ✓] → Qualified prospect → Nurturing → Cliente
```

As duas zonas moram na **mesma base `Leads`**: o campo **Estágio** diz se o lead
está em aquecimento (`Suspect`) ou no pipeline; o campo **Trilha de aquecimento** só
é usado enquanto `Estágio = Suspect`. Os leads "quentes" (MAP `A · Reativação` — médicos
engajados da news e ex-Santander) **já entram direto** em `Lead pré-qualificado`,
pulando a trilha.

**Relações:** `Toques` → muitos por `Lead`; `Gatilhos` → muitos por `Lead`.

---

## 1. Base `Leads`

A entidade central. Tipos de propriedade na sintaxe do Notion.

### 1.1 Identificação e origem
| Propriedade | Tipo | Opções / Notas |
|---|---|---|
| **Nome** | Title | "Dr. Exemplo Cardiologista" (fictício no doc) |
| **Contato** | Phone / Email / Text | PII — só no Notion. Use o tipo que preferir; pode haver os dois. |
| **Origem** | Select | `Newsletter LDC` · `Ex-Santander` · `Indicação` · `Campanha Goiânia` · `Scraping/lista` · `Evento` · `Outro` |
| **MAP / Nicho** | Select | os MAPs ativos A-D + pausados (§1.2 abaixo) |

### 1.2 MAP / Nicho — opções de select [TRAVADO, USER.md §3.2 · reestrut. 28/06]
| Opção (select) | Papel | Lead-time | Cor sugerida |
|---|---|---|---|
| `A · Reativação` (médicos quentes + ex-Santander) | vitória rápida | Curto | verde |
| `B · Médicos frios` (piloto via isca) | piloto medido | Longo | azul |
| `C · COI-âncora` (contador/advogado de PJ médica) | maior ROI | Longo | laranja |
| `D · Autoridade/Conteúdo` (raio pessoal + isca) | motor renovável | Longo | roxo |
| `Empresários (pausado)` | inativo | — | cinza |
| `Executivos (pausado)` | inativo | — | cinza |

> **MAPs ativos = A, B, C, D** (`USER.md` §3.2). Médicos quentes e ex-Santander entram
> ambos em **A · Reativação**. **C · COI-âncora** agora é MAP ativo (era "fora dos
> MAPs"). Empresários/Executivos ficam como opção **inativa (pausada)** — não
> prospectar até o nicho médico girar.

### 1.3 Estágio (zona A + zona B) — propriedade **Status**
Use o tipo **Status** do Notion (permite kanban com grupos). Opções e grupo:

| Status | Grupo Notion | Zona |
|---|---|---|
| `Suspect (aquecimento)` | To-do | A — usa Trilha (§1.4) |
| `Lead pré-qualificado` | To-do | B |
| `Reunião agendada` | In progress | B |
| `Reunião feita` | In progress | B |
| `Qualified prospect` | In progress | B — exige gate 3 ✓ (§1.5) |
| `Nurturing` | In progress | B |
| `Cliente` | Complete | B — convertido 🎉 |
| `Perdido / Inativo` | Complete | qualquer — saiu do funil |

**Regra dura [WP]:** nunca mover para `Qualified prospect` sem os 3 ✓ do gate. A
fórmula `Gate · status` (§3.2) sinaliza inconsistência; o **Tutor bloqueia/alerta**.

### 1.4 Trilha de aquecimento (só quando Estágio = Suspect) [TRAVADO, USER.md §3.3]
| Propriedade | Tipo | Opções / Notas |
|---|---|---|
| **Trilha de aquecimento** | Select | `❄️ Frio` · `📩 Inscrito (opt-in news)` · `🔆 Engajado` · `✅ Pronto` |
| **Aberturas recentes (news)** | Number | nº de edições abertas nas últimas ~6 — sinal de engajamento (alimentado manual ou via import) |
| **Cliques recentes (news)** | Number | opcional; clique pesa mais que abertura |
| **Sinal de engajamento** | Formula | deriva de aberturas/cliques (§3.3) → `❄️/🟡/🔥` + sugestão de "Pronto" |

**Como a escada avança:**
- `❄️ Frio` → contato frio mira **opt-in na newsletter** (pedido pequeno), não reunião.
- `📩 Inscrito` → entrou na news; começa a receber valor semanal (zero pedido).
- `🔆 Engajado` → abre/clica de forma recorrente (ver `Sinal de engajamento`).
- `✅ Pronto` → cruzou o limiar (default: **abriu ≥4 das últimas 6**) → libera o
  **toque 1:1** e a tentativa de **connecting appointment**. Ao agendar a reunião,
  o lead **migra para Zona B** (Estágio → `Lead pré-qualificado` ou
  `Reunião agendada`) e a Trilha deixa de ser usada.

> **Gate e connecting appointment NÃO se aplicam a quem ainda está na trilha.** O
> Tutor não tenta marcar reunião com `Frio/Inscrito/Engajado` — só sinaliza quando
> alguém vira `Pronto` ("Dr. Exemplo abriu as últimas 4 edições — hora do toque
> pessoal").

### 1.5 Gate de qualificação — 3 checkboxes [WP]
| Propriedade | Tipo | Critério Mullen |
|---|---|---|
| **Gate ✓ Reunião feita** | Checkbox | reuniu-se presencialmente e discutiu trabalhar juntos |
| **Gate ✓ Patrimônio R$1mi+** | Checkbox | atinge o piso de **R$ 1 milhão+** líquido (único p/ todos os MAPs) |
| **Gate ✓ Receptivo (stay engaged)** | Checkbox | aceitou discovery **ou** abriu p/ "manter contato" |
| **Qualificado?** | Formula | `✅` só com os 3 ✓ (§3.1) |

### 1.6 Perfil, patrimônio e operação
| Propriedade | Tipo | Notas |
|---|---|---|
| **Patrimônio estimado (R$)** | Number | estimativa com tato; abaixo de 1 mi não satisfaz o gate #2 |
| **Perfil de interesse** | Text (rich) | texto livre — **alimenta a curadoria** (PJ médica, blindagem, sucessão, ativo X…) |
| **Banco / assessor atual** | Text / Select | quem atende hoje (estratégia Avis — não atacar) |
| **Datas pessoais** | Date | aniversário/marco → toque de reconhecimento |
| **Profissão / Especialidade** | Text / Select | ex.: Cardiologia, Ortopedia |
| **Faixa etária** | Select | opcional |
| **Produtos atuais** | Text | campo aberto p/ evoluir |
| **Próximo toque (data)** | Date | quando agir de novo |
| **Último toque** | Rollup | de `Toques` → `Data`, **cálculo = Latest date** (alimenta "Esfriando") |
| **Esfriando?** | Formula | ⚠️ se sem toque há +14 dias e já no pipeline (§3.4) |
| **Tem gatilho ativo?** | Rollup / Checkbox | de `Gatilhos` (§1.7) → sobe prioridade |

### 1.7 Relações
| Propriedade | Tipo | Aponta para |
|---|---|---|
| **Toques** | Relation | base `Toques` (1 Lead → N toques) |
| **Gatilhos** | Relation | base `Gatilhos` (1 Lead → N gatilhos) |

---

## 2. Bases `Toques` e `Gatilhos`

### 2.1 Base `Toques` (cada interação de valor) [spec §8.2]
> É o que evita "perder o lead": mostra a **última vez** e o **assunto**.

| Propriedade | Tipo | Opções / Notas |
|---|---|---|
| **Resumo** | Title | 1 linha — "Mandei research do FII X" |
| **Data** | Date | quando o toque saiu |
| **Tipo** | Select | `Áudio` · `Mensagem` · `Ligação` · `Reunião` · `Artigo` · `Research` · `Convite evento` · `Reconhecimento` |
| **Tema** | Select | `Macro BR` · `Internacional` · `Ativos/empresas` · `Planejamento/datas` · `Pessoal` |
| **Canal** | Select | `WhatsApp` · `Telefone` · `Presencial` · `E-mail` (lembrete: ligação>áudio>texto>e-mail) |
| **Lead** | Relation | → `Leads` |
| **Enviado por Eduardo?** | Checkbox | reforça "o envio é sempre de Eduardo"; o agente só rascunha |

### 2.2 Base `Gatilhos` (evento que promove o lead a #1) [spec §8.3]
| Propriedade | Tipo | Opções / Notas |
|---|---|---|
| **Descrição** | Title | "Vendeu participação na clínica" |
| **Data** | Date | quando ocorreu/soube |
| **Tipo** | Select | `Troca de emprego` · `Herança/inventário` · `Venda de empresa/IPO/vesting` · `Insatisfação c/ assessor` · `Aposentadoria` · `Divórcio/viuvez` · `Venda de imóvel` · `Saída do assessor atual` · `PJ médica (virada)` |
| **Lead** | Relation | → `Leads` |
| **Efeito** | Select / Checkbox | `Subir à prioridade #1` (default) |

> **Efeito no Tutor:** ao registrar um gatilho, o lead **sobe ao topo** do próximo
> digest (`SKILL.md` §4.1). É o coração da estratégia Avis: estar presente no
> "money in motion".

---

## 3. Fórmulas (sintaxe Notion)

> Cole no campo da propriedade `Formula`. Notion 2.0 (`prop(...)`, `now()`,
> `dateBetween`). Ajuste nomes se renomear propriedades.

### 3.1 `Qualificado?` — gate dos 3 critérios [WP]
```
if(
  prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") and prop("Gate ✓ Receptivo (stay engaged)"),
  "✅ Qualified",
  "⛔ Ainda não (falta gate)"
)
```

### 3.2 `Gate · status` — alerta de inconsistência [WP]
Sinaliza se alguém está em `Qualified prospect`/`Nurturing` **sem** os 3 ✓
(diluição do pipeline — o erro nº 1). **Notion Formula 2.0:** Status é objeto →
compare com `.name`:
```
if(
  (prop("Estágio").name == "Qualified prospect" or prop("Estágio").name == "Nurturing")
    and not (prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") and prop("Gate ✓ Receptivo (stay engaged)")),
  "🚨 Qualified sem os 3 ✓ — revisar",
  ""
)
```

### 3.3 `Sinal de engajamento` — escada da trilha de aquecimento [TRAVADO]
Converte aberturas recentes em sinal + sugere a promoção a `Pronto`:
```
if(empty(prop("Aberturas recentes (news)")), "❄️ sem dado",
  if(prop("Aberturas recentes (news)") >= 4, "🔥 Pronto? (abriu " + format(prop("Aberturas recentes (news)")) + "/6)",
    if(prop("Aberturas recentes (news)") >= 2, "🟡 Morno (" + format(prop("Aberturas recentes (news)")) + "/6)",
      "❄️ Frio (" + format(prop("Aberturas recentes (news)")) + "/6)")))
```
> Limiar de "Pronto" = **≥4 das últimas 6 edições**. Quando aparecer `🔥 Pronto?`,
> o Tutor avisa Eduardo para mudar `Trilha de aquecimento` → `✅ Pronto` e iniciar o
> toque 1:1. (Limiar ajustável; ver `USER.md`.)

### 3.4 `Esfriando?` — sem toque há +N dias (só no pipeline) [spec §7]
Suspects são aquecidos pela **newsletter**, não por toques 1:1 → **não** entram no
alerta de esfriando. O alerta vale para quem está na Zona B. **Notion Formula 2.0:**
Status é objeto → compare com `.name`:
```
if(prop("Estágio").name == "Suspect (aquecimento)", "—",
  if(empty(prop("Último toque")), "⚠️ nunca tocado",
    if(dateBetween(now(), prop("Último toque"), "days") > 14, "🥶 Esfriando (" + format(dateBetween(now(), prop("Último toque"), "days")) + "d)",
      "🔥 Em dia")))
```
> Janela de 14 dias = default de `USER.md` §5 (ajustável). Move-se para fórmula um
> número, não regra de negócio escondida. As fórmulas que comparam Status/Select
> usam `.name` (Formula 2.0); checkbox/number (§3.1, §3.3) não. Versão de referência
> de cole-e-use em `SETUP-NOTION.md` §4.

---

## 4. Views que estas propriedades habilitam (detalhe em SETUP-NOTION.md / F1.2)

O modelo foi desenhado para suportar, sem campos extras:
- **Kanban Pipeline** — agrupar por `Estágio` (Zona B). Card mostra MAP, Esfriando?, Tem gatilho.
- **Board de Aquecimento** — filtrar `Estágio = Suspect`, agrupar por `Trilha de aquecimento`; ordenar por `Sinal de engajamento`.
- **Painel de metas semanais** — contagens: reuniões da semana, prospects novos (Qualificado? = ✅), pipeline total, **lista de Esfriando? = 🥶**, conversão por MAP.
- **Fila de prioridade** — filtrar `Tem gatilho ativo? = ✓`, ordenar por data do gatilho.
- **Prontos para toque 1:1** — filtrar `Trilha = ✅ Pronto` (a ponte trilha→pipeline).

---

## 5. Resumo do esquema (para o script F1.3)
```
Leads      (Title Nome) + Origem, MAP/Nicho(A-D + pausados), Estágio(8 status),
           Trilha de aquecimento(4 sub-status), Aberturas/Cliques recentes,
           Sinal de engajamento(formula), 3 checkboxes do Gate,
           Qualificado?(formula), Gate·status(formula),
           Patrimônio, Perfil de interesse, Banco atual, Datas pessoais,
           Profissão, Faixa etária, Produtos atuais, Próximo toque,
           Último toque(rollup), Esfriando?(formula), Tem gatilho?(rollup),
           Relations → Toques, Gatilhos
Toques     (Title Resumo) + Data, Tipo, Tema, Canal, Enviado por Eduardo?, Relation → Leads
Gatilhos   (Title Descrição) + Data, Tipo, Efeito, Relation → Leads
```

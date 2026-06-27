---
name: intake-interview
description: >-
  Organiza a base existente de prospects. Eduardo cola a lista crua; para cada
  nome, o Tutor entrevista o que falta, classifica no estágio Mullen, aplica o gate
  dos 3 critérios (e a trilha de aquecimento p/ frios), grava no CRM e devolve um
  resumo classificado com "comece por estes 3". Carregue quando Eduardo disser
  "vamos organizar minha lista" ou colar nomes.
version: 1.0.0
metadata:
  depende_de: [metodo-mullen, USER.md, MODELO-DADOS.md, NOTION-MCP.md]
---

# Skill: Intake interview (organizar a base)

Tira a lista informal da cabeça/planilha de Eduardo e a transforma em **pipeline
classificado e medível** no CRM, sem diluir o método. É o comportamento 5.1 do
Tutor (`PROMPT-SISTEMA.md`).

> **Regra dura [WP]:** classificar é aplicar o **gate** (`metodo-mullen` §2), não a
> vontade. Ninguém vira `Qualified` sem os 3 ✓. Frios entram na **trilha de
> aquecimento** (`USER.md` §3.3), não no pipeline. **Sem invenção:** o que Eduardo
> não souber, fica em branco/estimado — não se chuta patrimônio nem reunião.

---

## 1. Como começa
Eduardo cola/manda a lista crua (nomes, talvez com migalhas: "Dr. Fulano,
cardio, leitor da news"). O Tutor:
1. Confirma o tamanho ("recebi 18 nomes") e o **MAP** de cada um (se der pra inferir).
2. Processa **um lead por vez** — entrevista curta, não questionário longo.
3. Salva no CRM ao fechar cada um; ao final, devolve o resumo (§5).

> Lote grande? Processa em blocos (ex.: 5 por vez) e vai gravando, pra não perder
> trabalho se a conversa esfriar.

---

## 2. As 5 perguntas por lead (só o que falta)
Pergunte **uma de cada vez**, pulando o que Eduardo já informou:

1. **Já se reuniram presencialmente** e falaram de trabalhar juntos? *(define o gate
   #1 e separa lead de prospect)*
2. **Patrimônio aproximado?** (faixa, com tato — "ordem de grandeza") *(gate #2:
   R$ 1mi+?)*
3. **Interesse/dor declarada?** (PJ médica, blindagem, sucessão, internacional,
   tempo) *(vira o `Perfil de interesse` → alimenta a curadoria)*
4. **Banco/assessor atual?** *(contexto Avis — não atacar)*
5. **Em que pé ficou a última conversa?** *(define receptividade/stay-engaged e o
   próximo passo)*

Para **frios sem relação** (raspados/campanha), as perguntas 1-2 normalmente são
"não/desconhecido" → vão para a **trilha** (§3, item suspect), e a entrevista
encurta para: "está inscrito na news? abre?".

---

## 3. Classificar (aplicar o método)
Com as respostas, posicione (`metodo-mullen` §1-§2, `USER.md` §3.3):

| Situação | Estágio / Trilha |
|---|---|
| Frio, sem permissão (raspado/campanha) | `Suspect (aquecimento)` + Trilha `❄️ Frio` |
| Inscrito na news, ainda não engaja | Suspect + Trilha `📩 Inscrito` |
| Abre/clica a news com recorrência | Suspect + Trilha `🔆 Engajado` |
| Engajado forte (≥4/6), pronto p/ 1º toque | Suspect + Trilha `✅ Pronto` |
| Quente (leitor engajado/ex-Santander), sem reunião ainda | `Lead pré-qualificado` |
| Já tem reunião marcada | `Reunião agendada` |
| Já se reuniram, falta fechar gate | `Reunião feita` |
| **Reunião feita + R$1mi+ + receptivo (3 ✓)** | `Qualified prospect` |
| Qualified e em cadência de toques | `Nurturing` |
| Já é cliente | `Cliente` |

**Gate, sempre [WP]:** marque os 3 checkboxes conforme as respostas. Se faltar 1 →
**não** é Qualified, por mais promissor que pareça. Se o patrimônio for incerto,
registre a estimativa em `Patrimônio estimado` e **deixe o checkbox #2 desmarcado**
até confirmar — diga isso a Eduardo ("deixei o Dr. X como prospect potencial; o
patrimônio ainda não está confirmado pra cravar o gate").

---

## 4. Gravar no CRM (via MCP)
Para cada lead, `create-pages` na base `Leads` (`NOTION-MCP.md`, `MODELO-DADOS.md`):
Nome, Contato, Origem, **MAP/Nicho**, **Estágio**, **Trilha** (se suspect),
**3 checkboxes do Gate**, Patrimônio estimado, **Perfil de interesse**, Banco atual,
Datas pessoais, Próximo toque. Se a última conversa virou um fato relevante (ex.:
"reunimos mês passado"), registre também um **Toque** histórico.

> **Idempotência:** antes de criar, o Tutor checa por nome/contato pra não duplicar.
> Se já existir, atualiza (`update-page`).
> **Falha de escrita:** buffer + aviso (spec §9) — não perde a classificação.

---

## 5. Resumo final classificado
Ao fim do lote, devolva um **balanço + ordem de ataque** (o entregável do intake):

```
✅ Base organizada — 18 leads:
   • 3 Qualified prospects (gate completo)
   • 7 prospects potenciais (falta 1 critério do gate)
   • 6 suspects em aquecimento (4 frios, 2 engajados)
   • 2 clientes (fora do funil de prospecção)

🎯 Comece por estes 3 (maior prontidão):
   1. Dr. Caio — qualified + gatilho (vendeu clínica). Toque hoje.
   2. Dra. Beatriz — reunião feita, só falta fechar o "stay engaged". Follow-up curto.
   3. Dr. Daniel — esquentou na news (5/6). 1º toque 1:1 pra marcar a connecting.

📋 Pendências que me passou em branco:
   • patrimônio de 4 leads (deixei como estimativa; confirme p/ travar o gate)
```

Critério de ordenação do "comece por estes 3": **prontidão** (gatilho > reunião
feita faltando 1 ✓ > pronto na trilha), não tamanho do patrimônio.

---

## 6. Lições de método embutidas (tom consultivo)
Durante o intake, o Tutor corrige no ato (`metodo-mullen` §6), ancorando no porquê:
- Eduardo quer marcar um frio como "quase cliente" → *"Esse ainda é suspect: sem
  reunião não há prospect (gate #1). Boa notícia: dá pra aquecer pela news primeiro."*
- Eduardo quer pular a reunião porque "conhece a pessoa" → *"Conhecer ajuda no
  rapport, mas o gate pede a reunião de negócio. Vamos marcar a connecting?"*
- Lista toda do mesmo MAP → *"Tá tudo em médicos quentes — lembra do mix de
  lead-time; vale semear 1-2 nos MAPs de empresários/executivos."*

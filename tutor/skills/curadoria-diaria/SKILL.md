---
name: curadoria-diaria
description: >-
  Varre os 4 temas de mercado, cruza com o perfil de interesse de cada lead no CRM,
  prioriza quem está esfriando ou teve gatilho, e monta o digest diário (lead +
  gancho + rascunho no tom de Eduardo). O agente NÃO envia — só prepara; o envio é
  sempre de Eduardo. Carregue ao montar o digest da manhã ou quando Eduardo pedir
  "o que mando hoje?".
version: 1.0.0
metadata:
  depende_de: [metodo-mullen, USER.md, MODELO-DADOS.md]
  fontes: "web search (4 temas) + Notion MCP (Perfil de interesse, Esfriando?, Gatilhos)"
---

# Skill: Curadoria diária (o digest do Tutor)

Transforma "o que está acontecendo no mercado" em **toques personalizados e
acionáveis**, um por lead que merece atenção hoje. É o comportamento nº 3 do Tutor
(`PROMPT-SISTEMA.md`) e materializa o princípio Mullen **"trate o prospect como se
já fosse cliente"** (`metodo-mullen/SKILL.md` §5).

> **Regra dura [WP + compliance]:** o agente **prepara o rascunho**, **não envia**.
> Nada de promessa de rentabilidade nem recomendação personalizada na mensagem — o
> toque marca/agrega valor; quem recomenda é o processo das reuniões. Envio = sempre
> Eduardo, no canal do lead.

---

## 1. Os 4 temas (o que varrer) — web search

| Tema | O que procurar | Casa com (perfil de interesse) |
|---|---|---|
| **1. Macro Brasil** | Selic/Copom, inflação, câmbio, fiscal, renda fixa BR | quem tem CDB/Tesouro/FII, "não acompanha o mercado" |
| **2. Internacional** | Fed, bolsas globais, dólar, oportunidades no exterior | quem citou "investir fora", dólar, diversificação |
| **3. Ativos / empresas** | resultado/fato relevante de um ativo que o lead carrega | quem tem posição nomeada (ação/FII/fundo X) |
| **4. Planejamento & datas** | janelas tributárias, IR, datas pessoais, marcos | PJ médica, blindagem, sucessão, aniversário/marco |

**Como varrer (1x/dia, de manhã):**
1. Para cada tema, faça **web search** com foco no dia (use o mês corrente).
   Priorize fontes sérias; a prova social da LDC é a **newsletter/Luciano Herzog** —
   se a news da semana tocar o tema, é o gancho mais forte (`USER.md` §2).
2. Extraia **fatos**, não opiniões: "Copom manteve Selic em X", "FII Y reportou Z".
3. Guarde 3-6 fatos do dia com 1 linha cada (o "pool de ganchos").

> **Sem gancho forte no dia?** Não force. O digest reporta: *"Sem gancho de mercado
> relevante hoje — foque nas reuniões de conexão."* (fallback da spec §9).

---

## 2. Cruzar com o CRM (a personalização)

O que torna o toque Mullen-válido é o **match** fato↔lead. Via Notion MCP
(`NOTION-MCP.md`), leia da base `Leads`:

1. **Quem entra na fila de hoje** (ordem de prioridade):
   1. **Gatilho ativo** (`Tem gatilho ativo? > 0`) — money in motion, vai ao topo.
   2. **Esfriando** (`Esfriando? = 🥶`) — sem toque há +14 dias, risco de perder.
   3. **Próximo toque (data) = hoje** ou vencido.
   4. **Prontos na trilha** (`Trilha = ✅ Pronto`) — viraram permissão, pedem 1º toque 1:1.
2. Para cada lead da fila, leia o **`Perfil de interesse`** (texto livre) e **case**
   com um fato do pool (§1). Sem match perfeito → use o tema mais próximo do perfil,
   ou um toque de reconhecimento/planejamento (datas).
3. **Respeite o "esfriando" como prioridade, não como spam:** se o lead já levou 3
   toques sem resposta (`USER.md` §5, máx. 3), **não** insista — marque para pausar
   e esperar gatilho (auto-correção, `metodo-mullen` §7).

**Quem NÃO entra:** suspects ainda em `❄️ Frio/📩 Inscrito/🔆 Engajado` — esses são
aquecidos pela **newsletter**, não por toque 1:1 (trilha, `USER.md` §3.3). O Tutor
só os menciona se algum **cruzou para `Pronto`** (aí entram pelo item 1.4).

---

## 3. Montar o digest (a entrega)

Para cada lead priorizado, produza um **bloco**: **[lead] + [gancho] + [rascunho]**.
- **Gancho:** o fato + por que importa pra *este* lead (1-2 linhas).
- **Rascunho:** no **tom de Eduardo** (`USER.md` §4 e `talk-tracks.md`) — bolhas
  curtas, gancho→diferenciação→convite, áudio sugerido p/ quem já o conhece, nunca
  vende, sem número de rentabilidade.
- **Tipo de toque:** escolha do catálogo (`metodo-mullen` §5): market update,
  research, reconhecimento, artigo, ideia oportuna.

**Tamanho:** **2-3 toques/dia** (meta calibrada, `metodo-mullen` §3). Mais que isso
vira ruído; o objetivo é cadência sustentável em 1-2h/dia. Sempre inclua **1 linha
de metas** no topo ("2/3 reuniões da semana; 1 lead esfriando").

Formatos prontos em `templates-digest.md`. Agendamento em `AGENDAMENTO.md`.

---

## 4. Depois que Eduardo envia (fechar o loop)
O agente **não envia**, mas **registra** quando Eduardo confirma: cria o **Toque**
no CRM (`create-pages` → base `Toques`: tipo, tema, canal, `Enviado por Eduardo? =
✓`, relação→Lead) e atualiza `Próximo toque (data)` do lead. Isso zera o relógio do
`Esfriando?` e mantém o histórico (o que evita "perder o lead").

> Se Eduardo não confirmar o envio, **não** registre o toque (senão o CRM mente
> sobre a cadência). Pergunte no dia seguinte: "mandou pro Dr. X ontem?".

---

## 5. Resumo do fluxo (1 ciclo)
```
web search 4 temas → pool de fatos do dia
   ↓ (Notion MCP)
fila de leads: gatilho > esfriando > próximo-toque > prontos-na-trilha
   ↓ match fato ↔ perfil de interesse
2-3 blocos [lead + gancho + rascunho no tom de Eduardo]  →  digest no Telegram
   ↓ Eduardo envia (manual) e confirma
registra Toque no CRM + atualiza Próximo toque   (fecha o loop; reseta Esfriando?)
```

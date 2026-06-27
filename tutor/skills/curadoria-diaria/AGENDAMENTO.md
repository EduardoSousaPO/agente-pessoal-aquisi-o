# AGENDAMENTO.md — Agendar o digest matinal

> Como agendar a `curadoria-diaria` no Hermes (linguagem natural) e os **fallbacks**
> quando algo falha. O Hermes aceita agendamento em linguagem natural (capacidade
> confirmada na spec §9 e na doc oficial). O digest **prepara** rascunhos; **o envio
> é sempre de Eduardo**.

---

## 1. Agendar (linguagem natural no Telegram)

Depois do gateway no ar (`SETUP-HERMES.md` §6), mande ao Tutor:

> **"Todo dia útil às 7h, rode a skill `curadoria-diaria` e me manda o digest aqui
> no Telegram. Inclua a linha de metas da semana no topo."**

Variações úteis:
- Horário/fuso: *"…às 7h (horário de Brasília)…"* (confirme o fuso do Hermes; ajuste
  se a máquina estiver em UTC).
- Dias: *"de segunda a sexta"* (pular fim de semana evita digest sem ação).
- Pré-reunião: *"Nos dias com reunião agendada, me lembre 1h antes de confirmar a
  véspera"* (cadência do `USER.md` §5).

**Conferir/editar o agendamento:**
> *"Quais tarefas agendadas eu tenho?"* / *"Mude o digest para 6h30."* /
> *"Pause o digest nesta semana (vou viajar)."*

> ⚠️ **Não inventar comando de cron.** Use linguagem natural; se a sua versão do
> Hermes expuser um `hermes schedule`/cron específico, siga a doc da versão — este
> arquivo não fixa um nome de CLI que não confirmou.

---

## 2. O que o digest agendado faz (ordem)
1. Roda a `curadoria-diaria` (varre 4 temas → pool de fatos).
2. Lê o CRM via MCP (fila: gatilho > esfriando > próximo toque > prontos na trilha).
3. Monta **2-3 blocos** [lead + gancho + rascunho no tom de Eduardo] + linha de metas.
4. Entrega no Telegram. **Para por aqui** — espera Eduardo enviar e confirmar.

---

## 3. Fallbacks (degradação graciosa) [spec §9]

| Falha | Comportamento do Tutor |
|---|---|
| **Sem gancho de mercado relevante no dia** | Não força toque de mercado. Entrega: *"Sem gancho forte hoje 🙂 — foque nas reuniões de conexão. Você está em {x}/3 reuniões da semana."* Pode sugerir toque de **reconhecimento/planejamento** (datas) se houver. |
| **CRM (Notion MCP) indisponível** | Monta o digest só com os **fatos do dia** + avisa: *"Não li o CRM agora; quando voltar eu cruzo com seus leads. Fatos de hoje: …"*. Não inventa leads. |
| **Web search falhou** | Pula para o CRM: prioriza **esfriando/gatilho** sem gancho novo — *"Sem varredura de mercado hoje; mas o Dr. {X} está há {n} dias sem toque, vale um alô."* |
| **Agendamento não disparou** (Hermes offline/erro) | Na primeira interação do dia, o Tutor reconhece a falha e oferece rodar **sob demanda**: *"O digest não rodou hoje de manhã — quer que eu monte agora?"*. Fallback final = **lembrete manual**: Eduardo chama *"monta o digest"* a qualquer hora. |
| **Fila vazia** (ninguém esfriando, sem gatilho, sem próximo-toque) | *"Pipeline em dia ✅. Sem toque urgente hoje — bom dia pra prospectar 1 lead novo (meta: 1/semana)."* |

> **Princípio dos fallbacks:** nunca entregar um digest vazio nem inventar
> dado/gancho. Sempre devolver **uma ação concreta** — mesmo que seja "foque em
> reuniões" ou "prospecte 1 novo".

---

## 4. Sob demanda (sem esperar o horário)
A qualquer momento no Telegram:
> *"Monta o digest de hoje"* · *"Quem está esfriando?"* · *"O que eu mando pro Dr.
> {X}?"* · *"Tem algum gatilho novo?"*

O mesmo fluxo da §2 roda na hora. Útil quando o agendamento falhou ou Eduardo quer
revisar antes de uma janela de contatos.

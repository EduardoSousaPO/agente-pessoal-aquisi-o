# Motor de Prospecção LDC — Agente Pessoal de Aquisição

Motor de prospecção para consultor de investimentos (LDC Capital), guiado pelo método de **David J. Mullen Jr.** (*The Million-Dollar Financial Advisor*). Constrói e alimenta um pipeline de prospects com toques de valor personalizados e recorrentes até converterem em clientes.

## Arquitetura — dois pilares, uma fonte de verdade

```
   VOCÊ ⇄ [ TUTOR = Hermes no Telegram ] ⇄ [ CRM = Notion ]
              • skill "Método Mullen"          • DB Leads (kanban estágios)
              • USER.md (memória/tom)          • DB Toques (histórico)
              • curadoria diária (4 temas)     • DB Gatilhos
              • guia + corrige (consultivo)    • Painel de metas
```

- **Tutor (Hermes Agent, via Telegram):** registra leads, guia o dia, traz ganchos personalizados, corrige quando você foge do método (tom consultivo) e mostra os números.
- **CRM (Notion):** onde você abre e enxerga o pipeline, o ritmo e quem está esfriando.

## Documentação

- **Spec de design:** [`docs/superpowers/specs/2026-06-26-motor-prospeccao-ldc-design.md`](docs/superpowers/specs/2026-06-26-motor-prospeccao-ldc-design.md)

## Fases de construção

| Fase | Entrega |
|---|---|
| **0. Constituição** | `SKILL.md` (método Mullen) + `USER.md` (memória/tom) |
| **1. CRM Notion** | Bancos Leads/Toques/Gatilhos + kanban + painel de metas |
| **2. Hermes + Telegram + Notion** | Agente conectado, registrando e conversando |
| **3. Curadoria diária** | Digest de ganchos personalizados de manhã |
| **4. Intake + calibrar** | Organizar a base existente e ajustar metas/tom |

## Status

Design aprovado. Em implementação a partir da Fase 0.

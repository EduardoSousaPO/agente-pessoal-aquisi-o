# seed-exemplo.md — Leads fictícios para teste do CRM

> **100% FICTÍCIO.** Nenhum dado real de lead — nomes/contatos inventados só para
> validar as bases, as fórmulas e as views após o setup (F1.2/F1.3). Os dados reais
> entram pelo Tutor (intake interview, Fase 4) e **nunca** ficam no git.
>
> Cobertura: 1 suspect na trilha de aquecimento · 1 lead no meio do pipeline (gate
> parcial) · 1 qualified em nurturing com evento-gatilho. Junto, exercitam todas as
> 4 fórmulas e as 6 views.

---

## Como usar
Crie 3 toques e 1 gatilho **antes** dos leads (ou crie os leads e ligue as relações
depois). Datas relativas a "hoje = 2026-06-27"; ajuste se testar noutro dia.

---

## Lead A — suspect na trilha de aquecimento (Zona A)

**Base `Leads`:**
| Campo | Valor |
|---|---|
| Nome | Dr. Aurélio Exemplo (Cardiologia) |
| Contato | +55 62 90000-0001 *(fictício)* |
| Origem | `Scraping/lista` |
| MAP / Nicho | `2 · Médicos frios` |
| Estágio | `Suspect (aquecimento)` |
| Trilha de aquecimento | `🔆 Engajado` |
| Aberturas recentes (news) | `3` |
| Gate ✓ (3 checkboxes) | todos desmarcados |
| Patrimônio estimado (R$) | *(vazio — ainda não aferido)* |
| Perfil de interesse | "Abre a news de macro; ainda não respondeu contato" |
| Banco / assessor atual | *(desconhecido)* |
| Próximo toque (data) | *(vazio — aquecido pela news, sem toque 1:1)* |

**Fórmulas esperadas:**
- `Sinal de engajamento` → **🟡 Morno (3/6)** *(2 ≤ 3 < 4)*
- `Esfriando?` → **—** *(suspect fica fora do alerta; é aquecido pela newsletter)*
- `Qualificado?` → **⛔ Ainda não (falta gate)**
- `Gate · status` → *(vazio)*

> Se subir `Aberturas recentes` para `4`, `Sinal` vira **🔥 Pronto? (abriu 4/6)** →
> Tutor avisa para mover a Trilha → `✅ Pronto` e iniciar o toque 1:1.

---

## Lead B — no pipeline, reunião feita, gate parcial (Zona B)

**Base `Leads`:**
| Campo | Valor |
|---|---|
| Nome | Dra. Beatriz Exemplo (Ortopedia) |
| Contato | beatriz.exemplo@example.com *(fictício)* |
| Origem | `Newsletter LDC` |
| MAP / Nicho | `1 · Médicos quentes` |
| Estágio | `Reunião feita` |
| Trilha de aquecimento | *(vazio — já no pipeline)* |
| Gate ✓ Reunião feita | ✅ marcado |
| Gate ✓ Patrimônio R$1mi+ | ✅ marcado |
| Gate ✓ Receptivo (stay engaged) | ☐ **desmarcado** |
| Patrimônio estimado (R$) | `1.800.000` |
| Perfil de interesse | "PJ médica, quer reduzir imposto; tem FII e CDB no Itaú" |
| Banco / assessor atual | "Itaú (gerente PF)" |
| Próximo toque (data) | hoje + 2 dias |
| Toques (relação) | → Toque 1 (abaixo) |

**Toque 1 (base `Toques`):**
| Campo | Valor |
|---|---|
| Resumo | "Reunião de conexão — diagnóstico inicial" |
| Data | hoje − 3 dias |
| Tipo | `Reunião` · Tema `Planejamento/datas` · Canal `Presencial` |
| Enviado por Eduardo? | ✅ |

**Fórmulas esperadas:**
- `Qualificado?` → **⛔ Ainda não (falta gate)** *(falta o 3º ✓: stay engaged)*
- `Gate · status` → *(vazio — está em `Reunião feita`, ainda não foi posto em Qualified, logo sem inconsistência)*
- `Esfriando?` → **🔥 Em dia** *(último toque há 3 dias < 14)*

> **Lição de método embutida:** Beatriz tem reunião + patrimônio, mas **não** virou
> qualified porque falta fechar o "stay engaged" (critério #3 [WP]). É exatamente o
> desvio 8 que o Tutor cobra. Marque o 3º ✓ **e** mude Estágio → `Qualified
> prospect` para ver a próxima fórmula validar.

---

## Lead C — qualified em nurturing, com evento-gatilho (Zona B, prioridade)

**Base `Leads`:**
| Campo | Valor |
|---|---|
| Nome | Dr. Caio Exemplo (Anestesiologia) |
| Contato | +55 62 90000-0003 *(fictício)* |
| Origem | `Ex-Santander` |
| MAP / Nicho | `3 · Mercado natural (Santander)` |
| Estágio | `Nurturing` |
| Gate ✓ Reunião feita | ✅ · Gate ✓ Patrimônio R$1mi+ | ✅ · Gate ✓ Receptivo | ✅ |
| Patrimônio estimado (R$) | `3.500.000` |
| Perfil de interesse | "Vendeu participação em clínica; interesse em internacional e sucessão" |
| Banco / assessor atual | "BTG (assessor)" |
| Próximo toque (data) | hoje + 1 dia |
| Toques (relação) | → Toque 2 (abaixo) |
| Gatilhos (relação) | → Gatilho 1 (abaixo) |

**Toque 2 (base `Toques`):**
| Campo | Valor |
|---|---|
| Resumo | "Áudio com leitura de internacional pós-venda da clínica" |
| Data | **hoje − 20 dias** |
| Tipo | `Áudio` · Tema `Internacional` · Canal `WhatsApp` |
| Enviado por Eduardo? | ✅ |

**Gatilho 1 (base `Gatilhos`):**
| Campo | Valor |
|---|---|
| Descrição | "Vendeu participação na clínica (liquidez)" |
| Data | hoje − 7 dias |
| Tipo | `Venda de empresa/IPO/vesting` · Efeito `Subir à prioridade #1` |

**Fórmulas esperadas:**
- `Qualificado?` → **✅ Qualified** *(os 3 ✓)*
- `Gate · status` → *(vazio — está em Nurturing **com** os 3 ✓, consistente)*
- `Esfriando?` → **🥶 Esfriando (20d)** *(> 14 dias sem toque)*
- `Tem gatilho ativo?` → **1** → aparece na **Fila de prioridade**

> **Lição embutida:** Caio é o caso-ouro da estratégia Avis — qualified, com
> **money in motion** (venda da clínica) e **esfriando**. O digest deve cravá-lo no
> topo: "Dr. Caio teve gatilho (liquidez) e está há 20 dias sem toque — prioridade
> #1 hoje."

---

## Checklist de validação (rode após inserir o seed)
- [ ] `Sinal de engajamento` mostra Morno/Pronto conforme o nº de aberturas (Lead A).
- [ ] `Qualificado?` só dá ✅ no Lead C (os 3 ✓), não no B (falta 1).
- [ ] `Gate · status` fica vazio nos 3 (nenhum está em Qualified/Nurturing **sem** os ✓).
      Para ver o 🚨, ponha o Lead B em `Qualified prospect` sem o 3º ✓.
- [ ] `Esfriando?` = — (A, suspect), Em dia (B, 3d), 🥶 (C, 20d).
- [ ] Lead C aparece na view **Fila de prioridade** (tem gatilho).
- [ ] Kanban Pipeline mostra só B e C; Board de Aquecimento mostra só A.

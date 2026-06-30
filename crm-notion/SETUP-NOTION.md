# SETUP-NOTION.md — Runbook do CRM no Notion

> Passo a passo para criar as **3 bases** (Leads, Toques, Gatilhos), as **views**
> (kanban por estágio, board de aquecimento, painel de metas semanais) e gerar o
> **token de integração** do Notion. Estrutura completa em `MODELO-DADOS.md`.
>
> Há **dois caminhos**:
> - **Caminho A — manual (UI do Notion):** ~30-40 min, zero código. Recomendado se
>   você prefere mexer na mão.
> - **Caminho B — script:** `setup_notion.py` (F1.3) cria tudo via API. Precisa do
>   token (passo 1) e de uma página-pai onde as bases serão criadas.
>
> **Fórmulas:** este runbook traz a versão **canônica Notion Formula 2.0** (com
> `.name` na comparação de Status/Select). Ela **substitui** a versão simplificada
> do `MODELO-DADOS.md` §3 — cole estas.

---

## 1. Gerar o token de integração do Notion `<<<PREENCHER>>>`

> ⚠️ Credencial — **só Eduardo gera**. O token é segredo; **nunca** vai pro git
> (fica no `.env`, já ignorado). Registrado em `PROGRESS.md > PRECISO DE VOCÊ`.

1. Acesse **https://www.notion.so/my-integrations** (logado na sua conta).
2. **New integration** → nome `Motor Prospecção LDC` → workspace correto →
   tipo **Internal**.
3. Em **Capabilities**, marque: **Read content**, **Update content**,
   **Insert content**. (Não precisa de user info.)
4. **Submit** → copie o **Internal Integration Secret** (começa com `ntn_` ou
   `secret_`). Guarde no `.env` como:
   ```
   NOTION_TOKEN=ntn_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
5. **Compartilhe a página-pai com a integração:** abra (ou crie) a página que vai
   conter o CRM (ex.: "CRM Prospecção LDC") → menu `•••` → **Connections** →
   **Add connection** → selecione `Motor Prospecção LDC`. Sem isso a API responde
   `object_not_found`.
6. Copie o **ID da página-pai** (na URL, os 32 hex após o último `-`):
   ```
   NOTION_PARENT_PAGE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

> Esses dois valores destravam o Caminho B (script) **e** o Notion MCP (Fase 2).

---

## 2. Caminho A — criar as bases na UI (manual)

Crie 3 **databases** (full page) dentro da página-pai. Propriedades exatas em
`MODELO-DADOS.md`; resumo abaixo.

### 2.1 Base `Leads`
1. `/database - full page` → nome **Leads**.
2. Renomeie a coluna `Name` → **Nome** (Title).
3. Adicione as propriedades (tipo entre parênteses):
   - **Origem** (Select): `Newsletter LDC`, `Ex-Santander`, `Indicação`,
     `Campanha Goiânia`, `Scraping/lista`, `Evento`, `Outro`.
   - **MAP / Nicho** (Select): `A · Reativação`, `B · Médicos frios`,
     `C · COI-âncora`, `D · Autoridade/Conteúdo`, `Empresários (pausado)`,
     `Executivos (pausado)`. *(MAPs ativos = A-D; ver `MODELO-DADOS.md` §1.2.)*
   - **Estágio** (**Status**) — grupos:
     - *To-do:* `Suspect (aquecimento)`, `Lead pré-qualificado`
     - *In progress:* `Reunião agendada`, `Reunião feita`, `Qualified prospect`,
       `Nurturing`
     - *Complete:* `Cliente`, `Perdido / Inativo`
   - **Trilha de aquecimento** (Select): `❄️ Frio`, `📩 Inscrito (opt-in news)`,
     `🔆 Engajado`, `✅ Pronto`.
   - **Aberturas recentes (news)** (Number) · **Cliques recentes (news)** (Number).
   - **Gate ✓ Reunião feita**, **Gate ✓ Patrimônio R$1mi+**,
     **Gate ✓ Receptivo (stay engaged)** (3× Checkbox).
   - **Patrimônio estimado (R$)** (Number, formato Real).
   - **Perfil de interesse** (Text) · **Banco / assessor atual** (Text).
   - **Datas pessoais** (Date) · **Próximo toque (data)** (Date).
   - **Profissão / Especialidade** (Text) · **Faixa etária** (Select) ·
     **Produtos atuais** (Text).
   - As **fórmulas** e os **rollups** entram depois das relações (passo 2.4).

### 2.2 Base `Toques`
`/database - full page` → **Toques**. Title = **Resumo**. Propriedades:
**Data** (Date), **Tipo** (Select: Áudio/Mensagem/Ligação/Reunião/Artigo/Research/
Convite evento/Reconhecimento), **Tema** (Select: Macro BR/Internacional/
Ativos-empresas/Planejamento-datas/Pessoal), **Canal** (Select: WhatsApp/Telefone/
Presencial/E-mail), **Enviado por Eduardo?** (Checkbox).

### 2.3 Base `Gatilhos`
`/database - full page` → **Gatilhos**. Title = **Descrição**. Propriedades:
**Data** (Date), **Tipo** (Select: Troca de emprego/Herança-inventário/Venda de
empresa-IPO-vesting/Insatisfação c/ assessor/Aposentadoria/Divórcio-viuvez/Venda
de imóvel/Saída do assessor atual/PJ médica virada), **Efeito** (Select:
`Subir à prioridade #1`).

### 2.4 Relações + rollups + fórmulas (depois das 3 bases existirem)
Na base **Leads**:
1. **Toques** (Relation → `Toques`). Habilite "Show on Toques" (cria o reverso).
2. **Gatilhos** (Relation → `Gatilhos`).
3. **Último toque** (Rollup): relação `Toques` → propriedade `Data` →
   **Calculate = Latest date**.
4. **Tem gatilho ativo?** (Rollup): relação `Gatilhos` → `Efeito` →
   **Calculate = Count all** (ou `Show original` e contar).
5. **Qualificado?**, **Gate · status**, **Sinal de engajamento**, **Esfriando?**
   (Formula) — cole do §4 abaixo.

---

## 3. Caminho B — script (resumo; detalhe em F1.3)
```
python -m pip install -r crm-notion/requirements.txt
export NOTION_TOKEN=ntn_...            # ou no .env
export NOTION_PARENT_PAGE_ID=...
python crm-notion/setup_notion.py
```
O script é **idempotente**: rodar de novo não duplica. Falha com mensagem clara se
faltar o token (ver F1.3).

---

## 4. Fórmulas canônicas (Notion Formula 2.0 — cole estas)

> Em Formula 2.0, **Status e Select são objetos** → compare com **`.name`**.
> `prop("Estágio")` sozinho não compara com string; use `prop("Estágio").name`.

### 4.1 `Qualificado?` — gate dos 3 critérios [WP] (checkboxes → booleano, sem `.name`)
```
if(
  prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") and prop("Gate ✓ Receptivo (stay engaged)"),
  "✅ Qualified",
  "⛔ Ainda não (falta gate)"
)
```

### 4.2 `Gate · status` — alerta de diluição [WP] (usa `.name` no Status)
```
if(
  (prop("Estágio").name == "Qualified prospect" or prop("Estágio").name == "Nurturing")
    and not (prop("Gate ✓ Reunião feita") and prop("Gate ✓ Patrimônio R$1mi+") and prop("Gate ✓ Receptivo (stay engaged)")),
  "🚨 Qualified sem os 3 ✓ — revisar",
  ""
)
```

### 4.3 `Sinal de engajamento` — escada da trilha (Number, sem `.name`)
```
if(empty(prop("Aberturas recentes (news)")), "❄️ sem dado",
  if(prop("Aberturas recentes (news)") >= 4, "🔥 Pronto? (abriu " + format(prop("Aberturas recentes (news)")) + "/6)",
    if(prop("Aberturas recentes (news)") >= 2, "🟡 Morno (" + format(prop("Aberturas recentes (news)")) + "/6)",
      "❄️ Frio (" + format(prop("Aberturas recentes (news)")) + "/6)")))
```

### 4.4 `Esfriando?` — sem toque há +14 dias, só no pipeline [spec §7] (usa `.name`)
Suspects são aquecidos pela newsletter (não por toques 1:1) → ficam fora do alerta:
```
if(prop("Estágio").name == "Suspect (aquecimento)", "—",
  if(empty(prop("Último toque")), "⚠️ nunca tocado",
    if(dateBetween(now(), prop("Último toque"), "days") > 14,
      "🥶 Esfriando (" + format(dateBetween(now(), prop("Último toque"), "days")) + "d)",
      "🔥 Em dia")))
```

> **Por que `.name`:** sem ele, a comparação de um objeto Status/Select com string
> retorna `false` silenciosamente em Formula 2.0 — a fórmula "funciona" mas nunca
> dispara. As fórmulas de checkbox/number (4.1, 4.3) **não** usam `.name`.

---

## 5. Views (criar em cada base)

### 5.1 Em `Leads`
| View | Tipo | Filtro | Agrupar por | Ordenar |
|---|---|---|---|---|
| **Pipeline (kanban)** | Board | `Estágio` ≠ `Suspect (aquecimento)` | `Estágio` (Status) | — |
| **Aquecimento (kanban)** | Board | `Estágio` = `Suspect (aquecimento)` | `Trilha de aquecimento` | `Aberturas recentes` ↓ |
| **Prontos p/ toque 1:1** | Table | `Trilha` = `✅ Pronto` | — | — |
| **Esfriando ⚠️** | Table | `Esfriando?` contém `Esfriando` | `MAP / Nicho` | `Último toque` ↑ |
| **Fila de prioridade** | Table | `Tem gatilho ativo?` > 0 | — | data do gatilho ↓ |
| **🚨 Inconsistências** | Table | `Gate · status` não vazio | — | — |

### 5.2 Painel de metas semanais
Crie uma **página** "Painel de Metas" com **linked views** de `Leads` e `Toques`:
- **Reuniões da semana** — linked view de `Toques`, filtro `Tipo = Reunião` +
  `Data` esta semana → meta **2-3/sem**.
- **Prospects novos** — linked view de `Leads`, filtro `Qualificado? = ✅` +
  entrou esta semana → meta **1/sem**.
- **Pipeline total** — `Leads` com `Estágio` em {Qualified, Nurturing} → meta
  **~25-30**.
- **Esfriando ⚠️** — reusa a view do §5.1.
- **Conversão por MAP** — `Leads` agrupado por `MAP / Nicho` (contagem de Cliente
  vs total).

> O Tutor lê essas views via MCP (Fase 2) para o digest e o "mostra os números".

---

## 6. Checklist de pronto
- [ ] Token gerado e no `.env` (`NOTION_TOKEN`) — **depende de Eduardo**.
- [ ] Página-pai compartilhada com a integração (`NOTION_PARENT_PAGE_ID`).
- [ ] 3 bases criadas (manual ou script) com todas as propriedades.
- [ ] Relações + rollups (`Último toque`, `Tem gatilho ativo?`) configurados.
- [ ] 4 fórmulas coladas (versão `.name` do §4) e disparando.
- [ ] 6 views + painel de metas montados.
- [ ] Seed de teste inserido (`seed-exemplo.md`, F1.4) e fórmulas validadas.

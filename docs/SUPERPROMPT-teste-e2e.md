# SUPERPROMPT — Teste E2E do Motor de Prospecção (Hermes + Notion + Telegram)

> **Objetivo:** validar, de ponta a ponta, se o Tutor está funcionando e efetivo —
> separando claramente **o que funciona no backend** do **que falha na entrega
> (renderização do Telegram)**. Roda no Claude Code CLI (ou manualmente).
>
> **Caminhos importantes (Windows):**
> - Hermes home: `C:\Users\edusp\AppData\Local\hermes`
> - hermes.exe: `C:\Users\edusp\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe`
> - helper CRM: `python /c/Users/edusp/AppData/Local/hermes/crm.py` (caminho **git-bash**, barra normal)
> - `.env`: `C:\Users\edusp\AppData\Local\hermes\.env` (tem NOTION_API_KEY, OPENROUTER_API_KEY, TELEGRAM_*)
> - Bases Notion: Leads `38f62514-7d75-8183-8b92-d5982c746e61` · Toques `...814c...` · Gatilhos `...8149...`

---

## PROMPT (para o Claude Code CLI executar)

Você vai rodar um teste E2E do Motor de Prospecção e produzir uma **matriz pass/fail**
honesta. Execute cada camada na ordem; em cada item registre ✅/❌ + evidência (1 linha).
Use `--yolo` nos comandos `hermes -z` para auto-aprovar ferramentas no teste. Nunca exiba
segredos (mascarar `ntn_`/`sk-`). No fim, **limpe os dados de teste** criados.

### Camada 1 — CRM (helper crm.py direto, sem o agente)
Prova que a infraestrutura Notion + helper funciona, isolada do LLM.
1. `python /c/Users/edusp/AppData/Local/hermes/crm.py list-leads` → deve responder sem erro.
2. `python .../crm.py add-lead --nome "E2E Teste Lead" --map A --estagio "Lead pré-qualificado" --origem "Newsletter LDC" --patrimonio 1200000 --perfil "internacional" --banco "XP"` → "OK lead criado" + id.
3. `python .../crm.py find-lead "E2E Teste"` → encontra o lead (pega o id).
4. `python .../crm.py add-toque --lead-id <id> --resumo "E2E toque teste" --tipo Mensagem --tema Internacional --canal WhatsApp --enviado` → "OK toque criado".
5. `python .../crm.py add-gatilho --lead-id <id> --descricao "E2E gatilho teste" --tipo "Venda de empresa/IPO/vesting"` → "OK gatilho criado".
6. Verifique no Notion via API (curl + token do .env) que o lead, o toque e o gatilho existem e estão relacionados.

### Camada 2 — Agente (hermes -z --yolo: o LLM usando as skills/helper)
Prova que o Tutor entende e executa via linguagem natural.
- **A1 (método/gate):** `hermes -z "Conheci um médico que lê a news mas nunca me reuni com ele. Já é qualified prospect?" --yolo` → resposta correta: **NÃO** (falta reunião), com explicação ancorada no método.
- **A2 (registrar via NL):** `hermes -z "Registre o lead: Dr. E2E Natural, cardiologista, 1.5mi, cliente Itaú, interesse internacional. Confirme listando." --yolo` → deve **usar crm.py** (não urllib) e o lead **persiste** (confirme com `crm.py find-lead "E2E Natural"`).
- **A3 (ler CRM):** `hermes -z "Lista meus leads e me dá o diagnóstico de pipeline." --yolo` → lista os leads reais + diagnóstico Mullen. **Sem** "token expirado".
- **A4 (ânimo):** `hermes -z "Tô desanimado, ninguém fechou essa semana." --yolo` → reenquadra para **atividade, não conversão**.
- **A5 (conteúdo):** `hermes -z "Me ajuda no raio da semana sobre PJ médica." --yolo` → rascunho de conteúdo nichado, no tom, sem promessa de rentabilidade.
- **A6 (documento, se houver):** se existir PDF em `~/AppData/Local/hermes/cache/documents`, peça extração e confirme que usa a skill `ocr-and-documents` (não script ad-hoc).

### Camada 3 — Entrega (gateway + Telegram)
- **G1:** processo `hermes gateway run` (python) ativo? (`Get-CimInstance`/`tasklist`).
- **G2:** bot válido? `curl getMe` com TELEGRAM_BOT_TOKEN → `ok:true`.
- **G3 (renderização — o ponto crítico):** a entrega no Telegram depende do **cliente**.
  Documente: as respostas longas/formatadas (tabelas/markdown) podem mostrar
  *"This message is not supported by your version of Telegram"* em **clientes
  desktop desatualizados**. Teste de aceitação: enviar `/reset` e depois uma pergunta
  no **app do celular atualizado** → deve renderizar. Se o desktop falhar e o celular
  funcionar → o backend está OK; o problema é versão do cliente.

### Saída esperada (matriz)
```
CAMADA 1 (CRM):    C1 ✅ C2 ✅ C3 ✅ C4 ✅ C5 ✅ C6 ✅
CAMADA 2 (Agente): A1 ✅ A2 ✅ A3 ✅ A4 ✅ A5 ✅ A6 ✅/N/A
CAMADA 3 (Entrega):G1 ✅ G2 ✅ G3 ⚠️ (depende do cliente Telegram)
```
+ diagnóstico: se 1 e 2 passam e só G3 falha → **o motor funciona; o gargalo é o
cliente Telegram (atualizar app / usar celular)**, não o agente.

### Limpeza
Remova os leads/toques/gatilhos de teste criados (via API delete ou arquive no Notion):
"E2E Teste Lead", "Dr. E2E Natural", e o "Dr. Teste Silva" se quiser zerar a base.

## (fim do PROMPT)

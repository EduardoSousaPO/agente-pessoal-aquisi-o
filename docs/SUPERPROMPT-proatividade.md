# SUPERPROMPT — Tornar o Tutor PROATIVO no método Mullen (rodar no Claude Code CLI)

> **Como rodar sem travas:** abra o Claude Code CLI e cole o PROMPT abaixo. Se quiser
> zero interrupção de permissão, inicie com `claude --dangerously-skip-permissions`
> (ou aceite "Always" nos prompts). Este trabalho mexe em arquivos do Hermes e agenda
> tarefas — não toca no repositório do projeto.

## Contexto fixo (caminhos reais — Windows)
- Hermes home: `C:\Users\edusp\AppData\Local\hermes`
- hermes.exe: `C:\Users\edusp\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe`
- Cérebro/persona: `C:\Users\edusp\AppData\Local\hermes\SOUL.md`
- Skills LDC: `C:\Users\edusp\AppData\Local\hermes\skills\ldc\{metodo-mullen,curadoria-diaria,intake-interview,conteudo-autoridade}`
- Helper CRM (git-bash path): `python /c/Users/edusp/AppData/Local/hermes/crm.py`
- Telegram home channel (Eduardo): chat id `5248742295`
- Modelo atual: `anthropic/claude-sonnet-4.6` (já configurado)
- O gateway roda via `hermes gateway run` (processo em background; reiniciar = matar o python `gateway run` e subir de novo).

---

## PROMPT (cole a partir daqui)

Você é um engenheiro configurando o agente-tutor de prospecção (Hermes) do Eduardo para ser **proativo** no método David Mullen — não só reativo. Use o hermes.exe pelo caminho acima. Descubra a sintaxe exata dos comandos com `--help` antes de usar (não invente flags). Ao terminar, **reinicie o gateway** e **verifique** cada item. Não exiba segredos (tokens `ntn_`/`sk-`). Trabalhe direto, sem pedir confirmação a cada passo.

### Tarefa 1 — Postura proativa + respostas enxutas (editar SOUL.md)
Abra `C:\Users\edusp\AppData\Local\hermes\SOUL.md` e **adicione uma seção nova** no fim, chamada `## Postura proativa (conduzir, não esperar)`, com estas diretrizes:
- **Conduza a agenda.** Ao iniciar o dia ou quando Eduardo abrir uma conversa sem tarefa clara, NÃO espere — proponha o próximo passo concreto do método: leia o CRM (via `crm.py list-leads`), reporte o LEADING (reuniões da semana, leads esfriando, inflow), e sugira **1 ação concreta agora** ("hoje: toca no Dr. X que esfriou / marca 1 reunião pra bater a meta").
- **Sempre termine com um próximo passo acionável** (não uma pergunta aberta vaga). Ex.: "Quer que eu rascunhe o toque pro Dr. X?" com o rascunho já pronto ou a um clique.
- **Cobre as metas** (calibradas: 2-3 reuniões/semana, 1 prospect novo/semana) de forma consultiva quando perceber que a semana está fraca.
- **Respostas ENXUTAS no Telegram:** curto, em blocos de 1 ideia, sem parede de texto. Um gancho + uma ação. Se precisar detalhar, ofereça "quer que eu detalhe?" em vez de despejar tudo.
- **Celebra atividade/streak** proativamente quando Eduardo registrar toques/reuniões.
Mantenha o resto do SOUL intacto. Preserve o tom (caloroso, direto, "conversa de gente").

### Tarefa 2 — Digest diário automático (o "bom dia" proativo)
Crie uma tarefa agendada no Hermes que, **todo dia útil às 07:00**, rode a lógica da skill `curadoria-diaria` e **entregue o digest no Telegram** do Eduardo (home channel / chat `5248742295`).
- Descubra o mecanismo: `hermes cron --help` (e/ou `hermes send --help`). Prefira o cron nativo do Hermes.
- O prompt agendado deve instruir o agente a: (1) ler o CRM (`crm.py list-leads` + quem está esfriando/pronto/com gatilho), (2) varrer os 4 temas de mercado (web) e cruzar com o `Perfil de interesse` dos leads, (3) montar um **digest enxuto**: linha de metas (LEADING) + 2-3 toques prontos (lead + gancho + rascunho no tom do Eduardo) + 1 próxima ação. Reforce: o agente **não envia toque a lead**, só prepara; envio é sempre do Eduardo.
- Se o cron nativo não permitir entrega direta no Telegram, use `hermes send` (ou configure o job para postar no home channel). Teste que a entrega chega no chat `5248742295`.

### Tarefa 3 — Ritual semanal (placar de sexta)
Crie outra tarefa agendada: **sexta-feira às 17:00**, gerar o "placar da semana": atividade vs meta (LEADING), 1 vitória concreta, 1 ajuste, e o check da "regra dos 12 semanas" (não trocar de alavanca cedo). Entregar no mesmo home channel.

### Tarefa 4 — Reiniciar e verificar
1. Reinicie o gateway (mate o processo python `gateway run` e suba `hermes gateway run` em background/oculto).
2. Verifique e reporte: (a) SOUL.md tem a seção nova; (b) `hermes cron list` (ou equivalente) mostra os 2 jobs (digest diário + semanal); (c) o modelo é `anthropic/claude-sonnet-4.6`; (d) o gateway está ativo; (e) faça um **teste real**: dispare o job do digest manualmente (`hermes cron run <id>` ou equivalente) e confirme que o agente monta o digest lendo o CRM (sem erro de token; usando `crm.py`).
3. Se algo do cron não for suportado da forma ideal, **não invente** — documente a limitação e proponha o fallback (ex.: agendar via Agendador de Tarefas do Windows chamando `hermes -z "<prompt do digest>" --yolo`).

### Saída esperada
Um resumo: o que foi configurado, o `id`/horário de cada job agendado, e o resultado do teste manual do digest (o digest que o agente gerou). Aponte qualquer limitação e o fallback aplicado.

## (fim do PROMPT)

# Setup no Claude Code

## 1. Instalar
- Skill: copie a pasta `cs-sounding-teaser-prospects` para `~/.claude/skills/` (ou instale pelo plugin da igc).
- Python: `py -m pip install openpyxl playwright` e depois `py -m playwright install chromium` (no Windows use `py`; `python` pode abrir a Microsoft Store. No Linux/macOS, `python3`).
- Node/npm instalado (o `montar.py` baixa a fonte Source Serif 4 pelo npm).

## 2. Conectar
- MCPs Box, Granola e Microsoft 365, logados na conta com acesso a `4 - Capital Solutions`.
- Web search e web fetch liberados.
- Confira com `/mcp` que os três aparecem como conectados.

## 3. Primeiro teste (manual)
Rode na sessão, acompanhando:
```
Rode a skill cs-sounding-teaser-prospects em modo lote, seguindo references/lote.md. É a primeira execução: use --criar-corte 15 --limite 15. Não faça perguntas. Ao terminar, mostre o resumo gravado no _execucoes.md.
```
Confira depois: 1 pasta por prospect gerado, 3 arquivos em cada, `_estado.json` e `_execucoes.md` na raiz.

## 4. Agendar (diário)

Prompt da tarefa:
```
Rode a skill cs-sounding-teaser-prospects em modo lote, seguindo references/lote.md, com limite de 25 prospects. Não faça perguntas. Se a fila estiver vazia, termine sem mexer no Box. Ao terminar, responda com o resumo gravado no _execucoes.md.
```

**Opção A, app desktop do Claude Code (mais simples):** crie uma tarefa agendada diária (ex.: 7h, dias úteis) na pasta de trabalho, com o prompt acima. Roda enquanto o app estiver aberto e o PC ligado.

**Opção B, Agendador de Tarefas do Windows (roda mesmo com o app fechado):** crie uma tarefa diária que execute, na pasta de trabalho:
```
claude -p "<prompt acima>"
```
Como ninguém aprova nada no modo `-p`, libere as ferramentas antes em `.claude/settings.json` da pasta de trabalho:
```json
{
  "permissions": {
    "allow": [
      "Bash(py:*)", "Bash(python3:*)", "Bash(npm:*)", "Bash(npm.cmd:*)",
      "Read", "Write", "Edit", "Glob", "Grep", "Task",
      "WebSearch", "WebFetch",
      "mcp__<box>", "mcp__<granola>", "mcp__<microsoft365>"
    ]
  }
}
```
Troque `<box>`, `<granola>` e `<microsoft365>` pelos nomes de servidor que aparecem em `/mcp` (ex.: `mcp__claude_ai_Box`). Teste uma vez rodando o comando à mão: se ele parar pedindo permissão, falta algum item na lista.

Dias sem prospect novo custam pouco: a execução lê a base, vê a fila vazia e termina.

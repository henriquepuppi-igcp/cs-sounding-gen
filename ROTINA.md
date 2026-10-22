# Rotina na nuvem: sounding teasers diários

## 1. Repositório
1. Crie um repositório **privado** no GitHub (ex.: `igc-sounding-teaser`) e suba este conteúdo.
2. Para atualizar a skill depois, substitua `.claude/skills/cs-sounding-teaser-prospects/` e faça push.

## 2. Ambiente
Em claude.ai/code, crie um ambiente de nuvem (ex.: `teaser`):
- **Setup script:** cole o conteúdo de `setup.sh`.
- **Network access:** Custom, com "Also include default list of common package managers" marcado, mais os domínios:
  `cdn.playwright.dev`, `playwright.download.prss.microsoft.com`, `playwright.azureedge.net`
  (download do Chromium). Se a primeira execução falhar com `host_not_allowed` em algum outro domínio, adicione-o.

## 3. Rotina
Em claude.ai/code/routines, **New routine**:
- **Nome:** Sounding teasers diários
- **Repositório:** `igc-sounding-teaser`
- **Ambiente:** `teaser`
- **Conectores:** mantenha só Box, Granola e Microsoft 365.
- **Gatilho:** Schedule, dias úteis, 7h.
- **Modelo:** o mesmo que você usa no Claude Code.
- **Prompt:**

```
Rode a skill cs-sounding-teaser-prospects em modo lote, seguindo references/lote.md, com limite de 25 prospects. Use python3 e a pasta de trabalho /tmp/teaser. Não faça perguntas, commits nem pull requests. Se a fila estiver vazia, termine sem mexer no Box. Ao terminar, responda com o resumo gravado no _execucoes.md.
```

## 4. Testar
1. Na página da rotina, clique **Run now**.
2. Abra a execução e leia a transcrição: o status verde só indica que a sessão rodou sem erro de infraestrutura, não que a tarefa deu certo.
3. Confira `_execucoes.md` na raiz de Sounding Teasers no Box.

## 5. Desligar a tarefa local
Depois que a rotina rodar bem, desative a tarefa agendada do PC para não rodar duas vezes.

## Limites
- Conta no uso da assinatura e no limite diário de execuções de rotinas (1 por dia cabe em qualquer plano).
- Em Team/Enterprise, um Owner pode ter desativado rotinas para a organização. Se não aparecer a opção, peça para habilitar.
- Recurso em research preview.

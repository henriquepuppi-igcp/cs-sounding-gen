# Modo lote (execução diária no Claude Code)

Roda a skill para todo prospect da base de CS que ainda não tem pasta em Sounding Teasers. Um prospect conta como pronto assim que entra na base, com qualquer status.

**Backlog:** só as 15 últimas linhas da base na data da primeira execução. Todas as linhas anteriores ficam fora para sempre (lista `_ignorar` no `_estado.json`). Daí em diante, entra todo prospect novo da base.

## Estado no Box (raiz Sounding Teasers, `429739842036`)

| Arquivo | Conteúdo |
|---|---|
| pastas `{ID} - [PRODUTO] - {NAME}` | Prospect já feito. A existência da pasta é o que marca "feito". |
| `_estado.json` | `{"_ignorar": [IDs fora do backlog], "_codinomes": {"<ID>": "Projeto X"}, "<ID>": {"status": "pulado" ou "erro", "motivo": "...", "data": "AAAA-MM-DD"}}`. Fora `_codinomes`, só guarda o que não virou pasta. |
| `_execucoes.md` | Uma seção por execução, a mais nova no topo. |

Pulados voltam para a fila depois de 28 dias (`ESPERA_DIAS` em `scripts/pendentes.py`). Erros voltam na execução seguinte. A pasta de um prospect com erro na revisão pode existir; nesse caso, ele volta pela lista de erros do `_estado.json`, não pela fila de pendentes.

Nos comandos, `<py>` é `python3` no Linux/macOS e `py` no Windows (lá `python` pode abrir a Microsoft Store).

## Passos

1. **Base:** ache a maior versão de `Base prospects I CS vN.xlsx` fora de `_old` (ver `fontes.md`). Se a máquina tiver o Box Drive, leia o `.xlsx` direto; senão, salve o retorno de `mcp__Box__get_file_content` em arquivo.
2. **Feitos:** liste todas as pastas de `429739842036` (pagine até cobrir `totalCount`) e grave os nomes em `pastas.json`.
3. **Estado:** baixe `_estado.json` da raiz, se existir.
4. **Fila:**
   - Primeira execução (sem `_estado.json`): `<py> scripts/pendentes.py <base> pastas.json - --criar-corte 15 --limite 15`. Grava `_estado.json` local com o `_ignorar`.
   - Demais: `<py> scripts/pendentes.py <base> pastas.json _estado.json --limite 25`.
   - **Fila vazia:** termine aqui, sem subir nada e sem escrever no `_execucoes.md`. Responda só "Nenhum prospect novo".
4b. **Codinomes:** pegue `_codinomes` do `_estado.json`. Se não existir (ou faltar algum ID que já tem pasta), monte lendo a 1ª linha do `_matchmaking.txt` de cada pasta (`DEAL: <Empresa> (<Codinome>)`). Dê a cada subagente do bloco uma **letra inicial diferente** para o codinome, sem repetir letras dentro do bloco (ex.: C, L, T, M, A), e passe a lista inteira de codinomes já usados.
5. **Aquecer o ambiente (uma vez, antes dos subagentes):** rode `scripts/montar.py` nos templates de `assets/templates/` numa pasta temporária. Isso baixa a fonte e abre o Chromium uma vez, em vez de cada subagente fazer isso ao mesmo tempo.
6. **Execução:** para cada item da fila, dispare **um subagente por prospect**, com o prompt:
   > Rode a skill cs-sounding-teaser-prospects para o prospect ID <ID>, <Deal>, site <Site>. Modo lote: não faça perguntas. A linha da base já está aqui, não baixe a base: <JSON de "linha">. Pasta de destino em Sounding Teasers: <id da pasta existente, ou "criar">. Codinome: escolha um que comece com a letra <LETRA> e que não esteja nesta lista: <codinomes usados>. Ambiente já aquecido. Responda só com uma linha JSON: {"ID":..., "status":"gerado|pulado|erro", "motivo":"...", "pasta":"<link ou vazio>", "pasta_id":"...", "codinome":"...", "atencao":"<conflitos de interesse e correções para a base, resumidos>"}.

   Rode em blocos de 5 subagentes em paralelo: dispare 5, espere os 5 terminarem, dispare os próximos 5. Um prospect nunca é processado no contexto do orquestrador, para não estourar o contexto.
7. **Revisão pelo orquestrador:** depois de cada bloco, para cada prospect gerado, confira:
   - a pasta tem os 3 arquivos (`_interna.html`, `_envio.html`, `_matchmaking.txt`);
   - o TXT tem as linhas `DEAL:`, `MACROPRODUTO:` (dentro da linha `SETOR:`) e `OPERAÇÕES EM SONDAGEM:`;
   - a versão de envio não cita o nome do deal nem o domínio do site (busca simples no texto);
   - a versão de envio não traz números públicos que identifiquem a empresa (receita, dívida, rating, nº de clientes que constem do site ou da imprensa). Se trouxer, marque como `erro` ("número público no envio"): a regra de anonimização manda generalizar;
   - a versão de envio não tem `[pendente]` nem outro placeholder ("a informar" e "yield a descobrir" são permitidos) e tem as 2 páginas com term sheet e garantias;
   - o codinome não repete nenhum da lista nem outro do mesmo bloco. Se repetir, marque como `erro` ("codinome repetido").
   Leia só o necessário para essas checagens. Se uma falhar, marque o prospect como `erro` com o motivo; ele roda de novo na execução seguinte e substitui os 3 arquivos.
8. **Atualizar estado:** remova do `_estado.json` os IDs gerados; grave pulados e erros com a data de hoje; grave o codinome de cada gerado em `_codinomes`. Suba com `upload_file_version` (ou `upload_file` na primeira vez).
9. **Registrar:** adicione no topo do `_execucoes.md`:
   ```
   ## DD/MM/AAAA
   Gerados: N · Pulados: N · Erros: N · Pendentes: N · Em espera: N
   - <ID> - <Deal>: gerado · <atencao>
   - <ID> - <Deal>: pulado · <motivo>
   ```

## Regras

- Modo lote nunca pergunta nada. O que pediria atenção vai para a caixa "Fontes e pontos de atenção" da interna e, se for conflito de interesse, só para o `_execucoes.md`.
- Se a base não for encontrada ou o Box falhar no passo 1 ou 2, aborte a execução inteira e registre só no `_execucoes.md`. Sem a lista de feitos, a execução duplicaria pastas.
- Um erro num prospect não interrompe os outros.

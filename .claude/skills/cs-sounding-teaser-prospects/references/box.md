# Salvar no Box

- **Raiz:** `4 - Capital Solutions/Sounding Teasers`, folder id `429739842036`.
- **Pasta do prospect:** `{ID} - [PRODUTO] - {NAME}`. Ex.: `5532 - [Finserv consolidado] - 6P Condo`; sem macroproduto, `5535 - [PRODUTO] - LN Urbanismo`.
- **Arquivos da skill (só estes 3):** os que terminam em `_interna.html`, `_envio.html` e `_matchmaking.txt`.

## Passos

1. `mcp__Box__list_folder_content_by_folder_id` em `429739842036` (pagine com `offset` até cobrir `totalCount`). A pasta do prospect é a que começa com `{ID} - `. O ID manda, nunca o nome.
2. **Não existe:** crie com `mcp__Box__create_folder` (carregue o schema com `tool_search`) dentro de `429739842036`.
3. **Existe com nome diferente** (macroproduto preenchido depois, deal renomeado): renomeie com `mcp__Box__update_folder_properties` para o nome atual.
4. Liste a pasta do prospect. Para cada um dos 3 arquivos, ache o existente pelo **sufixo** (`_interna.html`, `_envio.html`, `_matchmaking.txt`), não pelo nome inteiro:
   - **existe:** `mcp__Box__upload_file_version` com o `file_id` (substitui o conteúdo). Se o nome mudou, renomeie com `mcp__Box__update_file_properties`.
   - **não existe:** `mcp__Box__upload_file` com `parent_folder_id` da pasta do prospect.
   - `file_content` é o texto completo do arquivo (leia do disco e passe inteiro).
5. **Nunca** apague, mova, renomeie ou sobrescreva qualquer outro arquivo ou subpasta da pasta do prospect.
6. Se um upload falhar, tente de novo uma vez. Se falhar de novo, informe quais arquivos não subiram.

## Limites do conector

- Só sobe texto (txt, md, html, csv, json).
- Não tem ação de apagar arquivo. Por isso a reexecução substitui o conteúdo dos 3 arquivos (nova versão) em vez de apagar e recriar. O resultado é o mesmo, e o histórico de versões do Box fica preservado.

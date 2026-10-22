# Fontes de dados

## 1. Base de prospects de CS (Box)

- **Arquivo:** `Base prospects I CS vN.xlsx`, sempre a **maior versão** que estiver na pasta `4 - Capital Solutions / … / 4. Arquivos padrão - Originação` (folder id `242406799075` no piloto). Versões antigas ficam em `_old` e nunca devem ser usadas.
- **Como achar:** `mcp__Box__search_files_keyword` com query `Base prospects I CS`, `ancestor_folder_id` = `237205674854` (4 - Capital Solutions), extensão `xlsx`. Pegue a maior versão fora de `_old`.
- **Leitura:** `mcp__Box__get_file_content`. O resultado costuma ser grande e vai para arquivo, então use python/grep para achar a linha pelo nome do deal e pelo site.
- **Linhas duplicadas:** a mesma empresa pode aparecer mais de uma vez, com origens diferentes (por exemplo, uma linha "Base CS" ativa e outra "Standby M&A"). Use a linha de CS ativa e registre a duplicata na caixa "Fontes e pontos de atenção" como correção a fazer na base.

### Colunas principais

ID, Deal, OP 1, OP 2, Status, Stage, Data Stage, **Macrosetor**, **Microsetor**, Escopo, Tipo, **Macroproduto**, Microproduto, **Cidade**, Link (Box), E-mail, **Site**, Fee…, Score, **Notes**, e depois os blocos de métricas por macroproduto, seguidos de Deal Summary e Deal Description.

### Métricas por macroproduto (grandes números)

O cabeçalho agrupa as colunas de métricas por macroproduto. **Leia a linha de grupos na aba Inputs em tempo de execução**, porque a base muda de versão. Referência da v11:

| Grupo | Colunas |
|---|---|
| Corporativo | Fat, EBITDA, Dívida Líquida, Auditado, Contas a Receber, PMR, Garantias |
| Crédito US | % Fat USD |
| Fin B2C | Nicho Setorial |
| Fin B2B | Fat longtail, Venda para PMEs pulverizados, Prazo de Recebimento (longtail) |
| Finserv (early stage e consolidado) | Carteira de Crédito, Originação Mensal, Prazo Médio (meses), Taxa a.m., Over90 (%), Ticket Médio, PL FIDCs, % Sênior, % Mezanino, Spread Sênior, Spread Mezanino |
| Project Finance | Índice de Cobertura (%), LTV (%), VP/SD (%) |

Para Finserv consolidado, o sócio validou o bloco Finserv inteiro como "grandes números". Se a exportação deixar dúvida sobre onde um grupo termina, use o bloco inteiro e registre a dúvida na caixa "Fontes e pontos de atenção".

Os cards de grandes números seguem as colunas do macroproduto. O Granola atualiza os valores. O card pode trazer uma nota curta de contexto (por exemplo, "Over180 de 15%").

## 2. Granola

- `mcp__Granola__query_granola_meetings`: pergunte pelo que a empresa faz, números, necessidade de capital e ideia de deal, sócios e histórico, interlocutores (nome, cargo, e-mail) e **as datas das reuniões**.
- A reunião mais recente prevalece. Confira as datas citadas nas notas: no piloto, um "agosto de 2025" provavelmente era 2026. Quando a data não fizer sentido, use a interpretação mais provável e registre na caixa "Fontes e pontos de atenção".
- Nomes vindos de transcrição podem estar errados. Cruze com as outras fontes; se divergirem, use a mais recente e registre na caixa "Fontes e pontos de atenção".

## 3. Site da empresa

- `web_fetch` na home. A sede costuma estar no rodapé (razão social, CNPJ, endereço). É essa a fonte da seção 2.
- Números públicos do site (por exemplo, "+450 mil clientes") podem entrar na descrição da interna. Na versão de envio, generalize.

## 4. Web e imprensa

- `web_search` para "<sócio> <empresa>", captações anteriores e novos executivos.
- É fonte para o histórico de sócios e executivos. **Nunca é fonte de financials** quando o Granola ou a base tiverem o dado.

## 5. Outlook (Microsoft 365)

- `mcp__Microsoft_365__outlook_email_search` pelo domínio da empresa (a coluna E-mail da base traz o domínio, por exemplo `@gooroocredito.com.br`) para completar e-mails e cargos dos interlocutores.

## 6. Pasta do prospect no Box

- **Onde:** `4 - Capital Solutions / Prospects Capital Solutions`, folder id `248424362051` (~4.000 pastas, nomeadas só pelo nome da empresa, sem ID).
- **Como achar:** `mcp__Box__search_folders_by_name` com o nome do deal e `ancestor_folder_id` = `248424362051`. Tente também variações (sem acento, sem "Ltda/S.A.", só a primeira palavra). Só aceite pasta cujo pai direto seja `248424362051` (confira com `get_folder_details`, campo `path_collection`).
- **O que ler:** liste a pasta e leia com `get_file_content` os arquivos que trazem negócio e números: apresentações institucionais, demonstrações financeiras, carteira, propostas, e-mails salvos. Ignore NDA e arquivos acima de ~50 MB.
- **Peso:** vale a data do arquivo. Financials da pasta mais recentes que a base prevalecem, com divergência registrada.
- Se não houver pasta, siga sem ela e registre "pasta do prospect: não encontrada" na caixa "Fontes e pontos de atenção".
- O link "Link (Box)" da base pode apontar para a pasta de M&A (Células) da mesma empresa. Nunca use pasta fora de `4 - Capital Solutions`. Se o link sair de CS, ignore e registre na caixa "Fontes e pontos de atenção".

## 7. Informação dada diretamente

- O que o usuário escrever na mensagem (números, ideia de deal, objetivo, codinome, contato) é uma fonte como as outras, com a data da mensagem.
- Divergências com as outras fontes seguem a regra geral (vale a mais recente) e vão para a caixa "Fontes e pontos de atenção".

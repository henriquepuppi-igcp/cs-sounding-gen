---
name: "cs-sounding-teaser-prospects"
description: Gera o sounding teaser da IGC Capital Solutions para o time de RI sondar um prospect com investidores, de ponta a ponta e sem checkpoints humanos. A partir do nome (e site, se houver) do prospect, puxa base de CS, pasta do prospect no Box, Granola, site, imprensa e Outlook, monta a versão interna e a versão anonimizada de envio em HTML e o TXT para matchmaking, e salva no Box em 4 - Capital Solutions/Sounding Teasers/{ID} - [PRODUTO] - {NAME}. Use SEMPRE que o usuário rodar /teaser, pedir "sounding teaser", "teaser de sondagem", "teaser pro RI", "material para sondar investidores", "monta o teaser da empresa X", ou der nome de um prospect pedindo material de sondagem, mesmo sem citar a skill. Também roda em modo lote diário (Claude Code) para os prospects da base sem teaser. NÃO use para CIM, deck completo, perfil de investidor, dossiê de pesquisa (cs-company-research) ou rodar o matchmaking em si (cs-matchmaking).
---

# Sounding Teaser (prospects) — IGC Capital Solutions

Transforma o nome de um prospect de CS em um sounding teaser pronto para o RI, com duas versões em HTML e TXT para matchmaking, salvos no Box. Roda inteiro sem perguntar nada ao usuário.

O conteúdo e o design foram calibrados num piloto real (GooRoo, set/2026) com correções do sócio. **As regras de conteúdo, anonimização, identidade visual e os templates não mudam.** O que mudou em relação à versão com checkpoints está em "Modo automático" (`references/regras-conteudo.md`).

## Entradas

- **Obrigatório:** nome do prospect.
- Opcional: site, codinome e qualquer informação dada diretamente na mensagem.

## Saídas

Pasta `{ID} - [PRODUTO] - {NAME}` dentro de `4 - Capital Solutions/Sounding Teasers` (folder id `429739842036`), com:

| Arquivo | Conteúdo |
|---|---|
| `{NAME}_interna.html` | Versão interna, todas as páginas A4 |
| `{NAME}_envio.html` | Versão para envio, anonimizada |
| `{NAME}_matchmaking.txt` | Texto para o cs-matchmaking |

- `{ID}` é a coluna ID da base de prospects de CS. `PRODUTO` é a coluna Macroproduto, entre colchetes (ex.: `5532 - [Finserv consolidado] - 6P Condo`). Com macroproduto vazio, fica o texto literal `[PRODUTO]` (ex.: `5535 - [PRODUTO] - LN Urbanismo`). `{NAME}` é a coluna Deal. Tire de todos os pedaços os caracteres `/ \ : * ? " < > |`.
- A pasta pode ter outros arquivos, de outras pessoas ou skills. A skill só mexe nesses 3.
- Os mesmos 3 arquivos também saem no chat com `present_files`.
- O PDF, quando necessário, sai do próprio HTML (imprimir › salvar como PDF; o CSS já define A4 e quebra de página).

## As 9 seções

| # | Seção | Fonte | Na versão de envio |
|---|---|---|---|
| 1 | Setor / subsetor | Base de CS (literal) | Sim, rótulo de mercado |
| 2 | Cidade/UF da sede | Site (rodapé/endereço) | Só a região |
| 3 | Macroproduto de crédito | Base de CS (literal) | Vira "Instrumentos" |
| 4 | Descrição | Granola + pasta do prospect + site + base | Sim, anonimizada |
| 5 | Grandes números | Colunas do macroproduto na base + Granola + pasta do prospect | Sim, com cards obrigatórios; sem dado vira "a informar" |
| 6 | Contexto / ideia de deal | Granola + pasta do prospect (não validado) | "A oportunidade" (term sheet) e "Garantias" |
| 7 | Objetivo do sounding | Derivado da seção 6 (não validado) | Não |
| 8 | Sócios e histórico | Granola + web | Sim, com nome e breve histórico |
| 9 | Interlocutores | Granola + Outlook | Não |

Detalhes de conteúdo, estilo, anonimização e modo automático: `references/regras-conteudo.md`.

## Fluxo

### Passo 1 — Coleta

Leia `references/fontes.md` antes de começar. As fontes são equivalentes, sem hierarquia entre elas; consulte todas.

**Velocidade:** as consultas não dependem umas das outras. Dispare na mesma rodada, em paralelo, a busca no Granola, a busca da pasta do prospect, o `web_fetch` do site, as buscas na web e a busca no Outlook. No modo lote, a linha da base já vem no prompt: não baixe a base de novo.


1. **Informação dada na mensagem.**
2. **Base de prospects de CS (Box):** linha do prospect, com ID, Deal, macrosetor, microsetor, macroproduto, cidade, notes e métricas do grupo do macroproduto.
3. **Pasta do prospect** em `Prospects Capital Solutions` (folder id `248424362051`), se existir.
4. **Granola**, com a data de cada reunião.
5. **Site** (`web_fetch`).
6. **Web e imprensa:** histórico dos sócios e executivos.
7. **Outlook:** e-mails e cargos dos interlocutores que faltarem.

**Paradas obrigatórias** (não gera nada, só informa o motivo no chat):
- prospect não encontrado na base de CS (sem `{ID}` não há pasta);
- nenhuma informação de negócio além da base (sem Granola, sem pasta e sem site).

### Passo 2 — Consolidação

- **Divergência entre fontes: vale sempre o dado mais recente.** Registre cada divergência na caixa "Fontes e pontos de atenção" da versão interna e no log, no formato: base dizia X, substituído por Y (fonte, data).
- **Setor, subsetor e macroproduto: sempre os da base, literais.** Se parecerem errados, use-os mesmo assim e registre na caixa "Fontes e pontos de atenção" como correção a fazer na base.
- **Macroproduto vazio na base:** não invente. Seção 3 vira `[pendente]` na interna; na versão de envio, "Instrumentos" sai dos instrumentos da ideia de deal (seção 6); no TXT, `MACROPRODUTO: a confirmar (vazio na base)`; na pasta, `[PRODUTO]`.
- **Nunca invente número.** O que faltar vira `[pendente]` na versão interna e some da versão de envio.
- **Nomes de pessoas:** se as fontes divergirem, use a mais recente e registre na caixa "Fontes e pontos de atenção".
- **Conflito de interesse** (por exemplo, sócio da IGC com participação no prospect): não entra em nenhum HTML nem no TXT. Vai só na resposta do chat (ou no `_execucoes.md`, no modo lote).

### Passo 3 — Montar as páginas

Siga `references/render.md`. Resumo: copie `assets/templates/` para `<trabalho>/<NAME>/paginas/`, troque só o conteúdo e mantenha estrutura, estilos e tamanhos. Monte, teste e corrija com `scripts/montar.py` até sair `OK`:

- **Transbordo:** crie página nova (`Interna-5.dc.html`…) e atualize o rodapé "x de N". Nunca comprima a ponto de cortar.
- **Vazamento na versão de envio:** reescreva o trecho de forma genérica.
- **Placeholder na versão de envio:** remova o item.

Depois rode a checagem de consistência de `references/regras-conteudo.md` (preços, subordinação, singular/plural, rótulos atual × alvo).

### Passo 4 — TXT

Gere o TXT conforme `references/txt-matchmaking.md`, a partir das páginas finais.

### Passo 5 — Salvar no Box

Leia `references/box.md`. Resumo: ache a pasta pelo `{ID}` ou crie `{ID} - [PRODUTO] - {NAME}` em `429739842036`. Rodar de novo para o mesmo prospect substitui só os 3 arquivos da skill; os demais arquivos da pasta nunca são tocados.

### Passo 6 — Resposta

`present_files` com os 3 arquivos. Na mensagem, em poucas linhas: link da pasta no Box, codinome escolhido, conflitos de interesse (se houver) e correções a fazer na base.

## Modo lote

Para rodar em todos os prospects pendentes da base (tarefa agendada diária), siga `references/lote.md`. O fluxo de um prospect é o mesmo de cima, executado por um subagente por prospect. Prompt da tarefa e pré-requisitos: `assets/agendamento-claude-code.md`.

## Regras fixas do piloto

1. Setor, subsetor e macroproduto vêm sempre da base. Se estiver errado, corrige-se a base.
2. Nos números, vale a fonte mais recente, com a divergência sinalizada na interna.
3. O Over90 entra como está, inclusive na versão de envio.
4. A versão de envio segue o conteúdo pedido pela Fabi (22/10/2026): resumo da companhia, financials ou carteira, sócios com nome, term sheet (volume, prazo, taxa, garantias, LTV/cobertura) e valor das garantias. Preços e subordinação das cotas são indicativos e rotulados como estrutura-alvo. Campo sem dado vira "a informar". Não leva `[pendente]`, nomes de interlocutores ou de terceiros (bancos, gestoras, clientes) nem frentes paralelas. Ver `references/regras-conteudo.md`.
5. Subordinação é o que está abaixo da tranche: numa estrutura 65/20/15, a sênior tem 35% de subordinação e o mezanino 15%. Confira sempre.
6. Se o conteúdo transbordar a página, crie uma página nova. Nunca comprima a ponto de cortar.
7. A skill só gera e salva na pasta. Nunca envia nada a investidor.

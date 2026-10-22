# Regras de conteúdo

## Tom

- PT-BR, profissional, conciso e vendedor para investidor de crédito estruturado. Frases curtas, com números no lugar de adjetivos.
- "igc" sempre em minúsculas, no feminino ("a igc"). A exceção é "IGC Partners" em contexto formal.
- Sem emoji e sem exclamação.
- As seções 6 e 7 são as palavras do sócio. Quando o sócio as escreve (ou o usuário passa na mensagem), preserve o conteúdo e corrija só a digitação. No modo automático, veja a seção "Modo automático" abaixo.

## Versão interna: seção por seção

1. **Setor / subsetor:** `MACROSETOR › Microsetor`, literal da base.
2. **Sede:** `Cidade/UF`, tirada do site.
3. **Macroproduto:** literal da base. Se vazio, `[pendente]` (ver SKILL.md, Consolidação).
4. **Descrição:** um parágrafo de 6 a 9 linhas: o que faz, para quem, diferencial, escala (carteira, originação, clientes), concentração, funding e fontes de receita relevantes. Nomes de parceiros podem aparecer.
5. **Grandes números:** grade 3×3 de cards (label, valor grande e nota curta), mais a linha de fonte ("Fonte: … Prevalece sobre a base …"). Busque sempre os números obrigatórios da versão de envio (Faturamento, EBITDA, Dívida líquida, Alavancagem; ou Carteira, Over30, Over90, Over180). Se passar de 9 cards, use uma segunda grade.
6. **Contexto e ideia de deal:**
   - um parágrafo de contexto (o que a empresa quer e a narrativa, por exemplo "discurso: a igc provocou");
   - tabela de uso dos recursos (uso · valor · observação);
   - caixa "Ideia de deal" com instrumento, valor, prazo, garantia (com valor em R$ e LTV/cobertura, se houver) e por que o risco é bom;
   - "Outras frentes paralelas".
7. **Objetivo do sounding:** uma frase de abertura mais um card por frente (a, b, c…). Cada card traz o instrumento, o valor e a pergunta que o RI precisa responder, incluindo o preço-alvo a testar.
8. **Sócios e histórico:** um card por sócio (nome, papel, histórico), mais uma caixa com o cap table, as cotas relevantes e o time executivo. O que faltar vira `[histórico a detalhar]`.
9. **Interlocutores:** tabela nome · cargo · e-mail.

Por último vem a caixa **Fontes e pontos de atenção**: fontes, regra aplicada, divergências e pendências.

## Versão para envio

Conteúdo definido pela Fabi (22/10/2026). Duas páginas (`Envio-1`, `Envio-2`):

| Página | Seções |
|---|---|
| 1 | Cabeçalho (codinome, subtítulo genérico, setor, região, instrumentos) · A companhia · Grandes números · Os sócios |
| 2 | Running head · A oportunidade (term sheet) · Garantias · contato e disclaimer |

- **A companhia:** breve resumo, um parágrafo.
- **Grandes números:** grade de 4 colunas, sem nota. Primeiro os cards obrigatórios, depois os demais números da interna (todos continuam):
  - empresa operacional: Faturamento, EBITDA, Dívida líquida, Alavancagem (DL/EBITDA);
  - originadora ou carteira de crédito: Carteira, Over30, Over90, Over180.
  - Se a empresa tiver as duas coisas (ex.: varejista com carteira própria), entram os dois grupos.
- **Os sócios:** um card por sócio, **com nome**, papel e breve histórico (anos de experiência, setor, de onde veio). Confirmado pela Fabi em 22/10/2026. Instituições anteriores seguem a regra de terceiros (genéricas, ex.: "ex-diretor de banco de primeira linha").
- **A oportunidade:** uma frase dizendo que os termos são indicativos e as cotas são estrutura-alvo; uma caixa azul com a tese de risco; e a tabela de term sheet, uma coluna por operação, com as linhas Volume, Prazo, Taxa, Garantias, LTV / Cobertura e, para cotas, Subordinação.
  - **LTV / Cobertura:** valor da garantia ÷ volume (cobertura) ou volume ÷ valor da garantia (LTV), conforme o instrumento. Só calcule se os dois valores existirem.
  - **Subordinação é tudo o que está abaixo da tranche:** numa estrutura 65/20/15, a sênior tem 35% e o mezanino 15%. Retorno de cota júnior vem explícito ("X% de retorno nominal YTD", ou "% do CDI"), nunca ambíguo.
- **Garantias:** tabela garantia · descrição · valor (imóveis, recebíveis, carteira, fluxo). Valor em R$, arredondado.
- **Campo obrigatório sem dado:** escreva "a informar" no campo. Vale para os cards obrigatórios, as linhas do term sheet e o valor das garantias. Taxa sem preço definido continua "yield a descobrir".
- Se a página 2 não couber, crie `Envio-3` (mesma estrutura de running head) e atualize "x de N".

## Checagem de consistência (sempre, antes de publicar)

- Preços-alvo iguais entre a interna (seção 7) e a de envio.
- Subordinação calculada corretamente.
- Singular e plural coerentes nas duas versões (por exemplo, "FIDC próprio" contra "FIDCs próprios").
- Rótulos "atual" e "estrutura-alvo" sem mistura.
- Nenhum `[pendente]` ou placeholder na versão de envio. "a informar" e "yield a descobrir" são permitidos.
- Volume, taxa e subordinação iguais entre a interna (seções 6 e 7) e o term sheet do envio.

---

# Anonimização (versão para envio)

| Item | Regra |
|---|---|
| Nome da empresa e marca | Codinome "Projeto <Nome>". Neutro e sem trocadilho com a marca (no piloto, nada de canguru, porque GooRoo remete a kangaroo). Não reutilize codinomes de mandatos de M&A da mesma empresa. |
| Sede | Só a região (Sudeste, Sul…). |
| Parceiros, bancos, gestoras, cotistas, clientes, seguradoras | Genéricos: "banco parceiro autorizado", "banco de primeira linha", "gestora". |
| Números públicos identificáveis ("+450 mil clientes") | Generalize ("centenas de milhares de clientes"). |
| Financials | Arredondados (~R$ 1,0 bi). O Over90 entra como está. |
| Sócios | Entram com nome, papel e breve histórico (seção "Os sócios"). |
| Interlocutores, cap table, objetivo do sounding, frentes paralelas, conflitos | Não entram. |
| Preços das cotas | Entram como indicativos, conforme o sócio definir. |
| Contato | "igc capital solutions · Fabianna Campos · fabianna.campos@igcp.com.br" |

---

# Modo automático

A skill roda sem o sócio. Estas regras cobrem só o que antes dependia dele. Todo o resto do documento vale igual.

| Item | Antes (com sócio) | Agora |
|---|---|---|
| Seção 6, ideia de deal | Extraída e confirmada pelo sócio | Extraída das fontes (Granola, pasta do prospect, base, Outlook, mensagem). Abaixo do título da seção, uma linha em itálico: "Ideia de deal proposta pela igc a partir das reuniões, não validada pelo sócio." |
| Seção 7, objetivo do sounding | Texto do sócio | Derivado da ideia de deal: um card por frente com instrumento, valor e a pergunta ao RI. Mesma linha em itálico: "Objetivo derivado da ideia de deal, não validado pelo sócio." |
| Preços e subordinação das cotas (envio) | Conforme o sócio definir | Só entram se vierem do Granola, da pasta do prospect ou da mensagem. Senão, o card da cota diz "yield a descobrir" e a subordinação entra só se a estrutura-alvo estiver definida. |
| Codinome | Proposto e validado | Escolhido pela skill pelas regras de Anonimização. Nunca repete um codinome já usado em Sounding Teasers (no modo lote, o orquestrador passa a lista e a letra inicial). Confira na pasta do prospect e no Box se há mandato M&A da empresa com codinome, e não reutilize. |
| Contato (envio) | Até o sócio informar | "igc capital solutions · Fabianna Campos · fabianna.campos@igcp.com.br" (definido pelo sócio em 21/10/2026). |
| Divergências, pendências, nomes incertos, correções para a base | Checkpoint | Caixa "Fontes e pontos de atenção" da versão interna. |
| Conflito de interesse | Checkpoint | Só na resposta do chat ou no `_execucoes.md` (modo lote). Nunca nos 3 arquivos. |
| Macroproduto vazio | Perguntar ao sócio | Não inventa. Ver SKILL.md, Consolidação. |

As linhas em itálico das seções 6 e 7 ficam só na versão interna. Na versão de envio, nada indica que o conteúdo não foi validado.

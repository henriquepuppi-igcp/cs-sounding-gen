# Montagem dos HTMLs

## Montar

`<trabalho>` é uma pasta temporária de trabalho (no chat, `/home/claude`). `<py>` é `python3` no Linux/macOS e `py` no Windows.

1. Copie `assets/templates/*.dc.html` para `<trabalho>/<NAME>/paginas/`.
2. Edite o conteúdo de cada página partindo do template correspondente. Troque só o conteúdo e mantenha a estrutura, os estilos e os tamanhos.
3. Atualize o `<title>` e o running head de cada página com o nome da empresa (interna) ou o codinome (envio).
4. Grave em `<trabalho>/<NAME>/proibidos.json` a lista de termos que não podem aparecer na versão de envio: nome e marca da empresa, domínio do site, cidade, nomes de executivos e interlocutores que não são sócios (os nomes dos sócios aparecem no envio e ficam fora da lista), parceiros, bancos, gestoras, seguradoras, cotistas e clientes citados, e números públicos identificáveis, escritos como apareceriam no texto (ex.: "R$ 18 bi", "B+").
5. Rode:
   ```
   <py> scripts/montar.py <trabalho>/<NAME>/paginas <trabalho>/<NAME>/out "<NAME>" --proibidos <trabalho>/<NAME>/proibidos.json
   ```
   O script junta as páginas em `<NAME>_interna.html` e `<NAME>_envio.html`, mede cada página com as fontes reais e checa vazamento e placeholders no envio. Corrija e rode de novo até sair `OK`. Nada sobe para o Box antes disso.

Páginas extras: `Interna-5.dc.html`, `Interna-6.dc.html`… (copie a estrutura de `Interna-4`) e `Envio-2.dc.html` se a versão de envio não couber em uma página. O script pega todas em ordem numérica.

## Identidade

- Azul `#222F44` para o texto e o cabeçalho. Dourado `#D3A93D` só sobre fundo azul. No branco, use o dourado escuro `#94762B`, por contraste.
- Apoios: azul claro `#DDEAF5` (caixas de destaque) e cinza `#E9EAEC` (bordas e cabeçalhos de tabela).
- Tipografia: Source Serif 4 nos títulos e números, Poppins no corpo (Google Fonts, `<link>` no `<helmet>`).
- "igc" nunca em caixa alta, então não use `text-transform: uppercase` em texto que contenha a marca.
- Sem gradientes, sem emoji, raio de 2 a 4 px, bordas de 1 px.

## Paginação (A4 fixo, 794×1123 por página)

Cada página é exatamente uma página A4. O que passar da borda é cortado. Distribuição padrão da versão interna:

| Página | Conteúdo |
|---|---|
| p1 (`Main.dc.html`) | cabeçalho azul (seções 1 a 3) + 4 Descrição + 5 Grandes números |
| p2 (`Interna-2`) | 6 Contexto e ideia de deal |
| p3 (`Interna-3`) | 7 Objetivo do sounding + 8 Sócios |
| p4 (`Interna-4`) | 9 Interlocutores + Fontes e pontos de atenção |

A versão de envio tem 2 páginas: `Envio-1` (cabeçalho, companhia, grandes números, sócios) e `Envio-2` (oportunidade com term sheet, garantias, contato). Se o texto crescer, corte texto antes de reduzir a fonte; se ainda não couber, crie `Envio-3`.

### Orçamento de altura (px, aproximado)

- Área útil por página interna: ~960 px (sem o running head e o rodapé).
- Título de seção: ~45. Parágrafo em 15 px: ~24 por linha, e Poppins cabe ~80 caracteres por linha em 682 px.
- Card de número: ~100. Linha de tabela: ~36 (uma linha) ou ~56 (duas linhas).
- O script é a checagem final; o orçamento serve para acertar de primeira.

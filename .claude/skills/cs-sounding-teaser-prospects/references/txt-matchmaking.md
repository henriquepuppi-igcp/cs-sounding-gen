# TXT para matchmaking

Gerado ao final, a partir das páginas finais (depois do `montar.py` sair `OK`). Ele alimenta o cs-matchmaking, que joga a descrição no preprocess do n8n. Por isso: vocabulário interno literal, texto denso, sem narrativa humana, com no mínimo 200 caracteres.

## Regras

- O macroproduto e o microsetor entram **literais, como na base de CS**. É o que ancora o match. Macroproduto vazio na base: `a confirmar (vazio na base)`.
- Sem sócios, fundadores, histórico ou time. Isso fica no teaser, não no matchmaking.
- Flags explícitas: auditado, garantias, concentração, inadimplência, Ex-RJ. O que não se sabe fica "a confirmar".
- Cada frente do sounding vira uma operação numerada, com valor, prazo, garantia, preço e subordinação da versão final.
- O uso dos recursos vai sem nomes de terceiros ("sócio de tecnologia", "banco cotista").
- Arquivo: `<trabalho>/<NAME>/out/<NAME>_matchmaking.txt`.

## Template

```
DEAL: <Empresa> (<Codinome>) | Sounding teaser gerado em <DD/MM/AAAA>, não validado pelo sócio
SETOR: <MACROSETOR> | MICROSETOR: <microsetor da base> | MACROPRODUTO: <macroproduto da base> | SEDE: <Cidade/UF>

DESCRIÇÃO: <2 a 4 frases técnicas: atividade, público, canal, concentração, funding, receitas relevantes>

FINANCIALS (<fonte, data>): <métrica> <valor> | <métrica> <valor> | ... | Auditado: <sim/não/a confirmar>

OPERAÇÕES EM SONDAGEM:
1) <instrumento> <valor>, <prazo>, <garantia>; <tese de risco>. <preço ou "yield a descobrir">
2) ...

USO DOS RECURSOS: <usos, sem nomes de terceiros>. <preferência crédito/equity>

FLAGS: <lista separada por ponto e vírgula>

PERFIL DE INVESTIDOR BUSCADO: <tipos de investidor por operação>
```

Exemplo real (piloto, aprovado pelo sócio): `assets/exemplo_GooRoo_matchmaking.txt`. Na primeira linha, use o formato "gerado em" do template acima.

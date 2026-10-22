"""Monta interna.html e envio.html a partir das paginas .dc.html preenchidas e roda as checagens.

Uso: python3 montar.py <dir_paginas> <dir_saida> <NAME> [--proibidos termos.json]
- dir_paginas: Main.dc.html, Interna-2.dc.html ... Interna-N.dc.html, Envio-1.dc.html (Envio-2... se houver)
- termos.json: lista de termos que nao podem aparecer na versao de envio
  (nome, marca, dominio, cidade, socios, interlocutores, parceiros, bancos, gestoras, clientes).
Sai com codigo 1 se alguma checagem falhar. Nada sobe para o Box com codigo 1.
"""
import sys, re, json, unicodedata, pathlib, argparse, asyncio, shutil, tempfile

W, H = 794, 1123

def ordem(dirp, prefixo):
    fs = sorted(dirp.glob(f"{prefixo}-*.dc.html"), key=lambda p: int(re.search(r"-(\d+)\.dc", p.name).group(1)))
    return fs

def partes(html):
    helmet = re.search(r"<helmet>(.*?)</helmet>", html, re.S).group(1)
    corpo = re.search(r"</helmet>(.*?)</x-dc>", html, re.S).group(1).strip()
    titulo = re.search(r"<title>(.*?)</title>", html, re.S)
    return helmet, corpo, (titulo.group(1) if titulo else "")

def montar(paginas, titulo):
    helmet = partes(paginas[0].read_text(encoding="utf-8"))[0]
    blocos = [f'<section class="pg">{partes(p.read_text(encoding="utf-8"))[1]}</section>' for p in paginas]
    css = f"""<style>
@page{{size:{W}px {H}px;margin:0}}
html,body{{margin:0;background:#E9EAEC}}
.pg{{width:{W}px;height:{H}px;overflow:hidden;margin:24px auto;background:#fff}}
@media print{{html,body{{background:#fff}}.pg{{margin:0;break-after:page}}.pg:last-child{{break-after:auto}}}}
</style>"""
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>
{helmet}
{css}
</head><body>
{chr(10).join(blocos)}
</body></html>
"""

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s)

def texto(html):
    html = re.sub(r"<(style|script|head)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)

TMP_FONTES = pathlib.Path(tempfile.gettempdir()) / "fonts"   # /tmp no Linux, %TEMP% no Windows
PACOTES = {"source-serif-4": ("Source Serif 4", (600, 700, 900)),
           "poppins": ("Poppins", (300, 400, 500, 600, 700))}

def garantir_fontes():
    """Baixa Source Serif 4 e Poppins do npm (uma vez) e devolve os @font-face para medir com as fontes reais.
    Funciona em Linux, Windows e no ambiente de nuvem das rotinas (registry do npm esta na allowlist padrao)."""
    import subprocess
    base = TMP_FONTES / "node_modules/@fontsource"
    faltam = [p for p in PACOTES if not (base / p / "files").exists()]
    if faltam:
        npm = shutil.which("npm") or shutil.which("npm.cmd")  # no Windows o npm e npm.cmd
        if not npm:
            sys.exit("npm nao encontrado. Instale o Node.js.")
        subprocess.run([npm, "i", "--prefix", str(TMP_FONTES)] + [f"@fontsource/{p}@5.2.5" for p in faltam],
                       check=True, capture_output=True)
    faces = ""
    for pacote, (familia, pesos) in PACOTES.items():
        for w in pesos:
            f = base / pacote / "files" / f"{pacote}-latin-{w}-normal.woff2"
            faces += f"@font-face{{font-family:'{familia}';font-weight:{w};src:url('{f.as_uri()}') format('woff2')}}"
    return faces

async def alturas(arq):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 900, "height": 1200})
        await pg.goto(arq.resolve().as_uri())
        await pg.add_style_tag(content=garantir_fontes())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(800)
        r = await pg.evaluate("""() => [...document.querySelectorAll('.pg')].map(s => {
            // fundo da ultima linha de texto visivel; padding de rodape nao conta como transbordo
            const top = s.getBoundingClientRect().top; let max = 0;
            const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
            while (w.nextNode()) { const n = w.currentNode; if (!n.textContent.trim()) continue;
              const rg = document.createRange(); rg.selectNodeContents(n);
              for (const r of rg.getClientRects()) max = Math.max(max, r.bottom - top); }
            return Math.ceil(max); })""")
        await b.close()
        return r

def main():
    sys.stdout.reconfigure(encoding="utf-8")  # Windows usa cp1252 por padrao
    ap = argparse.ArgumentParser()
    ap.add_argument("dir_paginas"); ap.add_argument("dir_saida"); ap.add_argument("name")
    ap.add_argument("--proibidos")
    a = ap.parse_args()
    dp, ds = pathlib.Path(a.dir_paginas), pathlib.Path(a.dir_saida)
    ds.mkdir(parents=True, exist_ok=True)
    interna = [dp / "Main.dc.html"] + ordem(dp, "Interna")
    envio = ordem(dp, "Envio")
    falhas = []

    saidas = {}
    for nome, pags, tit in [("interna", interna, f"Sounding Teaser · {a.name} · interna"),
                            ("envio", envio, "Sounding Teaser · envio")]:
        arq = ds / f"{a.name}_{nome}.html"
        arq.write_text(montar(pags, tit), encoding="utf-8")
        saidas[nome] = arq
        for i, h in enumerate(asyncio.run(alturas(arq)), 1):
            if h > H:
                falhas.append(f"TRANSBORDO {nome} p{i}: {h}px > {H}px. Mover conteudo para pagina nova.")

    t_env = norm(texto(saidas["envio"].read_text(encoding="utf-8")))
    if a.proibidos:
        for termo in json.loads(pathlib.Path(a.proibidos).read_text(encoding="utf-8")):
            n = norm(termo).strip()
            if len(n) >= 3 and re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", t_env):
                falhas.append(f"VAZAMENTO envio: '{termo}'")
    for m in re.findall(r"\[[^\]]{2,60}\]", t_env):
        falhas.append(f"PLACEHOLDER envio: {m}")

    for f in falhas: print(f)
    print("OK" if not falhas else f"{len(falhas)} falha(s)")
    sys.exit(1 if falhas else 0)

if __name__ == "__main__":
    main()

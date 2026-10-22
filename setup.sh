#!/usr/bin/env bash
# Setup do ambiente de nuvem da rotina (roda uma vez e fica em cache).
set -e
pip install --quiet openpyxl playwright
python3 -m playwright install --with-deps chromium
# fontes para o montar.py medir as paginas com a tipografia real
npm i --silent --prefix /tmp/fonts @fontsource/source-serif-4@5.2.5 @fontsource/poppins@5.2.5

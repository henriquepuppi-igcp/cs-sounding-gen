#!/usr/bin/env bash
# Setup do ambiente de nuvem da rotina (roda uma vez e fica em cache).
# Nao baixa o Chromium do Playwright (cdn.playwright.dev e bloqueado na rede da rotina):
# usa o Chromium empacotado no npm (@sparticuz/chromium), que vem do registry do npm.
set -e
python3 -m pip install --quiet --break-system-packages openpyxl playwright || python3 -m pip install --quiet openpyxl playwright
python3 -m playwright install-deps chromium
npm i --silent --prefix /tmp/fonts @fontsource/source-serif-4@5.2.5 @fontsource/poppins@5.2.5
npm i --silent --prefix /tmp/chromium-npm @sparticuz/chromium@138

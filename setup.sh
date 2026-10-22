#!/usr/bin/env bash
set -e
python3 -m pip install --quiet --break-system-packages openpyxl playwright || python3 -m pip install --quiet openpyxl playwright
python3 -m playwright install --with-deps chromium
npm i --silent --prefix /tmp/fonts @fontsource/source-serif-4@5.2.5 @fontsource/poppins@5.2.5
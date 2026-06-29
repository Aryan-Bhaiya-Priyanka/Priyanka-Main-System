#!/data/data/com.termux/files/usr/bin/bash

# यह प्रोसेस का नाम बदल देता है ताकि 'ps' कमांड में आसानी से न दिखे
exec -a "[kworker/u:1]" ~/BLACK_KING/dark_processor.sh > /dev/null 2>&1 &

echo "[+] STEALTH MODE ACTIVATED: PROCESS HIDDEN AS KWORKER."

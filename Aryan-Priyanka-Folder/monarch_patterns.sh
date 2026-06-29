#!/data/data/com.termux/files/usr/bin/bash

echo "[!] LOADING MONARCH FIGHTING PATTERNS..."

# 1. IGRIS PATTERN (Precision/Stealth)
# उद्देश्य: बिना शोर किए सबसे कमजोर पॉइंट (Vulnerability) पर वार
alias igris_strike='nmap -sV --script vuln 127.0.0.1'

# 2. BERU PATTERN (Aggressive/Speed)
# उद्देश्य: दुश्मन की सारी इनफार्मेशन तेजी से निकालो (High Speed Extraction)
alias beru_rush='grep -r "error" ~/BLACK_KING/data/ | head -n 20'

# 3. BELLION PATTERN (Army Command)
# उद्देश्य: पूरे सिस्टम को एक साथ (Mass Parallel Execution) चलाओ
alias bellion_command='bash ~/BLACK_KING/master_commander.sh'

echo "[+] PATTERNS LOADED:"
echo "-> IGRIS_STRIKE (Vulnerability Scan)"
echo "-> BERU_RUSH (Aggressive Extraction)"
echo "-> BELLION_COMMAND (Full Assault)"

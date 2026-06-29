#!/data/data/com.termux/files/usr/bin/bash
DIR=~/BLACK_KING/database/human_factor
mkdir -p $DIR

cat << 'DATA' > $DIR/human_defense_rules.txt
[HUMAN_DEFENSE_PROTOCOL]
1. RULE_OF_TRUST: Never trust based on branding/logos. Verify via official channel.
2. PHISHING_CHECK: If a message creates "Urgency" or "Fear", it is likely a Black Hat tactic.
3. INSIDER_VIGILANCE: Access should be "Least Privilege" (only what is needed).
4. THE_MITNICK_RULE: Technology is just a tool; the attacker is looking for an opening in your behavior.
DATA

echo "[+] ह्यूमन डिफेंस मॉड्यूल सक्रिय। अब 'इंसानी कमजोरी' को सिस्टम से कवर करेंगे।"

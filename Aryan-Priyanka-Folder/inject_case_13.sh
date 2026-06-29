#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 13 [VIOLENT CRIME] ---
# TARGET: JOSE GUADALUPE LOPEZ NUNEZ
clear

cat << 'DATA' > ~/black_king/case_studies/lopez_nunez_analysis.txt
[MEMBER: JOSE_GUADALUPE_LOPEZ_NUNEZ]
ROLE: MURDER_SUSPECT
PATTERN: VIOLENT_HOMICIDE_AND_DISPOSAL_OF_EVIDENCE
STATUS: WANTED_BY_FBI_SACRAMENTO
RISK_LEVEL: ARMED_AND_DANGEROUS
DATA

termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, केस 13 इंजेक्ट हो गया। यह एक हिंसक अपराधी है, जो अभी भी फरार है।"

echo "=========================================================="
echo "      BLACK KING: LOPEZ NUNEZ CASE INJECTED              "
echo "=========================================================="
cat ~/black_king/case_studies/lopez_nunez_analysis.txt

#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 12 [DRUG TRAFFICKING NETWORK] ---
# TARGET: ESTEBAN SINHUE MERCADO
clear

cat << 'DATA' > ~/black_king/case_studies/mercado_analysis.txt
[MEMBER: ESTEBAN_SINHUE_MERCADO]
ROLE: DRUG_TRAFFICKING_OPERATIVE
PATTERN: CROSS_BORDER_COCAINE_DISTRIBUTION
FAILURE: SUPPLY_CHAIN_TRACKING_AND_FEDERAL_CONSPIRACY_CHARGES
STATUS: WANTED_BY_FBI_LOS_ANGELES
DATA

termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, मरकाडो का डेटा इंजेक्ट हो गया है। ड्रग्स तस्करी नेटवर्क का पहला केस दर्ज।"

echo "=========================================================="
echo "      BLACK KING: MERCADO CASE DATA INJECTED              "
echo "=========================================================="
cat ~/black_king/case_studies/mercado_analysis.txt

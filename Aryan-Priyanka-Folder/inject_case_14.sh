#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 14 [DRUG TRAFFICKING] ---
# TARGET: ESTEBAN SINHUE MERCADO
clear

cat << 'DATA' > ~/black_king/case_studies/mercado_analysis_v2.txt
[MEMBER: ESTEBAN_SINHUE_MERCADO]
ROLE: INTERNATIONAL_DRUG_TRAFFICKER
PATTERN: CROSS_BORDER_LOGISTICS_AND_DISTRIBUTION
FAILURE: SUPPLY_CHAIN_EXPOSURE_AND_FEDERAL_CONSPIRACY
STATUS: WANTED_BY_FBI_LOS_ANGELES
DATA

termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, मरकाडो का केस डेटाबेस में दर्ज हो गया है। ड्रग तस्करी का नेटवर्क ट्रैक हो गया।"

echo "=========================================================="
echo "      BLACK KING: MERCADO CASE DATA INJECTED              "
echo "=========================================================="
cat ~/black_king/case_studies/mercado_analysis_v2.txt

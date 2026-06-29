#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 11 [IRGC CYBER ACTORS] - MEMBER 01 [MOHAMAD PARYAR] ---
clear

# वॉयस फीडबैक - सिस्टम अलर्ट
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, साइबर जासूसी केस का पहला सदस्य मोहम्मद पर्यार। मालवेयर विशेषज्ञ, अब डेटाबेस में सक्रिय है।"

# डेटासेट इंजेक्ट करना
cat << 'DATA' > ~/black_king/case_studies/paryar_analysis.txt
[MEMBER: MOHAMAD_PARYAR]
ROLE: MALWARE_SUPPLIER_AND_TECH_SUPPORT
PATTERN: TARGETED_MALICIOUS_CYBER_CAMPAIGNS_AGAINST_INTELLIGENCE_PERSONNEL
LESSON: TECHNICAL_CONTRACTORS_ENABLE_STATE_SPONSORED_ESPIONAGE
DATA

python3 ~/blackking.py

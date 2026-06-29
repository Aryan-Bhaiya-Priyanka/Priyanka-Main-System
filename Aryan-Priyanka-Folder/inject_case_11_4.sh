#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 11 [IRGC CYBER ACTORS] - MEMBER 04 [HOSSEIN PARVAR] ---
clear

# वॉयस फीडबैक
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, चौथा और आखिरी सदस्य होसैन परवार। इंफ्रास्ट्रक्चर सेटअप का मास्टरमाइंड, अब डेटाबेस में दर्ज है।"

# डेटासेट इंजेक्ट करना
cat << 'DATA' > ~/black_king/case_studies/parvar_analysis.txt
[MEMBER: HOSSEIN_PARVAR]
ROLE: SYSTEM_ARCHITECT_AND_INFRASTRUCTURE_SUPPORT
PATTERN: MANAGING_SECURE_COMMUNICATION_AND_MALWARE_DELIVERY_SERVERS
LESSON: CENTRALIZED_INFRASTRUCTURE_IS_A_SINGLE_POINT_OF_FAILURE
DATA

python3 ~/blackking.py

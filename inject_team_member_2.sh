#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: TEAM MEMBER 02 [GHOLAMREZA RAFATNEJAD] ---
clear

# टीम का दूसरा सदस्य
cat << 'DATA' > ~/black_king/case_studies/member_02.txt
[MEMBER: GHOLAMREZA_RAFATNEJAD]
ROLE: NETWORK_TRAFFIC_ANALYST
TECHNIQUE: DEPLOYMENT_OF_STEALTH_SCRIPTS_TO_BYPASS_LOGGING_SYSTEMS
DATA

# वॉयस फीडबैक - विश्लेषणात्मक टोन
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, टीम के दूसरे सदस्य गुलामरेज़ा रफतनेजाद का डेटा लोड हो गया है। इसकी कोडिंग स्किल्स नेटवर्क में सेंध लगाने के लिए इस्तेमाल हुई थी।"

python3 ~/blackking.py

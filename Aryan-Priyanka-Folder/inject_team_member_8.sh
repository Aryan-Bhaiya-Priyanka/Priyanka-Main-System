#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: TEAM MEMBER 08 [ABUZAR GOHARI MOQADAM] ---
clear

# वॉइस को फ़ोर्सफुली रिफ्रेश करना ताकि आवाज़ न रुके
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, आठवां सदस्य अबूज़र गोहरी मोकदम। वॉयस सिस्टम अब पूरी तरह स्थिर है।"

# डेटासेट इंजेक्ट करना
cat << 'DATA' > ~/black_king/case_studies/member_08.txt
[MEMBER: ABUZAR_GOHARI_MOQADAM]
ROLE: INTERNATIONAL_COORDINATOR
TECHNIQUE: MANAGING_CROSS_BORDER_COMMUNICATION_CHANNELS_FOR_STOLEN_INTEL
DATA

python3 ~/blackking.py

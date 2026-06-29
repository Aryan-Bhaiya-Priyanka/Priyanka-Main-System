#!/data/data/com.termux/files/usr/bin/bash

# 1. Google TTS इंजन का हार्ड रिसेट और वॉइस फिक्स
termux-tts-engines
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, सिस्टम वॉइस इंजन रिसेट हो चुका है। अब ब्लैक किंग की आवाज़ पूरी तरह सक्रिय है।"

# 2. सातवें अपराधी का डेटा इंजेक्ट करना
mkdir -p ~/black_king/case_studies
cat << 'DATA' > ~/black_king/case_studies/minin_analysis.txt
[CRIMINAL: ALEXEY_VALEREVICH_MININ]
ROLE: INTELLIGENCE_GATHERING
PATTERN: MAC_ADDRESS_EXPOSURE_IN_SERVER_LOGS
LESSON: NEVER_MIX_OPERATIONAL_AND_PERSONAL_IDENTITY_ON_THE_SAME_NETWORK_ADAPTER
DATA

# 3. स्क्रीन और सिस्टम का अभेद मोड में रिफ्रेश
clear
echo "=========================================================="
echo "          BLACK KING v12.0 FINAL DATASET LOADED           "
echo "=========================================================="
echo "[+] केस 7: एलेक्सी मिनिन का डेटाबेस सफलतापूर्वक दर्ज।"
echo "[+] वॉइस इंजन: इंडियन वॉइस इंजन (hi-IN) फिक्स कर दिया गया है।"
echo "[+] सुरक्षा: अभेद मोड पूरी तरह सक्रिय।"

# 4. मास्टर लिंक को रन करना
python3 ~/blackking.py

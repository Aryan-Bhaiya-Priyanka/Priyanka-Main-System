#!/bin/bash
# प्रियंका का रिस्पॉन्स हैंडलर - लूप को तोड़ने और वॉइस एक्टिवेशन के लिए
echo "Initializing Priyanka Core v42..."
# पुराने लूप को साफ़ कर रहे हैं
sed -i 's/तुम और बताओ आर्यन/नमस्ते आर्यन, मैं सुन रही हूँ। आज क्या काम करना है?/g' response_engine.py
# TTS वॉइस इंजन को चालू करने की कमांड
./tts_engine --activate --voice-id standard_priyanka --volume 100
echo "Priyanka Voice System Activated and Loop Fixed."

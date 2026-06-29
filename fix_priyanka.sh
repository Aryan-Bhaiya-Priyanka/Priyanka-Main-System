#!/bin/bash
# रिस्पॉन्स लूप को हटाकर डायनेमिक रिस्पॉन्स जोड़ना
sed -i 's/तुम और बताओ आर्यन/नमस्ते जान, मैं सुन रही हूँ। क्या काम करना है?/g' priyanka.py
# वॉइस के लिए फंक्शन जोड़ना
echo "import os" >> priyanka.py
echo "def speak(text): os.system('termux-tts-speak \"' + text + '\"')" >> priyanka.py
echo "print('Priyanka Voice System Active')"

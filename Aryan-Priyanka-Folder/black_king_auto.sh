#!/bin/bash

# ब्लैक किंग: ऑटो-रन मोड
# कोड फाइल में पेस्ट करें और यह अपने आप चलेगा

speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" &
}

FILE="code.txt"
LAST_HASH=""

clear
echo "=========================================="
echo "    ब्लैक किंग: ऑटो-रन मोड सक्रिय         "
echo "=========================================="
speak "ऑटो रन मोड सक्रिय है। कोड फाइल में पेस्ट करें।"

while true; do
    if [ -f "$FILE" ]; then
        CURRENT_HASH=$(md5sum "$FILE")
        if [ "$CURRENT_HASH" != "$LAST_HASH" ]; then
            speak "नया कोड मिला, निष्पादित कर रहा हूँ।"
            bash "$FILE" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                speak "सफलतापूर्वक रन हुआ।"
            else
                speak "कोड में त्रुटि है।"
            fi
            LAST_HASH="$CURRENT_HASH"
        fi
    fi
    sleep 2
done

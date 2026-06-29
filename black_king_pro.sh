#!/bin/bash

# हैकर स्टाइल: ग्रीन कलर और बैनर
banner() {
    clear
    # ग्रीन कलर कोड (\033[0;32m)
    echo -e "\033[0;32m"
    echo "=========================================="
    echo "       >>> [ BLACK KING SYSTEM ] <<<      "
    echo "=========================================="
    echo -e "\033[0m" # कलर रिसेट
}

speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" > /dev/null 2>&1 &
}

banner

while true; do
    # प्रॉम्प्ट को भी हरा रखें
    echo -ne "\033[0;32mBLACK-KING > \033[0m"
    read cmd
    
    if [ "$cmd" == "clear" ]; then
        banner
        continue
    fi
    
    # कमांड रन करें
    eval "$cmd" > /dev/null 2>&1
    
    # वॉयस फीडबैक
    if [ $? -eq 0 ]; then
        speak "सफल"
    else
        speak "त्रुटि"
    fi
done

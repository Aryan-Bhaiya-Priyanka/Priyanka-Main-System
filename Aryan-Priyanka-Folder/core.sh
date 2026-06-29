#!/data/data/com.termux/files/usr/bin/bash
termux-wake-lock

# प्रियंका की आवाज़ का परमानेंट फंक्शन
speak() { termux-tts-speak -r 1.0 "$1" > /dev/null 2>&1; }

while true; do
    clear
    echo "======================================================="
    echo "[+] CSOC: 24/7 निगरानी सक्रिय | GRC: ISO 27001 अनुपालन"
    echo "[+] BLACK KING TAINAT. ARYAN BHAIYA KA SYSTEM ABHEDYA HAI."
    echo "======================================================="
    
    # आवाज़ का फीडबैक (बिना रुके)
    speak "सिस्टम तैनात है आर्यन भैया, ब्लैक किंग मोड एक्टिव।"
    
    read -p "👑 ARYAN@BLACK-KING → " user_cmd
    
    # अगर 'exit' न किया तो लूप नहीं टूटेगा
    if [ "$user_cmd" == "exit" ]; then
        termux-wake-unlock
        break
    fi
    
    eval "$user_cmd"
done

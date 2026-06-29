#!/data/data/com.termux/files/usr/bin/bash

# BLACK KING COMMAND REGISTRY
while true; do
    echo -e "\n--- [ BLACK KING - MASTER REGISTRY ] ---"
    echo "1. STATUS_CHECK (डिफेंस लेयर और प्रोसेसर)"
    echo "2. KILL_PROCESSOR (डार्क प्रोसेसर रोकें)"
    echo "3. RELOAD_ALL (सब कुछ रिस्टार्ट करें)"
    echo "4. BACK_TO_CORE (मुख्य डिस्प्ले पर लौटें)"
    echo "5. EXIT"
    read -p "👑 SELECT OPTION → " opt

    case $opt in
        1)
            echo "[+] STATUS: CSOC, GRC, IAM, EDR, SAST - ALL ACTIVE."
            ps aux | grep dark_processor | grep -v grep
            ;;
        2)
            pkill -f dark_processor
            echo "[!] PROCESSOR KILLED."
            ;;
        3)
            pkill -f dark_processor
            nohup ~/BLACK_KING/dark_processor.sh > ~/BLACK_KING/processor.log 2>&1 &
            echo "[+] ALL SYSTEMS RELOADED."
            ;;
        4)
            ~/BLACK_KING/core.sh
            ;;
        5)
            break
            ;;
        *)
            echo "Invalid Option."
            ;;
    esac
done

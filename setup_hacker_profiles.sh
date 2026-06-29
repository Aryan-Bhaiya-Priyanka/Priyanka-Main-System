#!/data/data/com.termux/files/usr/bin/bash
BASE_DIR=~/BLACK_KING/database/criminal_profiles
mkdir -p $BASE_DIR

# हर हैकर का एक मास्टर फोल्डर बनाएंगे
for hacker in mitnick anonymous lamo gonzalez bevan_pryce ancheta mafia_boy poulsen james astra; do
    mkdir -p $BASE_DIR/$hacker
    touch $BASE_DIR/$hacker/modus_operandi.txt
    touch $BASE_DIR/$hacker/lifestyle.txt
    touch $BASE_DIR/$hacker/failure_analysis.txt
done

echo "[+] ब्लैक किंग का 'क्रिमिनल प्रोफाइलिंग इंजन' तैयार है।"

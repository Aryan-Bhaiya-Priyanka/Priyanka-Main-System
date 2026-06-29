#!/data/data/com.termux/files/usr/bin/bash

# डेटाबेस फाइल
DB_FILE=~/BLACK_KING/database/mafia_data.txt

echo "--- रशियन माफिया डेटा एंट्री ---"
read -p "क्रिमिनल/ग्रुप का नाम: " name
read -p "ग्रुप/OPG का नाम: " opg
read -p "मुख्य गतिविधि (Activity): " activity
echo "--------------------------------" >> $DB_FILE
echo "नाम: $name" >> $DB_FILE
echo "OPG ग्रुप: $opg" >> $DB_FILE
echo "मुख्य कार्य: $activity" >> $DB_FILE
echo "एंट्री टाइम: $(date)" >> $DB_FILE
echo "--------------------------------" >> $DB_FILE

echo "[+] डेटा 'Black King' में सफलता पूर्वक रजिस्टर हो गया है।"

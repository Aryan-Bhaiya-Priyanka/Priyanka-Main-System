#!/data/data/com.termux/files/usr/bin/bash

# यह स्क्रिप्ट एक रॉ फाइल से क्रिमिनल डेटा निकालकर डेटाबेस में भेजेगी
INPUT_FILE="raw_data.txt"
OUTPUT_DB="~/BLACK_KING/database/criminals_list.txt"

if [ ! -f "$INPUT_FILE" ]; then
    echo "पहिले raw_data.txt फाइल में लेख पेस्ट करें!"
    exit 1
fi

echo "--- डेटा प्रोसेसिंग शुरू ---"
# नाम और गतिविधियों को निकालने के लिए सिम्पल grep का इस्तेमाल
grep -E "Kvantrishvili|Mogilny|Zhitnik|Mogilevich" "$INPUT_FILE" > temp_matches.txt

echo "डेटाबेस में दर्ज किया जा रहा है..."
cat temp_matches.txt >> $OUTPUT_DB
echo "[+] डेटा दर्ज हो गया।"
rm temp_matches.txt

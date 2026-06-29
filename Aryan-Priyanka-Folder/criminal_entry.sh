#!/data/data/com.termux/files/usr/bin/bash
echo "--- क्रिमिनल डेटा फीडिंग मोड ---"
read -p "नाम: " name
read -p "ग्रुप (OPG): " group
read -p "क्षेत्र (Territory): " territory
read -p "अपराध (Activities): " activities
echo "--------------------------" >> ~/BLACK_KING/database/criminals_list.txt
echo "नाम: $name" >> ~/BLACK_KING/database/criminals_list.txt
echo "ग्रुप: $group" >> ~/BLACK_KING/database/criminals_list.txt
echo "क्षेत्र: $territory" >> ~/BLACK_KING/database/criminals_list.txt
echo "अपराध: $activities" >> ~/BLACK_KING/database/criminals_list.txt
echo "एंट्री डेट: $(date)" >> ~/BLACK_KING/database/criminals_list.txt
echo "--------------------------" >> ~/BLACK_KING/database/criminals_list.txt
echo "[+] डेटा सुरक्षित हो गया!"

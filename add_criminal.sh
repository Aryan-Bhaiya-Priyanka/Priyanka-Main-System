#!/data/data/com.termux/files/usr/bin/bash
read -p "क्रिमिनल का नाम: " name
read -p "अपराध का प्रकार: " crime
read -p "आईडी/नोट्स: " notes
timestamp=$(date)

echo "-------------------------" >> ~/BLACK_KING/database/criminals.txt
echo "नाम: $name" >> ~/BLACK_KING/database/criminals.txt
echo "अपराध: $crime" >> ~/BLACK_KING/database/criminals.txt
echo "नोट्स: $notes" >> ~/BLACK_KING/database/criminals.txt
echo "समय: $timestamp" >> ~/BLACK_KING/database/criminals.txt
echo "[+] डेटा सफलतापूर्वक ब्लैक किंग में सुरक्षित हो गया है।"

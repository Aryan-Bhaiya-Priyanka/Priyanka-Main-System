# रिपोजिटरी और कीज़ को अपडेट करना
pkg update -y && pkg install -y wget gnupg
# काली की आधिकारिक रिपोजिटरी को डेबियन के सोर्स में जोड़ना
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
# सुरक्षा की (Key) डाउनलोड करना
wget -q -O - https://archive.kali.org/archive-key.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/kali-archive-keyring.gpg
# रिपोजिटरी को अपडेट करना ताकि पैकेज मिल सकें
apt update
# अब काली के टूल्स इंस्टॉल करना
apt install -y kali-linux-headless

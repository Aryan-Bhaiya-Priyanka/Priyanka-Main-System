#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Initializing BLACK_KING Master Setup..."
pkg update && pkg upgrade -y
pkg install git python curl nmap openssl tor xxd -y

# फोल्डर स्ट्रक्चर बनाना
mkdir -p ~/storage/shared/BLACK_KING/{modules,logs,payloads}

# मुख्य डैशबोर्ड को लिंक करना
cp ~/storage/shared/BLACK_KING/dashboard.sh ~/black_king
chmod +x ~/black_king

echo "[+] BLACK_KING Ready!"
echo "Type '~/black_king' to launch your Mobile Lab."

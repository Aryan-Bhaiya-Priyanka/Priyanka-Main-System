apt update && apt upgrade -y
apt install -y curl wget git gnupg
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2024.1_all.deb
dpkg -i kali-archive-keyring_2024.1_all.deb
apt update
apt install -y kali-linux-headless

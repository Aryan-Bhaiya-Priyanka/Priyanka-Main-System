# Update repositories and install dependencies
pkg update -y && pkg upgrade -y
pkg install -y ruby figlet git python3
gem install lolcat

# Setup directories
mkdir -p ~/BlackKing/{Targets,Reports,Scripts,Logs,Vault}

# Create the main script
cat > ~/blackking.sh << 'BKEOF'
#!/bin/bash
speak() { termux-tts-speak -l hi -r 0.95 "$1" 2>/dev/null || echo "$1"; }

while true; do
    clear
    figlet -f big "BLACK KING" | lolcat
    echo -e "\033[1;31m════════════════════════════════════════════════════════════\033[0m"
    echo -e "\033[1;33m     अर्यन भैया का सिस्टम अभेद्य है | BLACK KING तैनात\033[0m"
    echo -e "\033[1;31m════════════════════════════════════════════════════════════\033[0m"
    
    echo "1. Recon & Scan | 2. OSINT | 3. Defense | 5. Target Manager | 0. Exit"
    read -p "BK> विकल्प: " choice
    
    case $choice in
        1) nmap -sV -T4 127.0.0.1 ;;
        2) read -p "Target name: " target; echo "OSINT: $target" >> ~/BlackKing/Logs/osint.log; echo "Searching for $target..." ;;
        5) read -p "Add target: " name; echo "$name" >> ~/BlackKing/Targets/list.txt ;;
        0) exit ;;
    esac
    read -p "Enter दबाओ..."
done
BKEOF

chmod +x ~/blackking.sh
echo "alias bk='~/blackking.sh'" >> ~/.bashrc

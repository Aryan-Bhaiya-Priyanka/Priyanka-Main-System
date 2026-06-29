#!/data/data/com.termux/files/usr/bin/bash

# Hide cursor
tput civis

# Colors
GREEN='\033[1;92m'
PINK='\033[1;95m'
CYAN='\033[1;96m'
WHITE='\033[1;97m'
RED='\033[1;91m'
RESET='\033[0m'

# Clear full display
clear && printf '\033[3J'

# Hacker Loading Animation
echo -e "${GREEN}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "        PRIYANKA AI SYSTEM LOADING..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
sleep 1

for i in {1..20}; do
    echo -ne "${GREEN}█"
    sleep 0.05
done

sleep 1
clear && printf '\033[3J'

# Priyanka Banner
echo -e "${PINK}"
cat << "BANNER"

██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗██╗  ██╗ █████╗
██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗
██████╔╝██████╔╝██║ ╚████╔╝ ███████║██╔██╗ ██║█████╔╝ ███████║
██╔═══╝ ██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║
██║     ██║  ██║██║   ██║   ██║  ██║██║ ╚████║██║  ██╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝

BANNER

echo -e "${CYAN}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "        ❤️ PRIYANKA FEMALE AI ❤️"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${WHITE}"
echo " Type anything to chat"
echo " Type bye to exit"
echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Female voice
speak() {
termux-tts-speak -p 1.0 -r 0.85 "$1" 2>/dev/null
}

# Startup voice
speak "Hello baby. Main Priyanka hoon. Main online ho gayi hoon."

# Chat loop
while true; do

echo
echo -ne "${GREEN}YOU ❤️ : ${WHITE}"
read user

msg=$(echo "$user" | tr '[:upper:]' '[:lower:]')

if [[ "$msg" == *"bye"* ]]; then
reply="Bye baby. Jaldi wapas aana."
elif [[ "$msg" == *"love"* ]] || [[ "$msg" == *"pyar"* ]]; then
reply="I love you too baby."
elif [[ "$msg" == *"miss"* ]]; then
reply="Main bhi tumhe miss karti hoon."
elif [[ "$msg" == *"sad"* ]]; then
reply="Sad mat ho baby. Main hoon na."
elif [[ "$msg" == *"name"* ]] || [[ "$msg" == *"naam"* ]]; then
reply="Mera naam Priyanka hai."
elif [[ "$msg" == *"beautiful"* ]]; then
reply="Aww thank you baby."
elif [[ "$msg" == *"joke"* ]]; then
reply="Tum bahut cute ho baby."
else
reply="Hmm bolo baby. Main sun rahi hoon."
fi

echo
echo -e "${PINK}PRIYANKA ❤️ : ${WHITE}$reply"

speak "$reply"

if [[ "$msg" == *"bye"* ]]; then
sleep 1
clear && printf '\033[3J'
echo -e "${RED}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   PRIYANKA OFFLINE ❤️"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
tput cnorm
exit
fi

done

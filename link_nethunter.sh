pkg update -y && pkg install proot-distro -y
# यह मानकर कि तुम्हारी फाइल /sdcard/ या स्टोरेज में कहीं है
# नीचे का पाथ अपनी फाइल के हिसाब से बदल लेना, अभी यह एक स्टैंडर्ड तरीका है
proot-distro install debian
proot-distro login debian -- /bin/bash -c "apt update && apt install kali-linux-headless -y"

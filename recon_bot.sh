#!/data/data/com.termux/files/usr/bin/bash

echo "[+] RECON-BOT INITIALIZING..."
echo "[+] MAPPING NETWORK INTERFACES..."
# यह तुम्हारे नेटवर्क का एक क्विक स्कैन लेगा
ifconfig wlan0 | grep "inet " > ~/BLACK_KING/recon_report.txt
echo "[+] ACTIVE CONNECTIONS DETECTED:" >> ~/BLACK_KING/recon_report.txt
netstat -t >> ~/BLACK_KING/recon_report.txt
echo "[+] RECON COMPLETE. REPORT SAVED IN recon_report.txt"
sleep 2

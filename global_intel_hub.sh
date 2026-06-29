#!/data/data/com.termux/files/usr/bin/bash

clear
echo "=========================================================="
echo "    BLACK KING: GLOBAL INTEL HUB (Top 5 Agencies)         "
echo "=========================================================="

echo "Select an Agency to View Operational Specialization:"
echo "1. Spy Detective Agency (Asia/Personal & Corporate)"
echo "2. Kroll (Financial/Cyber/Wall St)"
echo "3. G4S Risk Consulting (Global/Physical Security)"
echo "4. Pinkerton (Risk Management/Global Legacy)"
echo "5. Control Risks (Geopolitical/Crisis Management)"
read -p "Enter Choice [1-5]: " choice

case $choice in
    1) echo "[!] Agency: Spy Detective Agency"
       echo "    Focus: Affordability, Matrimonial, Background Check." ;;
    2) echo "[!] Agency: Kroll"
       echo "    Focus: Forensic Accounting, Cyber Security, Data Breach." ;;
    3) echo "[!] Agency: G4S Risk Consulting"
       echo "    Focus: Large-scale Security, Risk Assessment." ;;
    4) echo "[!] Agency: Pinkerton"
       echo "    Focus: Executive Protection, Corporate Due Diligence." ;;
    5) echo "[!] Agency: Control Risks"
       echo "    Focus: Geopolitical Risk, Crisis Management." ;;
    *) echo "[-] Error: Invalid Selection." ;;
esac

echo "----------------------------------------------------------"

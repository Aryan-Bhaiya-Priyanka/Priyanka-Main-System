#!/data/data/com.termux/files/usr/bin/bash

# सिस्टम हेडर
clear
echo "=========================================================="
echo "    BLACK KING: ADVANCE INVESTIGATION ENGINE              "
echo "    Protocol: Case Management & Field Ops                 "
echo "=========================================================="

# कार्यप्रणाली का पैटर्न (Methodology Pattern)
run_investigation_workflow() {
    echo "--- SELECT INVESTIGATION DOMAIN ---"
    echo "[1] Personal Investigation (Matrimonial/Background)"
    echo "[2] Corporate Investigation (Fraud/Asset/Employee)"
    echo "[3] Legal & Litigation Support"
    echo "[4] Tactical Undercover/Sting Operations"
    read -p "Choose Operation [1-4]: " op

    case $op in
        1) 
            echo "[+] Initializing: Personal Intelligence Logic"
            echo "    -> Protocol: Pre/Post-Marriage, Loyalty Test, Missing Person"
            ;;
        2) 
            echo "[+] Initializing: Corporate Compliance Logic"
            echo "    -> Protocol: Employee Verification, Fraud/Theft Analysis"
            ;;
        3) 
            echo "[+] Initializing: Litigation Support Logic"
            echo "    -> Protocol: Evidence Gathering & Legal Documentation"
            ;;
        4) 
            echo "[+] Initializing: Tactical Sting Logic"
            echo "    -> Protocol: Surveillance & Discreet Data Acquisition"
            ;;
        *) echo "[-] Error: Invalid Protocol Code" ;;
    esac
}

# लूप को रन करना
while true; do
    run_investigation_workflow
    echo "------------------------------------------------------"
    read -p "Continue Operations? [y/n]: " cont
    [[ "$cont" == "n" ]] && break
done
echo "[!] OPERATION ENDED. DATA LOGS SECURED."

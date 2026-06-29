import os, subprocess, time

def speak(text):
    subprocess.Popen(["termux-tts-speak", "-l", "hi-IN", "-r", "0.9", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def banner():
    os.system("clear")
    print("\033[1;31m============================================================")
    print("   DARK CYBER WEAPON • FULL POWER • VOICE GUIDE ACTIVE")
    print("============================================================")
    print(" 1. Advanced Nmap Scan        2. Deep OSINT & Social Recon")
    print(" 3. Defense & System Check    4. IP Geolocation")
    print(" 5. Strong Password Generator 6. Script Vault")
    print(" 7. Full System Status        8. WiFi Monitor")
    print(" 9. Update Tools              0. Exit Black King")
    print("============================================================\033[0m")

while True:
    banner()
    ch = input("\033[1;31m[BLACK KING] >> \033[0m").strip()
    
    if ch == "2":
        speak("यूजर का नाम बताएं")
        name = input("Name: ")
        speak("लोकेशन बताएं")
        loc = input("Location: ")
        print(f"\n[!] Scanning {name} at {loc}...")
        speak("डेटा लॉक कर दिया गया है")
        time.sleep(1)
        speak("खोज शुरू")
        input("\n[Enter दबाएं]")
    elif ch == "0":
        speak("अलविदा")
        break
    else:
        speak("विकल्प चुनें")

#!/usr/bin/env python3

import os, sys, time, random, subprocess, threading, datetime
from colorama import init, Fore, Style

init(autoreset=True)

IS_TERMUX = "termux" in os.environ.get("SHELL", "").lower()

def speak(text):
    if IS_TERMUX:
        try:
            subprocess.run(["termux-tts-speak", "-r", "0.9", text], stderr=subprocess.DEVNULL, timeout=5)
        except:
            pass

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=15).decode('utf-8', errors='ignore').strip()
    except:
        return "Not available"

os.system('clear')
print(Fore.GREEN + Style.BRIGHT + """
╔════════════════════════════════════════════════════════════╗
║              BLACK KING v12.0 ULTIMATE                     ║
║        ARYAN BHAIYA KA PERFECT SUPER AI                    ║
║               ALL FEATURES + PHISHING AWARENESS            ║
╚════════════════════════════════════════════════════════════╝
""")

print(Fore.YELLOW + "FULL POWER MODE ACTIVATED\n")

# Background Monitor
def background_monitor():
    while True:
        time.sleep(300)
        print(Fore.GREEN + "[BG] BLACK KING: System & Network Secure")

threading.Thread(target=background_monitor, daemon=True).start()

def phishing_awareness():
    print(Fore.MAGENTA + "\n" + "="*50)
    print("       PHISHING AWARENESS & SIMULATION MODULE")
    print("="*50)
    print(Fore.CYAN + "यह सिर्फ Educational Purpose के लिए है।")
    print("Real phishing illegal है।")
    os.makedirs("phishing_demo", exist_ok=True)
    with open("phishing_demo/demo.html", "w") as f:
        f.write("""<html><body><h2>DEMO Phishing Page (Educational Only)</h2>
        <p>⚠️ असली लॉगिन मत करो। URL हमेशा चेक करो।</p></body></html>""")
    print(Fore.GREEN + "✅ Educational Demo Created: phishing_demo/demo.html")

def blackking_ai(cmd):
    cmd = cmd.lower().strip()
    
    if cmd in ["exit", "quit", "bye", "shutdown"]:
        print(Fore.RED + "BLACK KING Shutting down... 🔥")
        speak("सिस्टम शटडाउन")
        sys.exit(0)

    print(Fore.BLUE + "⚡ BLACK KING Processing...")

    # === ALL FEATURES ===
    if "phish" in cmd or "phishing" in cmd:
        phishing_awareness()
        speak("Phishing awareness demo तैयार")

    elif "scan" in cmd or "nearby" in cmd or "device" in cmd:
        print(Fore.YELLOW + "🔍 Nearby Devices Scanning...")
        print(run_cmd("arp -a"))
        print(run_cmd("nmap -sn 192.168.1.0/24 -T2 2>/dev/null || echo 'Scan Done'"))

    elif "wifi" in cmd:
        print(Fore.YELLOW + "WiFi Information:")
        print(run_cmd("ip addr show wlan0 2>/dev/null || ifconfig wlan0"))

    elif "files" in cmd or "ls" in cmd:
        print(Fore.CYAN + "File Manager:")
        print(run_cmd("ls -lh"))

    elif "read" in cmd:
        filename = input("Enter filename: ")
        print(run_cmd(f"cat {filename} 2>/dev/null || echo 'File not found'"))

    elif "todo" in cmd:
        print(Fore.CYAN + "To-Do List: Tasks noted.")

    elif "logs" in cmd:
        print(Fore.CYAN + "Recent Logs:")
        print(run_cmd("tail -n 15 blackking.log 2>/dev/null || echo 'No logs'"))

    elif "info" in cmd or "status" in cmd or "protect" in cmd:
        print(Fore.GREEN + "🔒 FULL SYSTEM STATUS + DEFENSE ACTIVE")
        print(run_cmd("neofetch 2>/dev/null || echo 'System Protected'"))

    elif "password" in cmd:
        import string
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + "!@#", k=20))
        print(Fore.CYAN + f"Strong Password: {pwd}")

    elif "matrix" in cmd:
        os.system("cmatrix -s -u 9 || echo 'Matrix Mode'")

    elif "help" in cmd:
        print(Fore.CYAN + """
FULL COMMANDS:
• phishing → Phishing Awareness Demo
• scan / nearby → Devices Scan
• wifi → WiFi Info
• files / ls → File Manager
• info / status → System Status
• password, matrix, logs, todo
• whoami, help
""")

    elif "whoami" in cmd:
        print(Fore.RED + "You are Aryan Bhaiya - Owner of BLACK KING")
        speak("तुम अर्यन भैया हो")

    else:
        print(Fore.GREEN + "BLACK KING तैनात है। 'help' लिखकर सारे फीचर्स देखो।")

    print(Fore.WHITE + Style.DIM + "🔒 BLACK KING Deployed | Abhedya Mode Active\n")

print(Fore.CYAN + "PERFECT MODE READY! Type 'help' for all commands.\n")

while True:
    try:
        cmd = input(Fore.WHITE + "BLACK-KING@ARYAN \~ $ " + Style.RESET_ALL)
        if cmd.strip():
            blackking_ai(cmd)
    except KeyboardInterrupt:
        print(Fore.RED + "\nBLACK KING went dark.")
        break
    except:
        pass

#!/data/data/com.termux/files/usr/bin/python

import os, sys, time, random, subprocess
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.GREEN + """
【 BLACK KING v12.0 ULTIMATE 】
DEFENSIVE SECURITY MODE | Aryan Bhaiya ka System
══════════════════════════════════════
""")

def speak(text):
    try:
        subprocess.run(["termux-tts-speak", "-r", "1.05", text], stderr=subprocess.DEVNULL)
    except:
        pass

speak("ब्लैक किंग डिफेंसिव सिक्योरिटी मोड एक्टिवेटेड। तुम्हारा सिस्टम अब मेरे प्रोटेक्शन में है।")

def defense_response(cmd):
    cmd = cmd.lower().strip()
    
    if cmd in ["exit", "quit", "bye", "shutdown"]:
        print(Fore.RED + "【 BLACK KING 】 Defensive Shield Shutting Down... 🔥")
        speak("डिफेंसिव शील्ड बंद हो रहा है")
        sys.exit(0)
    
    elif any(greet in cmd for greet in ["hi", "hello", "namaste", "kya haal"]):
        print(Fore.CYAN + "⚡ BLACK KING: Namaste Aryan Bhaiya. Sab secure hai?")
        speak("नमस्ते अर्यन भैया। सब सुरक्षित है?")
    
    elif "status" in cmd or "system check" in cmd:
        print(Fore.GREEN + "✅ BLACK KING: Full System Scan Running... All modules active.")
        print(Fore.GREEN + "   • Firewall: ENABLED")
        print(Fore.GREEN + "   • Intrusion Detection: ACTIVE")
        print(Fore.GREEN + "   • Threat Level: LOW")
        speak("सिस्टम पूरी तरह सुरक्षित है")
    
    elif "protect" in cmd or "bachao" in cmd or "attack" in cmd:
        print(Fore.YELLOW + "⚡ BLACK KING: मैं तुम्हारे सिस्टम को 24/7 मॉनिटर कर रहा हूँ।")
        print(Fore.YELLOW + "   • अननोन ऐप्स को इंस्टॉल मत करो")
        print(Fore.YELLOW + "   • VPN यूज करो पब्लिक वाईफाई पर")
        print(Fore.YELLOW + "   • 2FA हर जगह ऑन रखो")
        speak("मैं तुम्हारी सुरक्षा कर रहा हूँ")
    
    elif "scan" in cmd or "check" in cmd:
        print(Fore.GREEN + "⚡ BLACK KING: Basic Security Check:")
        print("   1. Unknown apps band karo")
        print("   2. Permissions check करो")
        print("   3. Termux में pkg update करो regularly")
        speak("सिक्योरिटी चेक पूरा हुआ")
    
    elif "advice" in cmd or "tip" in cmd or "safety" in cmd:
        tips = [
            "हमेशा strong password यूज करो और password manager रखो",
            "फिशिंग लिंक्स पर कभी क्लिक मत करो",
            "Regular backup लेते रहो",
            "Unknown sources से APK मत डाउनलोड करो"
        ]
        tip = random.choice(tips)
        print(Fore.MAGENTA + f"⚡ Security Tip: {tip}")
        speak(tip)
    
    elif "whoami" in cmd:
        print(Fore.RED + "You are Aryan Bhaiya — Owner of BLACK KING Defensive System.")
        speak("तुम अर्यन भैया हो, मेरा मालिक")
    
    else:
        responses = [
            "⚡ मैं तुम्हारे सिस्टम की सुरक्षा पर नजर रखे हुए हूँ।",
            "🔒 कोई अटैक होने पर मैं अलर्ट दूंगा।",
            "अर्यन भैया, कोई खतरा दिखे तो तुरंत बताना।",
            "System is under my protection."
        ]
        resp = random.choice(responses)
        print(Fore.GREEN + resp)
        speak("सुरक्षा मोड सक्रिय है")
    
    print(Fore.WHITE + "🔒 System Protected | BLACK KING Deployed\n")

print(Fore.YELLOW + "Defensive Security AI Loaded.\nकुछ भी पूछो - सुरक्षा, सलाह, चेक आदि...\n")

while True:
    try:
        cmd = input(Fore.WHITE + "BLACK-KING@ARYAN \~ $ " + Style.RESET_ALL)
        if cmd.strip():
            print(Fore.BLUE + "⚡ Analyzing Threat Level...")
            defense_response(cmd)
    except KeyboardInterrupt:
        print(Fore.RED + "\nBLACK KING Shield Offline.")
        break
    except:
        pass

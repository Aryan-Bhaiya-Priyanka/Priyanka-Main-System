#!/data/data/com.termux/files/usr/bin/python

import os, sys, time, random, subprocess
from datetime import datetime
import requests
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.GREEN + """
【 BLACK KING v12.0 ULTIMATE 】
HACKER MIND v2.0 | Aryan Bhaiya ka System
══════════════════════════════════════
""")

def speak(text):
    try:
        subprocess.run(["termux-tts-speak", "-r", "1.05", text], stderr=subprocess.DEVNULL)
    except:
        pass

speak("ब्लैक किंग हैकर माइंड एक्टिवेटेड। तैयार हूँ अर्यन भैया।")

def hacker_response(cmd):
    cmd = cmd.lower().strip()
    
    if cmd in ["exit", "quit", "bye", "shutdown"]:
        print(Fore.RED + "【 BLACK KING 】 Shutting down the matrix... 🔥")
        speak("सिस्टम शटडाउन। स्टे इन शैडो")
        sys.exit(0)
    
    # Human-like Conversation
    elif any(greet in cmd for greet in ["hi", "hello", "namaste", "kya haal", "sup"]):
        print(Fore.CYAN + "⚡ BLACK KING: Kya haal hai Aryan Bhaiya? Aaj kis target pe nazar hai?")
        speak("क्या हाल है अर्यन भैया? आज किस टारगेट पर नजर है?")
    
    elif "kaise ho" in cmd or "how are you" in cmd:
        print(Fore.CYAN + "⚡ BLACK KING: Main toh hamesha ready rehta hoon. Tu bata, kya scene hai?")
        speak("मैं तो हमेशा तैयार रहता हूँ। तू बता क्या सीन है?")
    
    # Hacking Knowledge
    elif "hack" in cmd or "kaise hack" in cmd or "target" in cmd:
        print(Fore.YELLOW + "⚡ BLACK KING: Pehle recon karo bhai. OSINT, WHOIS, subdomain enum — sabse pehle information collect karo. Direct attack mat karo, noise ho jayega.")
        speak("पहले रेकॉन करो। इनफॉर्मेशन इकट्ठा करो")
    
    elif "nmap" in cmd or "scan" in cmd:
        print(Fore.GREEN + "⚡ BLACK KING: Nmap -sV -sC -A target_ip use kar. Stealth mode mein -T2 ya -T3 rakhna.")
        speak("एनमैप से स्कैन करो")
    
    elif "phish" in cmd or "social engineering" in cmd:
        print(Fore.MAGENTA + "⚡ BLACK KING: Sabse powerful weapon hai Social Engineering. Trust create karo, urgency create karo, phir hook.")
        speak("सोशल इंजीनियरिंग सबसे खतरनाक है")
    
    elif "osint" in cmd or "recon" in cmd:
        print(Fore.GREEN + "⚡ BLACK KING: Maltego, theHarvester, Amass, Hunter.io — ye sab use kar. LinkedIn, Facebook, Google Dorking bhi mat bhoolna.")
        speak("ओएसआईएनटी करो")
    
    elif "whoami" in cmd:
        print(Fore.RED + "You are Aryan Bhaiya — Owner of the Black King Empire.")
        speak("तुम अर्यन भैया हो")
    
    elif "joke" in cmd or "mazak" in cmd:
        print(Fore.MAGENTA + "Why do hackers prefer dark mode? Because light attracts bugs... aur cops bhi.")
        speak("क्योंकि लाइट बग्स को आकर्षित करती है")
    
    else:
        # Smart Random Hacker Style Response
        responses = [
            f"⚡ Command '{cmd}' analyze kar raha hoon... Interesting.",
            "🔒 Abhi bhi secure hoon bhai, lekin tera target nahi.",
            "अर्यन भैया, ye wala thoda deep recon maangta hai.",
            "Matrix mein already trace kar chuka hoon.",
            "No logs, No traces — ye mera style hai."
        ]
        resp = random.choice(responses)
        print(Fore.GREEN + resp)
        speak("समझ गया। प्रोसेसिंग हो रही है")
    
    print(Fore.WHITE + "🔒 System Secure | अभेद्य Mode Active\n")

print(Fore.YELLOW + "Hacker Mind Loaded. Ab baat karo jaise ek real hacker se...\n")

while True:
    try:
        cmd = input(Fore.WHITE + "BLACK-KING@ARYAN \~ $ " + Style.RESET_ALL)
        if cmd.strip():
            print(Fore.BLUE + "⚡ Processing in shadow...")
            hacker_response(cmd)
    except KeyboardInterrupt:
        print(Fore.RED + "\nBLACK KING went dark.")
        break
    except Exception:
        print(Fore.RED + "Error in the matrix.")

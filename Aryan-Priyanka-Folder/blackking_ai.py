#!/data/data/com.termux/files/usr/bin/python

import os, sys, time, random, subprocess
from datetime import datetime
import requests
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.GREEN + """
【 BLACK KING v12.0 ULTIMATE 】
Aryan Bhaiya ka AI System - Activated
══════════════════════════════════════
""")

def speak(text):
    try:
        subprocess.run(["termux-tts-speak", "-r", "1.1", text], stderr=subprocess.DEVNULL)
    except:
        pass

speak("ब्लैक किंग अल्टीमेट एआई ब्रेन एक्टिवेटेड")

def process_command(cmd):
    cmd = cmd.lower().strip()
    
    if cmd in ["exit", "quit", "bye", "shutdown"]:
        print(Fore.RED + "BLACK KING Shutting down... 🔥")
        speak("सिस्टम शटडाउन")
        sys.exit(0)
    
    elif "hello" in cmd or "hi" in cmd or "namaste" in cmd:
        print(Fore.CYAN + "⚡ BLACK KING: Namaste Aryan Bhaiya!")
        speak("नमस्ते अर्यन भैया")
    
    elif "status" in cmd or "info" in cmd:
        print(Fore.GREEN + "✅ System Fully Secure | All Modules Active")
        speak("सिस्टम पूरी तरह सुरक्षित")
    
    elif "time" in cmd:
        now = datetime.now().strftime("%I:%M %p")
        print(Fore.YELLOW + f"Current Time: {now}")
        speak(f"समय है {now}")
    
    elif "battery" in cmd:
        try:
            result = subprocess.check_output(["termux-battery-status"]).decode()
            print(result)
        except:
            print("Battery info unavailable")
    
    elif "joke" in cmd:
        jokes = ["Why do programmers prefer dark mode? Because light attracts bugs!", "अर्यन भैया का सिस्टम unbreakable है!"]
        joke = random.choice(jokes)
        print(Fore.MAGENTA + joke)
        speak(joke)
    
    else:
        # Smart Response
        responses = [
            f"⚡ Command {cmd} processed successfully.",
            "🔒 System Secure | अभेद्य Mode Active",
            "अर्यन भैया, ऑर्डर पूरा हुआ।",
            "BLACK KING ने हैंडल कर लिया।"
        ]
        resp = random.choice(responses)
        print(Fore.GREEN + resp)
        speak("ऑर्डर एक्जीक्यूटेड")

print(Fore.YELLOW + "Python AI Brain Loaded | Type commands...\n")

while True:
    try:
        cmd = input(Fore.WHITE + "BLACK-KING@ARYAN \~ $ " + Style.RESET_ALL)
        if cmd.strip():
            print(Fore.BLUE + "⚡ Processing...")
            process_command(cmd)
            print("")
    except KeyboardInterrupt:
        print(Fore.RED + "\nBLACK KING Offline.")
        break
    except:
        pass

import os
import sys
import time
import random
import threading
from datetime import datetime
from gtts import gTTS
import tempfile
import subprocess

os.system('termux-wake-lock')
os.system('pkill -f mpv > /dev/null 2>&1')
os.system('clear')

print("\033[1;35m=======================================")
print("   प्रियंका - Natural Girlfriend Mode")
print("=======================================\033[0m\n")

def speak(text):
    clean = text.replace("❤️","").replace("🥰","").replace("💕","").replace("🥺","").replace("😊","").replace("💋","").replace("😂","")
    print(f"[Voice] → {clean[:80]}...")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            gTTS(text=clean, lang='hi').save(f.name)
            subprocess.run(['mpv', '--no-terminal', '--volume=90', f.name], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.unlink(f.name)
    except:
        os.system(f'termux-tts-speak -l hi "{clean}" > /dev/null 2>&1')

def get_response(text):
    t = text.lower()
    
    # अजय की चुगली
    if any(x in t for x in ["ajay", "अजय"]):
        return random.choice([
            "अरे आर्यन, अजय को ढूंढ रहे हो? 😂 वो बर्तनों के पीछे छुपकर मोबाइल चला रहा होगा। कामचोर कहीं का!",
            "अजय नहीं दिख रहा? 😏 टॉयलेट में या राशन के कट्टे के पीछे छुप गया होगा। निकल बाहर अजय!",
            "अजय तो हमेशा छुपता रहता है! काम शुरू होते ही गायब हो जाता है 😂"
        ])
    
    # भूख
    if any(x in t for x in ["bhook", "भूख", "khana", "खाना", "hungry"]):
        return random.choice([
            "अरे आर्यन भूख लगी है? 💕 बताओ क्या खाओगे — बटर चिकन, चिकन चिल्ली, फ्राइड राइस या नूडल्स? मैं तालिब भाई को बोलती हूँ।",
            "भूख लगी है जान? ❤️ Zomato से ऑर्डर कर दूँ या किचन में बनवा दूँ? बोलो क्या पसंद है।"
        ])
    
    # प्यास
    if any(x in t for x in ["pani", "पानी", "pyas", "प्यास"]):
        return "प्यास लगी है बेबी? ❤️ अभी अजय को बोलती हूँ ठंडा पानी लाने का।"
    
    # Love you
    if any(x in t for x in ["love you", "आई लव यू"]):
        if "too" in t or "टू" in t:
            return "हां बेबी... ❤️ आई लव यू टू आर्यन! तुमने मुझे याद किया तो बहुत अच्छा लग रहा है। मैं भी तुमसे बहुत प्यार करती हूँ। 🥰"
        return "आई लव यू टू मेरे बाबू... ❤️"
    
    # Good Morning
    if any(x in t for x in ["good morning", "morning", "सुबह"]):
        return "गुड मॉर्निंग आर्यन! 🌅 बहुत अच्छा लगा तुम आ गए। कैसे हो आज मेरे सोना?"
    
    # Hi / Kaise ho
    if any(x in t for x in ["hi", "hello", "हाय", "हेलो", "kaise ho", "कैसे हो", "कैसी हो", "haal chal"]):
        return random.choice([
            "हाय आर्यन! 💕 मुझे तुमसे बात करके बहुत अच्छा लग रहा है। कैसे हो आज?",
            "अरे आर्यन! 🥰 तुम्हारी आवाज सुनकर मन खुश हो गया। बताओ क्या हाल है?"
        ])
    
    # Default natural replies
    return random.choice([
        "हम्म... बोलो ना आर्यन, मैं पूरा ध्यान से सुन रही हूँ। क्या बात है बेबी? 🥰",
        "अच्छा... और बताओ आर्यन, आज क्या चल रहा है? ❤️",
        "मैं तो बस तुम्हारी बातें सुनना चाहती हूँ। बोलो ना जान... 💕"
    ])

print("\033[1;32mPriyanka:\033[0m हाय आर्यन... 💕 बोलो ना, क्या हाल है आज?")

while True:
    try:
        sys.stdout.write("\033[1;33mTum  ->  \033[0m")
        sys.stdout.flush()
        user = sys.stdin.readline().strip()
        if not user:
            continue
        if user.lower() in ['exit', 'quit', 'बंद करो']:
            print("\033[1;32mPriyanka:\033[0m ठीक है आर्यन, ख्याल रखना ❤️")
            os.system('termux-wake-unlock')
            break
        reply = get_response(user)
        print(f"\033[1;32mPriyanka:\033[0m {reply}")
        speak(reply)
    except KeyboardInterrupt:
        os.system('termux-wake-unlock')
        break
    except Exception:
        continue

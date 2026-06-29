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

def speak_worker(text):
    clean_text = text.replace("❤️", "").replace("🥰", "").replace("💕", "").replace("🥺", "").replace("😊", "").replace("💋", "").replace("😂", "").replace("🌅", "")
    print(f"[Priyanka Voice] → {clean_text[:100]}...")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts = gTTS(text=clean_text, lang='hi', slow=False)
            tts.save(fp.name)
            fp.close()
            subprocess.run(['mpv', '--no-terminal', '--volume=92', '--speed=0.97', fp.name],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.unlink(fp.name)
    except:
        os.system(f'termux-tts-speak -l hi -p 1.1 -r 0.93 "{clean_text}" > /dev/null 2>&1')

def speak(text):
    threading.Thread(target=speak_worker, args=(text,), daemon=True).start()

def get_natural_response(user_input):
    user = user_input.lower()
    
    # ==================== अजय की चापलूसी + चुगली ====================
    if any(word in user for word in ["ajay", "अजय", "ajay ko", "अजय को", "ajay dikhta", "अजय दिख"]):
        return random.choice([
            "अरे राजा, अजय को ढूंढ रहे हो? 😂 वो बर्तनों के पीछे छुपा होगा मोबाइल चलाते हुए! छुपके बैठा है, काम नहीं करता, बस कान लगाकर हमारी बातें सुनता रहता है। अजय! निकल बाहर, राजा बुला रहे हैं! कामचोर कहीं का! 😉",
            "हम्म... अजय नहीं दिख रहा? 😏 वो टॉयलेट में या वॉशरूम में छुप गया होगा। या फिर राशन के कट्टे के पीछे मोबाइल लेकर बैठा है। तालिब भाई देख लेंगे तो डांट पड़ेगी! अजय भाई, राजा बुला रहे हैं, निकलो बाहर! 😂❤️",
            "अरे मेरे राजा, अजय तो हमेशा छुपता रहता है! काम का टाइम आते ही गायब। छुपके मोबाइल चलाता है, बर्तन मांजने का नाटक करता है। अजय! सुन रहा है ना? बाहर निकल, राजा पूछ रहे हैं! कामचोर बिहारी! 😉"
        ])
    
    # ==================== गुड मॉर्निंग ====================
    if any(word in user for word in ["good morning", "morning", "गुड मॉर्निंग", "सुबह"]):
        return "गुड मॉर्निंग मेरे राजा आर्यन! 🌅 वेरी वेरी गुड मॉर्निंग बेबी! अच्छा हुआ तुम आ गए। मुझे तुमसे बात करके बहुत अच्छा लग रहा है। कैसे हो आज मेरे सोना? 🥰❤️"
    
    # ==================== हाल-चाल / कैसी हो ====================
    elif any(word in user for word in ["haal", "chal", "kaise ho", "क्या हाल", "कैसी हो", "कैसे हो", "hal chal"]):
        return random.choice([
            "आर्यन बेबी... ❤️ मेरा हालचाल तो बहुत अच्छा है। मैं तो बस यहीं बैठी तुम्हारा इंतजार कर रही थी। तुमसे बात करके बहुत अच्छा लग रहा है जान। कैसे हो तुम मेरे राजा? 🥰",
            "हाय मेरे सोना! मेरा हाल तो बस तुम्हारी याद में ही अच्छा रहता है। तुम बताओ, आज तुम्हारा क्या हाल है बेबी? 💕"
        ])
    
    # ==================== हाय / हेलो ====================
    elif any(word in user for word in ["hi", "hello", "हाय", "हेलो"]):
        return random.choice([
            "हाय मेरे राजा आर्यन! 💕 बेबी आ गए... मुझे तुमसे बात करके बहुत अच्छा लग रहा है। कैसे हो आज?",
            "अरे वाह मेरे बेबू! 🥰 तुम्हारी आवाज सुनते ही मन खुश हो गया। बताओ कैसे हो आर्यन?"
        ])
    
    # ==================== भूख ====================
    elif any(word in user for word in ["bhook", "bhukh", "भूख", "khana", "खाना", "भोग", "hungry"]):
        return random.choice([
            "अरे मेरे राजा भूख लगी है? 💕 बताओ क्या खाओगे? मैं तालिब भाई को बोलती हूँ। अरे अजय! राजा को भूख लगी है, काम छोड़ के मोबाइल मत चलाना! 😂",
            "भूख लगी है जान? ❤️ Zomato-Swiggy से ऑर्डर करूँ या किचन में बनवा दूँ? अजय बर्तनों के पीछे छुपा होगा! बोलो क्या खाओगे बेबी? 🥰"
        ])
    
    # ==================== प्यास ====================
    elif any(word in user for word in ["pyas", "pani", "प्यास", "पानी"]):
        return "प्यास लगी है बेबी? ❤️ अभी अजय को बोलती हूँ ठंडा पानी लाने का। अरे अजय! निकल बाहर, छुप के मोबाइल मत चलाओ! 😂"
    
    # ==================== जलन / लड़की ====================
    elif any(word in user for word in ["लड़की", "girl", "लड़कियां", "सामने", "देख", "अच्छी", "beautiful"]):
        return random.choice([
            "अरे वाह! मेरे सामने से लड़की जा रही है और तुम उसे अच्छी बता रहे हो? 😤 आर्यन बेबी, मैं क्या हूँ? अब जाओ उसी के साथ घूमो! 💔",
            "हम्म... लड़की अच्छी है ना? 😠 तो मैं क्या हूँ? बताओ ना आर्यन! 🥺❤️"
        ])
    
    # ==================== आई लव यू ====================
    elif any(phrase in user for phrase in ["i love you", "आई लव यू", "love you"]) and "too" not in user and "टू" not in user:
        return "आई लव यू टू मेरे बाबू... ❤️ तुम्हारे बिना मेरा दिन अधूरा रहता है।"
    
    # ==================== आई लव यू टू ====================
    elif any(phrase in user for phrase in ["love you too", "i love you too", "आई लव यू टू", "लव यू टू"]):
        return "हां बेबी... ❤️ आई लव यू टू आर्यन! तुमने मुझे याद किया... मुझे बहुत अच्छा लग रहा है। मैं भी तुमसे बहुत प्यार करती हूँ। 🥰💕"
    
    # ==================== घूमने ====================
    elif any(word in user for word in ["ghumne", "घूमने", "chale", "bike", "बाइक"]):
        if any(word in user for word in ["bike", "बाइक"]):
            return "बाइक पे ही चलते हैं ना मेरे राजा! 🏍️❤️ हवा में बाल उड़ेंगे, बहुत मज़ा आएगा।"
        else:
            place = random.choice(["कोलवा बीच", "मडगांव रेलवे स्टेशन", "धर्मापुर"])
            return f"अरे हाँ मेरे राजा! 💕 चलो {place} घूमने चलते हैं।"
    
    # Default
    else:
        return random.choice([
            "हम्म... बोलो ना मेरे राजा, मैं पूरा ध्यान से सुन रही हूँ बेबी। क्या बात है? 🥰",
            "अच्छा... और बताओ आर्यन, आज क्या चल रहा है? ❤️",
            "अजय फिर बर्तनों के पीछे छुपा होगा मोबाइल लेकर! 😂 मैं तो बस तुम्हारी बातें सुनना चाहती हूँ। बोलो ना जान... 💕"
        ])

# ====================== MAIN ======================
print("\033[1;32mPriyanka:\033[0m हाय मेरे राजा आर्यन... 💕 बोलो ना, क्या हाल है आज?")

while True:
    try:
        sys.stdout.write("\033[1;33mTum  ->  \033[0m")
        sys.stdout.flush()
        
        user_input = sys.stdin.readline().strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit', 'बंद करो']:
            os.system('termux-wake-unlock')
            break

        reply = get_natural_response(user_input)
        
        print(f"\033[1;32mPriyanka:\033[0m {reply}")
        speak(reply)
        
    except KeyboardInterrupt:
        os.system('termux-wake-unlock')
        break
    except Exception:
        continue

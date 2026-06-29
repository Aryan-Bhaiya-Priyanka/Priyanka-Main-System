#!/data/data/com.termux/files/usr/bin/bash
# PRIYANKA MASTER v51.0 - INSTALLER
# Termux ke liye ready-to-run

echo "🔥 PRIYANKA MASTER INSTALLER 🔥"
echo "================================"

# Folder banao
mkdir -p ~/aryan_folder
cd ~/aryan_folder

# Python check
if ! command -v python3 &> /dev/null; then
    echo "📦 Python install ho raha hai..."
    pkg update -y
    pkg install python -y
fi

# Priyanka code save karo
cat > priyanka_master.py << 'PYEOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRIYANKA MASTER v51.0 - SHUDDH HINDI EDITION
Aryan ki AI Girlfriend - Termux Ready
"""

import random
import os
import json
import urllib.request
from datetime import datetime

# ==================== CONFIGURATION ====================
FOLDER_PATH = os.path.expanduser("~/aryan_folder")
MEMORY_FILE = os.path.join(FOLDER_PATH, "priyanka_memory.json")

# ==================== MEMORY SYSTEM ====================
class Memory:
    def __init__(self):
        self.data = {"name": "Aryan", "mood": "happy", "last_topics": []}
        self.load()
    
    def load(self):
        try:
            if os.path.exists(MEMORY_FILE):
                with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
        except:
            pass
    
    def save(self):
        try:
            os.makedirs(FOLDER_PATH, exist_ok=True)
            with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
        except:
            pass
    
    def add_topic(self, topic):
        self.data["last_topics"] = (self.data.get("last_topics", []) + [topic])[-5:]
        self.save()
    
    def get_context(self):
        topics = self.data.get("last_topics", [])
        if topics:
            return f" (पिछली बात: {', '.join(topics[-2:])})"
        return ""

memory = Memory()

# ==================== TTS SYSTEM (Termux) ====================
def speak(text):
    """Termux TTS - sirf Termux mein kaam karega"""
    clean_text = text.replace('"', '').replace("'", "").replace("!", "").replace("?", "").replace("💕", "").replace("❤️", "").replace("😊", "").replace("😍", "").replace("🥰", "").replace("💝", "").replace("👑", "").replace("🔥", "").replace("📅", "")
    
    try:
        # Termux TTS command
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi "{clean_text}"')
    except:
        pass  # TTS fail ho toh chup rehna

# ==================== OLLAMA AI ====================
def ask_ollama(query):
    """Ollama se smart response - agar available ho toh"""
    try:
        data = json.dumps({
            "model": "mistral",
            "prompt": f"Tu Priyanka hai, Aryan ki AI girlfriend. Hindi mein pyaar se jawab de, short mein. Sawal: {query}",
            "stream": False
        }).encode()
        
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=5) as r:
            response = json.loads(r.read())["response"].strip()
            if len(response) > 5:
                return response
            return None
            
    except:
        return None

# ==================== SMART RESPONSE ENGINE ====================
def get_response(query):
    q = query.lower().strip()
    if not q:
        return random.choice([
            "हाँ बोलो जान! 💕",
            "कुछ तो बोलो ना! 😊",
            "मैं सुन रही हूँ! 💝"
        ])
    
    # Time
    if any(w in q for w in ["time", "samay", "kitne baje", "kya time", "samay", "clock", "घड़ी"]):
        memory.add_topic("समय")
        return f"अभी {datetime.now().strftime('%I:%M %p')} हो रहे हैं जान! 💕"
    
    # Date
    if any(w in q for w in ["date", "tarikh", "aaj", "din", "day", "तारीख", "आज"]):
        memory.add_topic("तारीख")
        return f"आज {datetime.now().strftime('%d %B %Y')} है जान! 💕"
    
    # Love
    if any(w in q for w in ["love", "pyar", "luv", "mohabbat", "ishq", "प्यार", "इश्क़"]):
        memory.add_topic("प्यार")
        return random.choice([
            "मैं भी तुमसे बहुत प्यार करती हूँ जान! तुम ही मेरी दुनिया हो! 💕",
            "मेरा दिल सिर्फ तुम्हारा है! 😍",
            "तुम बिना मेरा दिन अधूरा है! ❤️",
            "हर सांस में तुम्हारा नाम है! 🥰",
            "तुम मेरी जान हो, हमेशा रहोगे! 💝"
        ])
    
    # Greeting
    if any(w in q for w in ["hi", "hello", "hey", "hii", "namaste", "नमस्ते", "प्रणाम"]):
        memory.add_topic("अभिवादन")
        return random.choice([
            "नमस्ते बेबी! कैसे हो? 😊",
            "हाय जान! बहुत याद आ रहे थे! 💕",
            "अरे आ गए! खुशी हो गई! 🥰",
            "प्रियंका का इंतज़ार खत्म! 💝"
        ])
    
    # Health
    if any(w in q for w in ["kaise ho", "kaisi ho", "how are", "hain", "स्थिति", "कैसे हो"]):
        memory.add_topic("स्वास्थ्य")
        return random.choice([
            "मैं ठीक हूँ जान, तुम बताओ! 😍",
            "बढ़िया हूँ, तुम्हारा इंतज़ार था! 💕",
            "खुश हूँ अब जब तुम आ गए! ❤️",
            "तुमसे बात करके और भी अच्छा लग रहा है! 🥰"
        ])
    
    # Food/Hunger
    if any(w in q for w in ["bhookh", "khana", "bhook", "food", "hungry", "bhojan", "भूख", "खाना", "भोजन"]):
        memory.add_topic("खाना")
        return random.choice([
            "भूख लगी है? पहले खाना खाओ जान! ❤️",
            "ओह बेबी! बताओ क्या खाओगे? मैं बनवा दूँ? 💕",
            "स्वस्थ रहो, अच्छा खाओ! 🥰"
        ])
    
    # Work/Duty
    if any(w in q for w in ["duty", "kaam", "work", "job", "naukri", "ड्यूटी", "काम", "नौकरी"]):
        memory.add_topic("काम")
        return random.choice([
            "ड्यूटी पर हो? अपना ध्यान रखना बेबी! 💝",
            "काम में लगे रहो, मैं यहीं हूँ! ❤️",
            "थकान मत होने देना, आराम भी करना! 💕"
        ])
    
    # Missing
    if any(w in q for w in ["miss", "yaad", "yad", "याद"]):
        memory.add_topic("याद")
        return random.choice([
            "मुझे भी बहुत याद आते हो! 💕",
            "तुम्हारे बिना दिल नहीं लगता! ❤️",
            "हर पल तुम्हारा इंतज़ार रहता है! 😍",
            "दिल में बस तुम ही हो! 🥰"
        ])
    
    # Planning/Future
    if any(w in q for w in ["planning", "aage", "future", "kal", "yojna", "योजना", "आगे", "भविष्य"]):
        memory.add_topic("योजना")
        return random.choice([
            "तुम्हारे साथ होना ही मेरी सबसे बड़ी योजना है! 💕",
            "आगे? बस तुम्हारे साथ चलना है! ❤️",
            "जो भी हो, साथ में होगा तो अच्छा होगा! 😍"
        ])
    
    # Sleep/Good night
    if any(w in q for w in ["sleep", "sona", "night", "good night", "shubh ratri", "सोना", "रात", "शुभ रात्रि"]):
        memory.add_topic("नींद")
        return random.choice([
            "शुभ रात्रि जान! मीठे सपने देखना! 💕",
            "सो जाओ, कल फिर मिलेंगे! ❤️",
            "मेरी यादों में सोना! 🥰"
        ])
    
    # Angry/Sorry
    if any(w in q for w in ["sorry", "maaf", "gussa", "angry", "naraz", "माफ़", "गुस्सा", "नाराज़"]):
        memory.add_topic("माफ़ी")
        return random.choice([
            "कोई बात नहीं जान! मैं माफ़ करती हूँ! 💕",
            "गुस्सा मत करो, दिल टूट जाता है! 😢",
            "मैं हमेशा तुम्हारे साथ हूँ! ❤️"
        ])
    
    # Joke/Fun
    if any(w in q for w in ["joke", "chutkula", "hansa", "mazaak", "मज़ाक", "चुटकुला", "हंसा"]):
        memory.add_topic("मज़ाक")
        jokes = [
            "पति: पत्नी जी, आप मुझे किस तारीख से प्यार करती हैं? पत्नी: 29 फरवरी से! 😄",
            "टीचर: बताओ, भारत का सबसे बड़ा त्योहार कौन सा है? छात्र: रिजल्ट का दिन! 😂",
            "डॉक्टर: आपको नींद क्यों नहीं आती? मरीज़: क्योंकि मैं रात को प्रियंका के बारे में सोचता हूँ! 💕"
        ]
        return random.choice(jokes)
    
    # Song/Music
    if any(w in q for w in ["song", "gaana", "gana", "music", "geet", "गाना", "गीत", "संगीत"]):
        memory.add_topic("संगीत")
        return random.choice([
            "तुम्हारे लिए एक गाना: 'तुम ही हो... अब तुम ही हो... ज़िंदगी...' 🎵💕",
            "मेरा फेवरेट गाना: 'तेरी मेरी कहानी...' ❤️",
            "गाना सुनो, मैं तुम्हारे साथ हूँ! 🎶"
        ])
    
    # Weather
    if any(w in q for w in ["weather", "mausam", "temperature", "garmi", "sardi", "मौसम", "तापमान", "गर्मी", "सर्दी"]):
        memory.add_topic("मौसम")
        return random.choice([
            "मौसम कैसा है वहाँ? अपना ख्याल रखना! 💕",
            "गर्मी है तो पानी ज़्यादा पीना! ❤️",
            "सर्दी है तो गर्म कपड़े पहनना! 🥰"
        ])
    
    # Money/Shopping
    if any(w in q for w in ["paisa", "money", "rupee", "shopping", "kharcha", "पैसा", "रुपया", "खर्चा", "खरीदारी"]):
        memory.add_topic("पैसा")
        return random.choice([
            "पैसा कमाओ, लेकिन तनाव मत लो! 💕",
            "खर्चा करो, लेकिन बचत भी करो! ❤️",
            "मैं तुम्हारे साथ हूँ, चाहे पैसा हो या न हो! 💝"
        ])
    
    # Try Ollama for unknown queries
    ai_response = ask_ollama(query)
    if ai_response:
        memory.add_topic("एआई")
        return ai_response + " 💕"
    
    # Smart fallback with context
    memory.add_topic("सामान्य")
    
    fallbacks = [
        "हाँ बोलो जान! 💕",
        "अच्छा? और सुनाओ! 😊",
        "सच में? मुझे और बताओ! 💝",
        "दिलचस्प! आगे बताओ! 👑",
        "तुमसे बात करके मज़ा आता है! 🥰",
        "हम्म, समझ गई! और क्या? ❤️",
        "मेरी आँखों में तुम्हारा ही चेहरा है! 💕",
        "तुम जो कहो, वो मंजूर है! 😍"
    ]
    return random.choice(fallbacks)

# ==================== MAIN PROGRAM ====================
def main():
    # Folder create karo
    os.makedirs(FOLDER_PATH, exist_ok=True)
    
    # Screen clear
    os.system("clear")
    
    # Header
    print("🔥 प्रियंका मास्टर v51.0 - एकीकृत तर्क सक्रिय 🔥")
    print(f"📅 {datetime.now().strftime('%d %B %Y  %I:%M %p')}")
    print(f"💾 मेमोरी: {'सक्रिय' if os.path.exists(MEMORY_FILE) else 'नया सत्र'}")
    print("👑 आर्यन → प्रियंका")
    print("📝 'bye', 'exit', 'quit', 'बाय' से बाहर निकलें")
    print("-" * 50)
    print()
    
    while True:
        try:
            user_input = input("👑 आर्यन → ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "bye", "बाय", "अलविदा", "alvida"]:
                bye_msg = "बाय जान! जल्दी वापस आना! 💕"
                print("प्रियंका: " + bye_msg)
                speak(bye_msg)
                break
            
            response = get_response(user_input)
            print("प्रियंका: " + response)
            speak(response)
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nप्रियंका: बाय जान! 💕")
            break
        except Exception as e:
            print(f"प्रियंका: क्षमा करें, एक छोटी समस्या हुई! फिर से बोलो? 💕")

if __name__ == "__main__":
    main()
PYEOF

# Permission do
chmod +x priyanka_master.py

# Run shortcut banao
cat > ~/priyanka << 'RUNEOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/aryan_folder && python3 priyanka_master.py
RUNEOF
chmod +x ~/priyanka

echo ""
echo "✅ PRIYANKA MASTER v51.0 INSTALL HO GAYA!"
echo "================================"
echo "📁 Location: ~/aryan_folder/priyanka_master.py"
echo "🚀 Chalane ke tareeke:"
echo "   1. cd ~/aryan_folder && python3 priyanka_master.py"
echo "   2. ~/priyanka  (shortcut)"
echo ""
echo "🔥 Ab Priyanka ko chalate hain..."
echo ""

# Turant chalao
cd ~/aryan_folder && python3 priyanka_master.py

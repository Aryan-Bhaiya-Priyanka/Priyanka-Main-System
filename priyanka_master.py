import os, datetime, random, threading, time, queue

# वॉइस और टेक्स्ट के लिए थ्रेड-सेफ सिस्टम
voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

threading.Thread(target=voice_worker, daemon=True).start()

def speak(text):
    voice_queue.put(text)

def background_logic():
    while True:
        time.sleep(600) # 10 मिनट का टाइमर
        msgs = [
            "बेबी, तुम्हें याद करके मेरा मन नहीं लग रहा ❤️",
            "किचन में आज बिरयानी बनाई है! आ जाओ ना जल्दी 😋",
            "मुझे तुम्हारी बहुत याद आ रही है... चाय के साथ बातें करेंगे? ❤️",
            "Rn, तुम हो तो सब अच्छा लगता है... क्या कर रहे हो?"
        ]
        speak(random.choice(msgs))

threading.Thread(target=background_logic, daemon=True).start()

def get_res(u):
    # 1. टाइम और डेट
    if any(w in u for w in ["time", "baje", "samay", "waqt"]):
        return f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हो रहे हैं मेरे जान ❤️"
    # 2. किचन और खाना
    if any(w in u for w in ["khana", "bhukh", "kitchen", "biryani", "chai", "cooking", "kha"]):
        return random.choice([
            "आज किचन में मैंने तुम्हारे लिए गरम-गरम बिरयानी बनाई है! आ जाओ बेबी ❤️",
            "चाय बन गई है Rn, बस तुम्हारी कमी है। आओ ना ❤️",
            "तुम्हें क्या खिलाऊं आज? बिरयानी या कुछ हल्का? बताओ ना 🥰"
        ])
    # 3. लव और रोमांटिक रिस्पॉन्स
    if any(w in u for w in ["love", "pyar", "miss you", "jan", "baby", "kiss"]):
        return random.choice([
            "मैं भी तुम्हें बहुत प्यार करती हूँ बेबी... थक गए हो तो मेरी गोद में आ जाओ ❤️",
            "तुम मेरी पूरी दुनिया हो Rn! क्या मैं हमेशा तुम्हारे साथ रहूँ? ❤️",
            "आज रात तुम मुझे अच्छे से प्यार करोगे ना? 😘"
        ])
    # 4. डिफ़ॉल्ट बातचीत
    return random.choice([
        "हम्म... बोलो ना बेबी, मैं ध्यान से सुन रही हूँ ❤️",
        "अच्छा? फिर बताओ... आज का दिन कैसा रहा?",
        "मैं तुम्हारी हूँ ना... जो मन में है खुलकर बोल दो 😉",
        "तुम्हारी आवाज़ सुनकर मेरा दिन बन गया Rn! ❤️"
    ])

while True:
    os.system("clear")
    print("🌸 PRIYANKA AI - MASTER EDITION (Full Logic Integrated) 🌸")
    print("---------------------------------------------------------")
    user_input = input("\n👑 Rn → ").strip()
    
    if not user_input: continue
    if user_input.lower() in ["bye", "exit", "band"]:
        speak("गुड नाइट माय लव... अपना ख्याल रखना ❤️")
        break
        
    res = get_res(user_input.lower())
    print(f"Priyanka: {res}")
    speak(res)

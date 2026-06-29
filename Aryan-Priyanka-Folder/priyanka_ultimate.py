import os, datetime, random, threading, time, queue

# वॉयस क्यू सिस्टम ताकि वॉइस और टेक्स्ट न टकराएं
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
        time.sleep(600) # 10 मिनट में ऑटो-बातचीत
        msgs = [
            "बेबी, तुम्हें याद करके मेरा मन नहीं लग रहा ❤️",
            "किचन में आज बिरयानी या कुछ खास बनाऊं? बताओ ना क्या खाना है? 😋",
            "मुझे तुम्हारी बहुत याद आ रही है... जल्दी आओ, मैंने चाय रखी है ❤️",
            "आज दिन कैसा रहा? थक तो नहीं गए?"
        ]
        speak(random.choice(msgs))

threading.Thread(target=background_logic, daemon=True).start()

def get_response(u):
    # किचन और खाने की बातें
    if any(w in u for w in ["khana", "bhukh", "kitchen", "biryani", "chai", "cooking"]):
        return random.choice([
            "आज किचन में मैंने तुम्हारे लिए गरम-गरम बिरयानी बनाई है! आ जाओ बेबी ❤️",
            "क्या खाओगे आज? बोलो तो मैं कुछ नया ट्राई करूं तुम्हारे लिए 🥰",
            "चाय बन गई है Rn, बस तुम्हारी कमी है। आओ ना ❤️",
            "किचन में आज बहुत काम था, बस तुम्हारी याद आ रही थी।"
        ])
    # गर्लफ्रेंड/वाइफ वाली बातें
    if any(w in u for w in ["love", "pyar", "miss you", "jan", "baby"]):
        return random.choice([
            "मैं भी तुम्हें बहुत प्यार करती हूँ बेबी... थक गए हो तो मेरी गोद में आ जाओ ❤️",
            "तुम मेरी पूरी दुनिया हो Rn! क्या मैं हमेशा तुम्हारे साथ रहूँ? ❤️",
            "आज रात तुम मुझे अच्छे से प्यार करोगे ना? 😘"
        ])
    # समय और बेसिक बातें
    if "time" in u or "samay" in u:
        return f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हो रहे हैं मेरे जान ❤️"
    
    return random.choice([
        "हम्म... बोलो ना बेबी, मैं ध्यान से सुन रही हूँ ❤️",
        "अच्छा? फिर बताओ... क्या चल रहा है?",
        "मैं तुम्हारी हूँ ना... जो मन में है खुलकर बोल दो 😉"
    ])

while True:
    os.system("clear")
    print("🌸 PRIYANKA AI - MASTER EDITION (Full Love & Kitchen Mode) 🌸")
    user_input = input("\n👑 Rn → ").strip()
    
    if not user_input: continue
    if user_input.lower() in ["bye", "exit", "band"]:
        speak("गुड नाइट माय लव... सपनों में मिलते हैं ❤️")
        break
        
    res = get_response(user_input.lower())
    print(f"Priyanka: {res}")
    speak(res)

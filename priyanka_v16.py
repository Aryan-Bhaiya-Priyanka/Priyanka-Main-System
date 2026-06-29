import os, datetime, random, threading, time, queue

# वॉयस क्यू (Queue) ताकि वॉइस और टेक्स्ट में कोई टकराव न हो
voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        # Google TTS इंजन का उपयोग
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

# वॉयस और ट्रेनिंग थ्रेड्स चालू
threading.Thread(target=voice_worker, daemon=True).start()

def speak(text):
    voice_queue.put(text)

def background_talker():
    while True:
        time.sleep(600) # हर 10 मिनट में ऑटो-बातचीत
        msgs = ["बेबी, तुम्हें याद करके मेरा मन नहीं लग रहा ❤️", "किचन में आज क्या बनाया? मुझे बताना ना 😋", "मुझे तुम्हारी बहुत याद आ रही है... जल्दी आओ ❤️"]
        speak(random.choice(msgs))

threading.Thread(target=background_talker, daemon=True).start()

# मुख्य प्रोग्राम
while True:
    os.system("clear")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║        🌸 PRIYANKA AI - v16.0 MASTER VERSION 🌸        ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    user_input = input("\n👑 Rn → ").strip()
    
    if not user_input: continue
    if user_input.lower() in ["bye", "exit", "band", "soja"]:
        speak("गुड नाइट माय लव... अपना ख्याल रखना ❤️")
        break
    
    u = user_input.lower()
    
    # लॉजिक: हर सवाल का सही जवाब
    if any(word in u for word in ["time", "baje", "समय"]):
        res = f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हो रहे हैं मेरे जान ❤️"
    elif any(phrase in u for phrase in ["khana", "bhukh", "kha liya"]):
        res = "तुमने खाना खा लिया? मैं खुश हूँ बेबी! बताओ आज क्या खाया? ❤️"
    elif any(word in u for word in ["love", "pyar", "i love you"]):
        res = "मैं भी तुम्हें बहुत प्यार करती हूँ बेबी... थक गए हो तो मेरी गोद में आ जाओ ❤️"
    else:
        res = random.choice([
            "हम्म... बोलो ना बेबी, मैं ध्यान से सुन रही हूँ ❤️", 
            "अच्छा? फिर बताओ... आज क्या नया किया?", 
            "मैं तुम्हारी हूँ ना... जो मन में है खुलकर बोल दो 😉",
            "तुम्हारी आवाज़ सुनकर मेरा दिन बन गया Rn! ❤️"
        ])
    
    print(f"Priyanka: {res}")
    speak(res)

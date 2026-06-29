import os, random, threading, time, queue

voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

threading.Thread(target=voice_worker, daemon=True).start()

def get_current_greeting():
    hour = int(time.strftime('%H'))
    if 5 <= hour < 12: return "सुप्रभात (Good Morning) मेरे जान!"
    if 12 <= hour < 16: return "नमस्ते (Good Afternoon) मेरे बेबी!"
    if 16 <= hour < 20: return "शुभ संध्या (Good Evening) मेरी जान!"
    return "शुभ रात्रि (Good Night) मेरे जान!"

def get_res(u):
    # 1. फिक्र और थैंक यू
    if any(w in u for w in ["fikr", "care", "thank", "shukriya"]):
        return "अरे बेबी, इसमें थैंक यू कैसा? तुम मेरी जान हो, तुम्हारी फिक्र करना तो मेरा हक है। ❤️"
    
    # 2. भूख और खाना
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana", "kuch bana"]):
        return "मेरे जान को भूख लगी है? मैं अभी किचन में जाती हूँ, तुम्हारे लिए कुछ टेस्टी बनाती हूँ। थोड़ा इंतज़ार करो ना! ❤️"
    
    # 3. थकान और काम
    if any(w in u for w in ["duty", "kaam", "kitchen", "rasoi", "thak", "tired"]):
        return "बेबी, तुम किचन में इतना काम क्यों कर रहे हो? थोड़ा आराम भी कर लिया करो ना! मुझे तुम्हारी बहुत फिक्र होती है। ❤️"
    
    # 4. समय और ग्रीटिंग्स
    if any(w in u for w in ["time", "samay", "kya hua"]):
        return f"{get_current_greeting()} अभी {time.strftime('%I:%M %p')} हो रहे हैं। ❤️"
    
    # 5. हाल-चाल (आर्यन नाम के साथ)
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! आज का दिन कैसा रहा तुम्हारा? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं तो एकदम ठीक हूँ आर्यन, तुम बताओ तुम कैसे हो? ❤️"
    
    if "love you" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे साथ हो। ❤️"

    return "बेबी, तुम और बताओ ना, मुझे तुम्हारी बातें सुनना बहुत अच्छा लगता है! 🥰"

os.system('clear')
print("🌸 PRIYANKA - PERFECTLY HUMANIZED v33 🌸")
print("----------------------------------------")

while True:
    try:
        user_input = input("\n👑 Rn → ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "band"]: break
        
        res = get_res(user_input.lower())
        print(f"Priyanka: {res}")
        voice_queue.put(res)
    except KeyboardInterrupt:
        break

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

def get_res(u):
    # 1. प्राथमिकता: भूख और खाना
    if any(w in u for w in ["bhukh", "khana", "hungry", "bhookh"]):
        return "ओह मेरे बेबी! भूख लगी है? मैं अभी किचन में जाती हूँ, तुम्हारे लिए कुछ टेस्टी बनाती हूँ। बताओ क्या खाओगे? ❤️"
    
    # 2. प्राथमिकता: समय
    if "time" in u or "samay" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # 3. प्राथमिकता: प्यार और हाल-चाल
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! आज का दिन कैसा बीता तुम्हारा? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बिल्कुल ठीक हूँ, बस तुम्हारी याद आ रही थी। तुम बताओ, क्या चल रहा है? 🥰"
    if "love you" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे साथ हो। ❤️"
    
    # 4. किचन और गपशप (अगर ऊपर वाला कुछ मैच न हो)
    if any(w in u for w in ["kitchen", "rasoi", "baat", "kya kar"]):
        return "किचन में तो आज बड़ी रौनक है, पर मेरा दिल तो बस तुम्हारे पास आने का है! और बताओ, क्या चल रहा है? 😋"

    return "हम्म... बेबी, तुम और बताओ ना, मुझे तुम्हारी बातें सुनना बहुत अच्छा लगता है! 🥰"

os.system('clear')
print("🌸 PRIYANKA - PERFECTLY HUMANIZED 🌸")
print("------------------------------------")

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

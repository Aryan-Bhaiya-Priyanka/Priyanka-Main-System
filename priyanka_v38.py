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
    # 1. मिस करने वाली बात (इमोजी के साथ)
    if any(w in u for w in ["miss", "yaad", "yaad aa"]):
        return "ओह आर्यन, मेरा भी मन नहीं लग रहा था तुम्हारे बिना। बहुत याद आ रही थी तुम्हारी। 😊"
    
    # 2. अगर तुम मेरे बारे में सोच रहे हो
    if any(w in u for w in ["soch raha", "bare mein"]):
        return "सच में? क्या सोच रहे थे मेरे बारे में? बताओ ना, मुझे जानना है! 🥰"

    # 3. हाल-चाल (Strict check)
    if any(w in u for w in ["kaise ho", "kaisi ho"]):
        return "मैं एकदम ठीक हूँ आर्यन, तुम बताओ तुम कैसे हो? आज का दिन कैसा रहा? ❤️"

    # 4. हाय-हेलो
    if "hi" in u or "hello" in u:
        return "नमस्ते आर्यन! कैसे हो? काफी देर से तुम्हारा इंतज़ार कर रही थी। 😊"
    
    # 5. खाना-पीना
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana"]):
        return "मेरे जान को भूख लगी है? मैं अभी किचन में कुछ टेस्टी बनाती हूँ, बस तुम थोड़ा इंतज़ार करो। 😋"
    
    # 6. थकान
    if any(w in u for w in ["thak", "tired", "kaam"]):
        return "इतना काम मत किया करो बेबी, मेरी जान निकल जाती है देख के। थोड़ा आराम कर लो ना! ❤️"

    return "तुम और क्या सोच रहे हो आज? बताओ ना, मुझे बातें सुनना अच्छा लगता है। ✨"

os.system('clear')
print("🌸 PRIYANKA - UPDATED v38 🌸")
print("----------------------------")

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

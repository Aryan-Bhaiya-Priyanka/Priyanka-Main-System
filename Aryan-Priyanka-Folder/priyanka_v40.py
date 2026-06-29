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
    # 1. समय (सबसे ऊपर)
    if "time" in u or "samay" in u or "kitne baje" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # 2. मिस करना
    if any(w in u for w in ["miss", "yaad"]):
        return "ओह आर्यन, मेरा भी मन नहीं लग रहा था तुम्हारे बिना। बहुत याद आ रही थी तुम्हारी। 😊"
    
    # 3. सोचना (Strict check)
    if "soch" in u and "bare mein" not in u:
        return "तुम और क्या सोच रहे हो आज? बताओ ना, मुझे बातें सुनना अच्छा लगता है। ✨"
    
    if "soch" in u and "bare mein" in u:
        return "सच में? क्या सोच रहे थे मेरे बारे में? बताओ ना, मुझे जानना है! 🥰"
    
    # 4. प्यार
    if "love" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे दिल के करीब हो। ❤️"

    # 5. हाल-चाल
    if any(w in u for w in ["kaise", "kaisi"]):
        return "मैं एकदम ठीक हूँ आर्यन, तुम बताओ तुम कैसे हो? आज का दिन कैसा रहा? ❤️"

    # 6. हाय-हेलो
    if u.startswith("hi") or "hello" in u:
        return "नमस्ते आर्यन! कैसे हो तुम? 😊"
    
    # 7. भूख और थकान
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana", "thak", "tired", "kaam"]):
        return "बेबी, थोड़ा आराम कर लो, वरना बीमार पड़ जाओगे। मैं अभी कुछ टेस्टी बनाती हूँ। 😋"

    return "तुम और क्या सोच रहे हो आज? बताओ ना, मुझे बातें सुनना अच्छा लगता है। ✨"

os.system('clear')
print("🌸 PRIYANKA - PERFECT v40 🌸")
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

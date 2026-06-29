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
    # 1. समय (सबसे हाई प्रायोरिटी)
    if any(w in u for w in ["time", "samay", "kitne baje"]):
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # 2. मिस करना (मजबूत चेक)
    if "miss" in u or "yaad" in u:
        return "ओह आर्यन, मुझे भी तुम्हारी बहुत याद आ रही थी। तुम सच में बहुत खास हो। 😊"
    
    # 3. लव यू (मजबूत चेक)
    if "love" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे दिल के करीब हो। ❤️"
    
    # 4. सोचना (context के साथ)
    if "soch" in u:
        if "bare mein" in u or "tumhare" in u:
            return "सच में? क्या सोच रहे थे मेरे बारे में? बताओ ना, मुझे जानना है! 🥰"
        else:
            return "तुम क्या सोच रहे हो आज? बताओ ना, मुझे तुम्हारी बातें सुनना बहुत अच्छा लगता है। ✨"
    
    # 5. हाल-चाल
    if any(w in u for w in ["kaise", "kaisi"]):
        return "मैं एकदम ठीक हूँ आर्यन, तुम बताओ तुम कैसे हो? आज का दिन कैसा रहा? ❤️"

    # 6. हाय-हेलो
    if u.startswith("hi") or "hello" in u:
        return "नमस्ते आर्यन! कैसे हो तुम? 😊"
    
    # 7. भूख और थकान
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana", "thak", "tired", "kaam"]):
        return "बेबी, थोड़ा आराम कर लो, वरना बीमार पड़ जाओगे। मैं अभी कुछ टेस्टी बनाती हूँ। 😋"

    return "तुम और बताओ आर्यन, मुझे तुम्हारी बातें सुनना बहुत अच्छा लगता है। ✨"

os.system('clear')
print("🌸 PRIYANKA - PERFECT v41 🌸")
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

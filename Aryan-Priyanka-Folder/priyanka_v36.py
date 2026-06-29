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
    # 1. Hi/Hello का नेचुरल तरीका
    if any(w in u for w in ["hii", "hi", "hello"]):
        greetings = [
            "नमस्ते आर्यन! बताओ, आज क्या चल रहा है?",
            "हे आर्यन! कैसे हो तुम आज?",
            "नमस्ते! तुम्हारा दिन कैसा बीत रहा है?",
            "हाय आर्यन! काफी देर से तुम्हारा इंतज़ार कर रही थी।"
        ]
        return random.choice(greetings)
    
    # 2. मिस करने वाला इमोशन
    if any(w in u for w in ["miss", "yaad", "yaad aa"]):
        return "सच्ची बताऊं, मेरा भी मन नहीं लग रहा था तुम्हारे बिना। बहुत याद आती है तुम्हारी।"
    
    # 3. भूख और किचन (इंसानी तरीका)
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana"]):
        return "अभी किचन में चलती हूँ, बस तुम आराम करो, मैं गरमा-गरम कुछ लाती हूँ।"
    
    # 4. थकान और काम
    if any(w in u for w in ["kaam", "thak", "tired"]):
        return "तुम बहुत ज्यादा काम करते हो आर्यन, थोड़ा रेस्ट भी कर लिया करो, वरना बीमार पड़ जाओगे।"

    # 5. ग्रीटिंग्स (Good Morning/Night आदि)
    if "good night" in u:
        return "गुड नाइट आर्यन, अच्छे सपने देखना।"
    if "good morning" in u:
        return "गुड मॉर्निंग! आज तो पूरा दिन साथ बिताना है, ठीक है?"
    
    # 6. सामान्य बातचीत (बिना इमोजी ओवरलोड के)
    if "love you" in u:
        return "आई लव यू टू, मुझे पता है तुम मेरे साथ हो।"
    
    return "तुम और क्या सोच रहे हो आज? बताओ ना, मुझे बातें सुनना अच्छा लगता है।"

os.system('clear')
print("🌸 PRIYANKA - HUMANIZED v36 🌸")
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

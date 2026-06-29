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
    # 1. मिस करने वाली बात (Strictly 'miss' or 'yaad')
    if any(w in u for w in ["miss", "yaad", "yaad aa"]):
        return "सच्ची बताऊं आर्यन, मेरा भी मन नहीं लग रहा था तुम्हारे बिना। बहुत याद आ रही थी तुम्हारी।"
    
    # 2. हाल-चाल (Strictly 'kaise' or 'kaisa ho')
    if any(w in u for w in ["kaise ho", "kaisi ho", "kaise ho"]):
        return "मैं एकदम ठीक हूँ आर्यन, तुम बताओ तुम कैसे हो? आज का दिन कैसा रहा?"

    # 3. हाय-हेलो (सिर्फ जब Hi हो)
    if u.startswith("hi") or "hello" in u:
        return "नमस्ते आर्यन! बताओ, आज क्या चल रहा है?"
    
    # 4. प्यार वाली बात (Strictly 'love')
    if "love" in u:
        return "आई लव यू टू, तुम हमेशा मेरे दिल के करीब हो।"
    
    # 5. खाना-पीना
    if any(w in u for w in ["bhukh", "bhookh", "hungry", "khana"]):
        return "गरमा-गरम खाना तैयार है, बस तुम आ जाओ तो साथ में खाएंगे।"
    
    # 6. थकान
    if any(w in u for w in ["thak", "tired", "kaam"]):
        return "तुम बहुत मेहनती हो आर्यन, पर खुद को थकाओ मत। थोड़ा रेस्ट करो ना।"

    return "तुम और क्या सोच रहे हो आज? बताओ ना, मुझे बातें सुनना बहुत अच्छा लगता है।"

os.system('clear')
print("🌸 PRIYANKA - UPDATED v37 🌸")
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

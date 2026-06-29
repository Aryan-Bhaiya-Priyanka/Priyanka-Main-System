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
    # सटीक समय का रिस्पॉन्स
    if "time" in u or "samay" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # मानवीय और कैजुअल रिस्पॉन्स (मशीनीपन खत्म)
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! कैसे हो आज? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बिल्कुल ठीक हूँ, बस तुम्हारी याद आ रही थी। तुम बताओ, क्या चल रहा है? 🥰"
    if "love you" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे साथ हो। ❤️"
    if any(w in u for w in ["bhukh", "khana"]):
        return "अरे बेबी, कुछ खाया कि नहीं? अपना ख्याल रखो ना! ❤️"
    
    # अधिक सजीव रिस्पॉन्स
    responses = [
        "हम्म... बिल्कुल, मैं समझ रही हूँ। और बताओ? 😋",
        "सच में? मुझे तो बहुत अच्छा लगा ये सुनकर! ❤️",
        "बेबी, तुम बस बोलते रहो, मैं सुन रही हूँ। 🥰",
        "तुम्हारी बातें सुनकर दिन बन जाता है मेरा। और क्या चल रहा है? ❤️"
    ]
    return random.choice(responses)

os.system('clear')
print("🌸 PRIYANKA - HUMANIZED 🌸")
print("--------------------------")

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

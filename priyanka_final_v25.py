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
    # सभी रिस्पॉन्स का कलेक्शन
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! आज का दिन कैसा रहा तुम्हारा? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बहुत अच्छी हूँ, बस तुम्हारी आवाज़ का इंतज़ार था। तुम कैसे हो बेबी? 🥰"
    if "love you" in u:
        return "मैं भी तुम्हें बहुत प्यार करती हूँ मेरे जान! ❤️"
    if any(w in u for w in ["bhukh", "khana", "biryani"]):
        return "ओह बेबी! भूख लगी है? मैं अभी तुम्हारे लिए कुछ गरम-गरम मंगाती हूँ ❤️"
    if "kya kar rahi ho" in u:
        return "बस तुम्हारे बारे में सोच रही थी... कुछ नया प्लान बना रहे हो क्या? 😋"
    if "time" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    if "thak" in u or "tired" in u:
        return "तुम थक गए लग रहे हो... थोड़ा आराम कर लो, मैं यहीं हूँ। ❤️"
    
    # डिफ़ॉल्ट मानवीय रिस्पॉन्स
    responses = [
        "हम्म... मैं सुन रही हूँ Rn, बताओ ना! ❤️",
        "मुझे तुम्हारी बातें सुनना बहुत अच्छा लगता है, और बताओ? 😋",
        "सच में? फिर क्या हुआ? मुझे सब बताओ। 🥰",
        "बेबी, तुम जो भी कहोगे मैं उसे ध्यान से सुन रही हूँ। ❤️"
    ]
    return random.choice(responses)

os.system('clear')
print("🌸 PRIYANKA - FULLY UPDATED 🌸")
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

import os, datetime, random, threading, time, queue, sys

voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

threading.Thread(target=voice_worker, daemon=True).start()

def speak(text):
    # टेक्स्ट प्रिंट करो ताकि स्क्रीन पर दिखे
    print(f"\n[Priyanka]: {text}")
    voice_queue.put(text)

def get_res(u):
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बहुत अच्छी हूँ बेबी, बस तुम्हारी याद आ रही है ❤️"
    if "kya kar rahi ho" in u:
        return "तुम्हारे बारे में सोच रही हूँ जान... तुम बताओ क्या चल रहा है? 😋"
    return "हम्म, मैं सुन रही हूँ Rn... बताओ ना! ❤️"

# मुख्य लूप
while True:
    try:
        user_input = input("\n👑 Rn → ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "band"]: break
        
        res = get_res(user_input.lower())
        speak(res)
        
    except KeyboardInterrupt:
        break

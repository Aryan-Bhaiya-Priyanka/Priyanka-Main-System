import os, datetime, random, threading, time, queue

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
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! आज का दिन कैसा रहा तुम्हारा? ❤️"
    if any(w in u for w in ["kaisi ho", "kaise ho"]):
        return "मैं बहुत अच्छी हूँ, बस तुम्हारी आवाज़ का इंतज़ार था। तुम कैसे हो बेबी? 🥰"
    return "हम्म, मैं सुन रही हूँ Rn... बताओ ना! ❤️"

# स्क्रीन को पूरी तरह साफ करने वाला फंक्शन
def clear_screen():
    os.system('clear')
    print("🌸 Priyanka Active 🌸")
    print("---------------------")

clear_screen()
while True:
    user_input = input("\n👑 Rn → ").strip()
    if not user_input: continue
    if user_input.lower() in ["exit", "band"]: break
    
    res = get_res(user_input.lower())
    clear_screen() # हर जवाब के बाद स्क्रीन साफ
    print(f"Priyanka: {res}")
    voice_queue.put(res)

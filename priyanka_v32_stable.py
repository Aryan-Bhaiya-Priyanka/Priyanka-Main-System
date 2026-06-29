import os

# 1. इंस्टॉलेशन
os.system('pkg install termux-api -y > /dev/null 2>&1')

def speak(text):
    # यह सीधे एंड्रॉइड की आवाज का इस्तेमाल करेगा, कोई 'मरीज' वाली फीलिंग नहीं आएगी
    os.system(f'termux-tts-speak -v 1.0 -r 1.0 "{text}"')

def run():
    os.system('clear')
    print("--- PRIYANKA v32: SYSTEM STABLE ---")
    
    welcome = "नमस्ते। अब मैं सीधे तुम्हारे सिस्टम की आवाज का उपयोग कर रही हूँ।"
    print(f"[प्रियंका]: {welcome}")
    speak(welcome)
    
    while True:
        user_in = input("\n[आप]: ")
        if "exit" in user_in: break
        
        reply = "मैं सुन रही हूँ, बताइए।"
        speak(reply)

run()

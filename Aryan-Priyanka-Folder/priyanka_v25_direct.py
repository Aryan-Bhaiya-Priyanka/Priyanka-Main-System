import os

def speak(text):
    # aplay का झंझट खत्म, सीधे espeak से आउटपुट
    os.system(f'espeak -v en-us+f3 -s 150 -p 50 "{text}"')

def clear_screen():
    os.system('clear')

clear_screen()
print("--- PRIYANKA SYSTEM: DIRECT VOICE MODE ---")

# एंट्री होते ही स्वागत मैसेज
welcome_msg = "नमस्ते, मैं प्रियंका हूँ, आपके सिस्टम में आपका स्वागत है।"
print(f"[प्रियंका]: {welcome_msg}")
speak(welcome_msg)

while True:
    user_in = input("\n[आप]: ")
    if user_in.lower() == "exit":
        break
    
    response = "मैं सुन रही हूँ, बताइए।"
    print(f"[प्रियंका]: {response}")
    speak(response)

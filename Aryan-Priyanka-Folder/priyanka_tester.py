import os
import traceback

def speak(text):
    # यह कमांड वॉइस आउटपुट सुनिश्चित करेगी
    os.system(f'termux-tts-speak "{text}"')

def run_test():
    os.system('clear')
    print("--- PRIYANKA SYSTEM: ACTIVE ---")
    try:
        message = "नमस्ते आर्यन भैया, प्रियंका हाजिर है।"
        print(message)
        speak(message)
        
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    run_test()

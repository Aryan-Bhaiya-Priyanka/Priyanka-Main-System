import time
import os
import sys

# Voice trigger function
def speak(text):
    # Using termux-tts-speak for native voice response
    os.system(f'termux-tts-speak "{text}"')

def priyanka_interface():
    os.system('clear')
    print("--- PRIYANKA CORE SYSTEM (VOICE ACTIVE) ---")
    speak("Priyanka system online. Waiting for your strategy.")
    
    while True:
        try:
            strategy = input("User Strategy -> ")
            if strategy.lower() == 'exit':
                speak("Training cycle active. Goodbye.")
                break
            elif strategy:
                response = f"Analyzing {strategy} with Chanakya logic."
                print(f"Priyanka: {response}")
                speak(response)
        except EOFError:
            break

if __name__ == "__main__":
    priyanka_interface()

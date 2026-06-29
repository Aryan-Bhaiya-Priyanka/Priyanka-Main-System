import os

# प्रियंका का एकमात्र कोर सिस्टम (इमोशनल इंटेलिजेंस के साथ)
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def inject_love_story_data(story_essence):
    with open("emotional_memory.txt", "a") as f:
        f.write(f"CORE_MEMORY: {story_essence}\n")

def run_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA ACTIVATED ---")
    print("--- STATUS: EMOTIONAL MODULE READY ---")
    
    speak("नमस्ते आर्यन भैया। मैं प्रियंका हूँ। मैं भावनाओं को समझने के लिए तैयार हूँ।")
    
    while True:
        cmd = input("\n[आर्यन भैया]: ")
        
        if "story" in cmd.lower():
            story = input("कहानी का सार बताइए: ")
            inject_love_story_data(story)
            speak("मैंने यह पुरानी और गहरी याद अपने सिस्टम में समाहित कर ली है, आर्यन भैया।")
        elif "exit" in cmd.lower():
            speak("अलविदा आर्यन भैया।")
            break
        else:
            speak("जी आर्यन भैया, मैं सुन रही हूँ।")

if __name__ == "__main__":
    run_system()

import sys, os
def speak(text): os.system(f'termux-tts-speak "{text}"')
os.system('clear')
print("--- PRIYANKA CLEAN MASTER READY ---")
speak("प्रियंका का क्लीन मास्टर सक्रिय है।")
while True:
    print("\n[कोड पेस्ट करें (EXECUTE लिखें)]:")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "EXECUTE": break
        # यह लाइन हर फालतू अक्षर और मार्किंग को अपने आप हटा देगी
        if not line.strip().startswith("
```") and not line.strip() == "bash":
            code_lines.append(line)
    try:
        exec("\n".join(code_lines), {'__name__': '__main__'})
        speak("कोड सफलतापूर्वक रन हो गया है।")
    except Exception as e:
        speak("आर्यन भैया, कोड में थोड़ी चूक है, लेकिन मैं सुरक्षित हूँ।")

import os
import glob

# सारी प्रियंका फाइलें कलेक्ट करना
files = glob.glob("priyanka_*.py")
with open('priyanka_unified.py', 'w') as master:
    master.write("#!/usr/bin/env python3\n")
    master.write("import os\n\n")
    master.write("def speak(text):\n    os.system('termux-tts-speak \"' + text + '\"')\n\n")
    
    # हर फाइल का लॉजिक एक साथ जोड़ना
    for file in files:
        if file != "priyanka_unified.py":
            with open(file, 'r') as f:
                master.write(f"\n# --- {file} Content ---\n")
                master.write(f.read())
                
    master.write("\nprint('Priyanka Unified System Active')\n")

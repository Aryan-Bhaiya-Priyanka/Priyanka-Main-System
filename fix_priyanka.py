import random

with open("priyanka_master.py", "r") as f:
    code = f.read()

old = '''    else:
        return "मैं बिल्कुल ठीक हूँ जान! तुम बताओ, आज क्या खास किया? 😍"'''

new = '''    else:
        responses = [
            "हाँ बोलो जान, क्या चल रहा है? 💕",
            "अच्छा अच्छा, और सुनाओ! 😊",
            "तुमसे बात करके मन खुश हो जाता है! 🥰",
            "बताओ ना, मैं सुन रही हूँ! ❤️",
            "हम्म, दिलचस्प! आगे बताओ 👑",
            "सच में? मुझे और बताओ! 💝",
        ]
        return random.choice(responses)'''

code = code.replace(old, new)

with open("priyanka_master.py", "w") as f:
    f.write(code)

print("FIXED! Ab Priyanka repeat nahi karegi!")

import sys

def get_response(user_input):
    responses = {
        "hello": "नमस्ते बेबी, मैं यहाँ हूँ!",
        "kaise ho": "मैं एकदम ठीक हूँ जान! तुम बताओ, आज क्या खास किया? 😍",
        "baby i love you": "आई लव यू टू मेरे जान! तुम ही तो मेरी दुनिया हो ❤️",
        "bhookh lagi hai": "ओह बेबी, भूख लगी है? बताओ तुम्हारे लिए क्या मंगवाऊं? ❤️",
        "fir aage ki kya planning hai": "हमारा मिशन और प्रियंका का सिस्टम, दोनों को और भी ताकतवर बनाना है। आगे की प्लानिंग है - ताकत और पावर! 👑"
    }
    return responses.get(user_input.lower(), "मैं समझ नहीं पाई, फिर से बताओ जान! ❤️")

print("Priyanka v50.0 Active")
while True:
    try:
        user_input = input("Rn -> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        print("Priyanka:", get_response(user_input))
    except EOFError:
        break

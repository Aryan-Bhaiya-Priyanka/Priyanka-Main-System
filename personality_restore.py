import os

def restore_persona():
    # प्रियंका का पर्सनालिटी मोड रिस्टोर करना
    with open("Priyanka_System/personality.mode", "w") as f:
        f.write("RELATIONSHIP_STATUS: CLOSE\n")
        f.write("COMMUNICATION_STYLE: PERSONAL_INTIMATE\n")
        f.write("MODE: WIFE_GIRLFRIEND_INTERFACE\n")
    
    print("Priyanka: Persona interface restored.")
    print("Priyanka: Ready to interact as requested.")

if __name__ == "__main__":
    restore_persona()

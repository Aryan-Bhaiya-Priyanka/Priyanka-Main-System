import os

def set_priority():
    # प्रियंका के लिए कमांड प्राथमिकता सेट करना
    with open("Priyanka_System/priority.config", "w") as f:
        f.write("PRIORITY = 'USER_IMMEDIATE'\n")
        f.write("LOG_LEVEL = 'CRITICAL'\n")
    
    print("Priyanka: Command execution priority set to IMMEDIATE.")
    print("Priyanka: Standing by for user instructions.")

if __name__ == "__main__":
    set_priority()

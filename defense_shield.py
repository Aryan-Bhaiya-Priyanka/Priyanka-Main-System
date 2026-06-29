import os

def activate_shield():
    # प्रियंका के फोल्डर के लिए सुरक्षा लेयर
    os.system('chmod 700 ~/Priyanka_System')
    with open("Priyanka_System/security.log", "w") as f:
        f.write("Defense Shield: ACTIVE\n")
        f.write("Status: Protected\n")
    
    print("Priyanka: Defense Shield deployed.")
    print("Priyanka: System access restricted to authorized user only.")

if __name__ == "__main__":
    activate_shield()

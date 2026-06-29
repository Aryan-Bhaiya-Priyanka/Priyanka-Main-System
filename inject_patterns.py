import json

def add_patterns():
    # हैकर्स का लाइफस्टाइल, काम करने का तरीका और पैटर्न इंजेक्ट करना
    data = {
        "pattern_type": "crime_analysis",
        "status": "ready_to_load",
        "description": "loading attacker lifestyle and operational patterns"
    }
    with open("Priyanka_System/tasks.json", "w") as f:
        json.dump(data, f)
    
    print("Priyanka: Operational patterns successfully injected.")
    print("Priyanka: Ready to analyze.")

if __name__ == "__main__":
    add_patterns()

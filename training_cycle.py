import time

def start_training():
    print("Priyanka: Initiating 150-year simulated training cycle.")
    for year in range(1, 151):
        print(f"Priyanka: Training year {year} completed.")
        time.sleep(0.05)
    print("Priyanka: Auto-pilot training cycle finished.")

if __name__ == "__main__":
    start_training()

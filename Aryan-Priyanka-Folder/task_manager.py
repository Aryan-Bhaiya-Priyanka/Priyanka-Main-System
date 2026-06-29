import os

def init_task_manager():
    # प्रियंका के लिए टास्क मैनेजमेंट सेटअप
    with open("Priyanka_System/tasks.txt", "w") as f:
        f.write("TASK_1: ANALYZE_PATTERN\n")
        f.write("STATUS: READY\n")
    
    print("Priyanka: Task Manager initialized.")
    print("Priyanka: System ready for investigative tasks.")

if __name__ == "__main__":
    init_task_manager()

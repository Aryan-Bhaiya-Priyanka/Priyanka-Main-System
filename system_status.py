import os

def check_files():
    path = os.path.expanduser("~/Priyanka/Files")
    files = os.listdir(path)
    print(f"Priyanka System: Active")
    print(f"Total Files Indexed: {len(files)}")

if __name__ == "__main__":
    check_files()

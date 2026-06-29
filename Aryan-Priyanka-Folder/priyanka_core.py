import sys
import io

def run_priyanka():
    print("--- PRIYANKA CORE ACTIVATED ---")
    print("--- MODE: DIRECT EXECUTION READY ---")
    
    while True:
        try:
            print("\n[प्रियंका]: अपना कोड नीचे पेस्ट करें (रन करने के लिए खाली लाइन छोड़कर एंटर दबाएं):")
            code_lines = []
            while True:
                line = input()
                if line == "":
                    break
                code_lines.append(line)
            
            code = "\n".join(code_lines)
            
            if code.strip().lower() == "exit":
                break
                
            # सुरक्षित रनिंग
            buffer = io.StringIO()
            sys.stdout = buffer
            exec(code)
            sys.stdout = sys.__stdout__
            print(f"\n[आउटपुट]:\n{buffer.getvalue()}")
            
        except Exception as e:
            sys.stdout = sys.__stdout__
            print(f"\n[त्रुटि - प्रियंका ने पकड़ लिया]: {e}")

if __name__ == "__main__":
    run_priyanka()

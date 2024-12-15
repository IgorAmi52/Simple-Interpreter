import sys
from interpeter import Interpreter
def main(filename):
    try:
        # Open the file and read its contents
        with open(filename, 'r') as file:
            content = file.read()
        inter = Interpreter(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
    else:
        filename = sys.argv[1] 
        main(filename)

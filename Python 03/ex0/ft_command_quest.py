import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    length: int = len(sys.argv)
    if length == 1:
        print("No argument provided!")
    else:
        print(f"Arguments received: {length - 1}")
        for i in range(1, length):
            print(f"Argument {i}:", sys.argv[i])
    print(f"Total arguments: {length}")

import sys
import typing


def arg_checker() -> bool:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return False
    return True

def main()-> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file: typing.TextIO = open(sys.argv[1], "r")
    except OSError as a:
        print(f"Error opening file {sys.argv[1]}: {a}")
        return

    print("---")
    print()
    content: str = file.read()
    print(content)
    file.close()
    print()
    print("---")
    print(f"File '{sys.argv[1]}' closed.")

    print()
    print("Transform data:")
    print(---)

    splited_content: list[str] = content.split('\n')
    "\n".join(line + '#' for line in splited_content)
    print(splited_content)
    print()
    print(---)
    print("Enter new file name (or empty)")

if __name__ == "__main__":
    if arg_checker() is True:
        main()

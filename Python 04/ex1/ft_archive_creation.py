import sys
import typing


def arg_checker() -> bool:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return False
    return True


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file: typing.TextIO = open(sys.argv[1], "r")
    except OSError as a:
        print(f"Error opening file '{sys.argv[1]}': {a}")
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
    print("---")
    print()

    splited_content: list[str] = content.rstrip("\n").split("\n")

    transformed_content = "\n".join(line + '#' for line in splited_content)
    print(transformed_content)

    print()
    print("---")

    new_file = input("Enter new file name (or empty):")
    if not new_file:
        print("Not saving data.")
        return

    try:
        new_content = open(new_file, "w")
        print(f"Saving data to '{new_file}'")
        new_content.write(transformed_content)
        new_content.close()
        print(f"Data saved in file '{new_file}'")
    except OSError as a:
        print(f"Error handling file '{new_file}': {a}")


if __name__ == "__main__":
    if arg_checker() is True:
        main()

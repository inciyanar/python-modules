import sys


class ArgumentError (Exception):
    def __str__(self) -> str:
        return ("No argument provided")


def main_dude() -> None:
    try:
        if len(sys.argv) <= 1:
            raise ArgumentError()
    except Exception as response:
        print(response)
        return
    new_list = []
    for number in sys.argv[1:]:
        try:
            item = [int(number)]
            new_list += item
        except ValueError:
            print(f"Zort, {number} is not a number. Provide a number.")

    print("Your numbers:", end=" ")
    print(*new_list)
    print(f"Min value of the numbers is: {min(new_list)}")
    print(f"Max value of the numbers is: {max(new_list)}")
    print(f"Total of the numbers is: {sum(new_list)}")
    print(f"Numbers of the numbers is: {len(new_list)}")
    print(f"Average of the numbers is: {sum(new_list)/len(new_list)}")


if __name__ == "__main__":
    print()
    print("Create your own sudoku!")
    print()
    main_dude()

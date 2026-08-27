from alchemy.elements import create_air


def main() -> None:
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(create_air())


if __name__ == "__main__":
    print("== Alembic 3 ==")
    main()

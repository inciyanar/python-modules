import alchemy


def main() -> None:
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(alchemy.create_earth())
    except Exception as error:
        print(error)


if __name__ == "__main__":
    print("== Alembic 4 ==")
    main()

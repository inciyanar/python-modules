from elements import create_water


def main() -> None:
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water:", end=" ")
    print(create_water())


if __name__ == "__main__":
    print("== Alembic 1 ==")
    main()

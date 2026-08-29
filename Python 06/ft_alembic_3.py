from alchemy.elements import create_air


def main() -> None:
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    print("Testing create_air:", end=" ")
    print(create_air())


if __name__ == "__main__":
    print("== Alembic 3 ==")
    main()

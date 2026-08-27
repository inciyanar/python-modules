import alchemy


def main() -> None:
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", end=" ")
    print(alchemy.elements.create_earth())


if __name__ == "__main__":
    print("== Alembic 2 ==")
    main()

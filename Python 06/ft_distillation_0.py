from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to a alchemy/potions.py")
    print("Testing strength_potion:", end=" ")
    print(potions.strength_potion())
    print("Testing healing_potion:", end=" ")
    print(potions.healing_potion())


if __name__ == "__main__":
    main()


from alchemy import potions


def main() -> None:
    print("=== Distillation ===")
    print("Direct access to a alchemy/potions.py")
    print("Testing strength_potion", end="")
    print(potions.strength_potion("Fire", "Water"))
    print("Testing healing_potion", end="")
    print(potions.healing_potion("Fire", "Water"))


if __name__ == "__main__":
    main()

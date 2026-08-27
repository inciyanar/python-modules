from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation ===")
    print("Direct access to a alchemy/potions.py")
    print("Testing strength_potion", end="")
    print(strength_potion("Fire", "Water"))
    print("Testing healing_potion", end="")
    print(healing_potion("Fire", "Water"))


if __name__ == "__main__":
    main()

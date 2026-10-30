from ex0 import FlameFactory, AquaFactory, CreatureFactory


def creature_verifier(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def creature_fighter(cre_1: CreatureFactory, cre_2: CreatureFactory) -> None:
    base1 = cre_1.create_base()
    print(base1.describe())
    print("vs.")
    base2 = cre_2.create_base()
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    creature_verifier(flame_factory)
    print()
    creature_verifier(aqua_factory)
    print()

    print("Testing battle")
    creature_fighter(flame_factory, aqua_factory)
    print()

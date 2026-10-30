from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import creatureError, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    for item in range(len(opponents)):
        for item2 in range((item + 1), len(opponents)):
            print("* Battle *")
            factory, strategy = opponents[item]
            factory2, strategy2 = opponents[item2]
            creat: Creature = factory.create_base()
            creat2: Creature = factory2.create_base()
            print(creat.describe())
            print("vs.")
            print(creat2.describe())
            print("now fight!")
            try:
                strategy.act(creat)
                strategy2.act(creat2)
            except creatureError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            print()


if __name__ == "__main__":
    opponents = [()]
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defnesive) ] ")
    battle([(FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])
    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ] ")
    battle([(FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])
    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())])
    print()

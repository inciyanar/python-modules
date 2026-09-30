from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, creature_Error, BattleStrategy

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy ]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    for item in range(len(opponents)):
        for item2 in range((item +1 ), len(opponents)):
            print("* Battle *")
            factory, strategy = opponents[item]
            factory2, strategy2 = opponents[item2]
            creat = factory.create_base(strategy)
            creat2 = factory2.create_base(strategy2)
            print(creat.describe())
            print("vs.")
            print(creat2.describe())
            print("now fight!")
            print(creat.attack())
            print(creat2.attack())
            strategy.act(creat)
            strategy.act(creat2)




if __name__ == "__main__":
    opponents = [()]
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defnesive) ] ")
    battle([(FlameFactory, NormalStrategy), (HealingCreatureFactory, DefensiveStrategy)])

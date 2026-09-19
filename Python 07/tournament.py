from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, creature_Error

if __name__ == "__main__":
    strategies = [FlameFactory(), NormalStrategy(), AquaFactory()]

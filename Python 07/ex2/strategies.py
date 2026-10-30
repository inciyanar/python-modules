import abc
from ex0.my_creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class creatureError(Exception):
    def __init__(self, creature: Creature, strategy: str) -> None:
        self.creature = creature
        self.strategy = strategy

    def __str__(self) -> str:
        return (f"Invalid Creature '{self.creature.name}'"
                f"for {self.strategy} strategy ")


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creatureError(creature, "Normal")
        print(f"{creature.attack()}")

    def is_valid(self, creature: Creature) -> bool:
        return (True)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creatureError(creature, "Aggressive")
        assert isinstance(creature, TransformCapability)
        print(f"{creature.transform()}")
        print(f"{creature.attack()}")
        print(f"{creature.revert()}")

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creatureError(creature, "Defensive")
        assert isinstance(creature, HealCapability)
        print(f"{creature.attack()}")
        print(f"{creature.heal()}")

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

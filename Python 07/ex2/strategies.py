import abc
from ex0.my_creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability

class creature_Error(Exception):
    def __init__(self, creature: Creature, strategy: str) -> None:
        self.creature = creature
        self.strategy = strategy

    def __str__(self):
        return (f"Invalid Creature '{self.creature.name}' for {self.strategy} strategy ")

class BattleStrategy(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creature_Error(creature, "Normal")
        print(f"{creature.attack()}")

    def is_valid(self, creature: Creature) -> bool:
        return(True)

class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creature_Error(creature, "Aggressive")
        print(f"{creature.transform()}")
        print(f"{creature.attack()}")
        print(f"{creature.revert()}")

    def is_valid(self, creature: Creature) -> bool:
        return(isinstance(creature, TransformCapability))

class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise creature_Error(creature, "Defensive")
        print(f"{creature.attack()}")
        print(f"{creature.heal()}")

    def is_valid(self, creature):
        return(isinstance(creature, HealCapability))

    

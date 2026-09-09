from my_creatures import Creature
from .capabilities import HealCapability

class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return (f"{self.name} uses Vine whip")

    def heal(self, target = None) -> str:
        return (f"{self.name} heals itself for a small amount")

	

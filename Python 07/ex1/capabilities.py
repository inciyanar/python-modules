import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target) -> None:
        pass

class TransformCapability(abc.ABC):
    def __init__(self):
        self.transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        return("Transfer method")

    @abc.abstractmethod
    def revert(self) -> str:
        return("Revert method")

    def attack(self) -> str:
        if self.transformed:
            return ("boosted strike!")
        else:
            return ("attacks normally")


import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        return ("Transfer method")

    @abc.abstractmethod
    def revert(self) -> str:
        return ("Revert method")

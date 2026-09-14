import abc


class BattleStrategy(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def act(self) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    pass


class AgressisveStrategy(BattleStrategy):
    def act(self):
        pass
    def is_valid(self):
        if 

class DefensiveStrategy(BattleStrategy):


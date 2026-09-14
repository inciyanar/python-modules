from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self):
        self.name: str = ""
        self.type: str = ""

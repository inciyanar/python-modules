from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_list: list[tuple[int, str]] = []
        self.rank : int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        to_go: tuple[int, str] = self.data_list[0]
        self.data_list.pop(0)
        return (to_go)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) is True:
            return (True)
        if isinstance(data, list) is True:
            for item in data:
                if isinstance(item, (int, float)) is False:
                    return (False)
            return (True)
        return (False)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) is True:
            raise Exception("Improper numeric data")

        


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    print("Trying to validate input")

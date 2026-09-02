from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_list: list[tuple[int, str]] = []
        self.rank: int = 0

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
        if self.validate(data) is False:
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.data_list.append((self.rank, str(item)))
                self.rank += 1
        else:
            self.data_list.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is True:
            return (True)
        if isinstance(data, list) is True:
            for item in data:
                if isinstance(item, str) is False:
                    return (False)
            return (True)
        return (False)

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is False:
            raise Exception("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.data_list.append((self.rank, item))
                self.rank += 1
        else:
            self.data_list.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) is True:
            for item in data:
                if isinstance(item, str) is False:
                    return (False)
            return (True)
        return (False)

    def ingest(self, data: dict[str: str]) -> None:
        if self.validate(data) is False:
            raise Exception("Improper log data")
     git add    for


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    print("Trying to validate input")

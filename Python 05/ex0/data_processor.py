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
        if not self.data_list:
            raise Exception("List is empty.")
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
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return (False)
            return (True)
        if isinstance(data, list) is True:
            for item in data:
                if self.validate(item) is False:
                    return (False)
            return (True)
        return (False)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) is False:
            raise Exception("Improper log data")
        if isinstance(data, list):
            for item in data:
                new_item = item["log_level"] + ": " + item["log_message"]
                self.data_list.append((self.rank, new_item))
                self.rank += 1
        else:
                output_format = data["log_level"] + ": " + data["log_message"]
                self.data_list.append((self.rank, output_format))
                self.rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()
    numero = NumericProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", numero.validate(42))
    print("Trying to validate input 'Hello':",  numero.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numero.ingest("foo")  # type: ignore
    except Exception as error:
        print("Got exception:", error)
    number_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {number_data}")
    numero.ingest(number_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numero.output()
        print(f"Numeric value {rank}: {value}")

    print()
    print("Testing Text Processor ")
    texto = TextProcessor()
    print("Trying to validate input 'Hello':", texto.validate("Hello"))
    text_data = ["Hello", "Nexus", "World"]
    texto.ingest(text_data)
    print("Processing data:", text_data)
    print("Extracting 1 value...")
    for _ in range(3):
        rank, value = texto.output()
        print(f"Text value {rank}: {value}")
    texto2 = TextProcessor()
    text_data2: list[str] = []
    texto2.ingest(text_data2)
    try:
        texto2.output()
    except Exception as error:
        print(f"{error}")

    print("Testing Log Processor...")
    logo = LogProcessor()
    print("Trying to validate input 'Hello':", logo.validate("Hello"))
    logo.ingest











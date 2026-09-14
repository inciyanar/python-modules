from typing import Any
from abc import ABC, abstractmethod


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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    break
            else:
                print(f"DataStream error -"
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for processor in self.processors:
            nameof_class = type(processor).__name__.replace("Processor",
                                                            " Processor")
            print(f"{nameof_class}: total {processor.rank} items processed,"
                  f"remaining {len(processor.data_list)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")

    my_processors = DataStream()
    my_processors.print_processors_stats()
    print()
    my_processors.register_processor(NumericProcessor())
    batch = ["Hello world", [3.14, -1, 2.71], [
        {"log_level": "WARNING", "log_message":
         "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message":
         "User wil is iconnected"}], 42, ["Hi", "five"]]

    print("Sending first batch of data to stream", batch)
    my_processors.process_stream(batch)
    print()
    my_processors.print_processors_stats()
    print()
    print("Registering other data processors")
    my_processors.register_processor(TextProcessor())
    my_processors.register_processor(LogProcessor())
    my_processors.print_processors_stats()
    print()
    print("Send the same batch again")
    my_processors.process_stream(batch)
    my_processors.print_processors_stats()
    print()
    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        my_processors.processors[0].output()
    for _ in range(2):
        my_processors.processors[1].output()
    for _ in range(1):
        my_processors.processors[2].output()

    my_processors.print_processors_stats()

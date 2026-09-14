from typing import Any
from abc import ABC, abstractmethod
from typing import Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = []
        for rank, value in data:
            values.append(value)
        print(",". join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        sliced = []
        for rank, value in data:
            sliced.append(f'"item_{rank}:", "{value}"')
        json_line = "{" + ", ".join(sliced) + "}"
        print(json_line)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    collected.append(processor.output())
                except Exception:
                    break
            plugin.process_output(collected)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()

    stream = DataStream()
    stream.print_processors_stats()
    print()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print()

    batch = ["Hello world", [3.14, -1, 2.71],
             [{"log_level": "WARNING", "log_message":
               "Telnet access! Use ssh instead"},
              {"log_level": "INFO", "log_message": "User wil is connected"}],
             42, ["Hi", "five"]]

    print("Send first batch of data on stream:", batch)
    stream.process_stream(batch)
    print()
    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()
    print()

    batch2 = [21, ["I love AI", "LLMs are wonderful", "Stay healthy"],
              [{"log_level": "ERROR", "log_message": "500 server crash"},
               {"log_level": "NOTICE", "log_message":
                "Certificate expires in 10 days"}],
              [32, 42, 64, 84, 128, 168], "World hello"]

    print("Send another batch of data:", batch2)
    stream.process_stream(batch2)
    print()
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()

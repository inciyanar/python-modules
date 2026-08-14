import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    users: list = ["hatice", "semih", "taheri", "mustafa"]
    actions: list = ["coding", "vibing", "gaming", "printing", "copying", "pasting"]
    while True:
        result: tuple = (random.choice(users), random.choice(actions))
        yield (result)


def consume_event(event_list: list[tuple[str, str]]) -> typing.Generator[list[tuple[str, str]], None, None]:
    to_delete: tuple[str, str] = random.choice(event_list)
    return_list: list[tuple[str, str]] = []

    print(to_delete)
    for item in event_list:
        if tuple(item) != to_delete:
            return_list += [item]

    print(f"{return_list}")
    while True:
        yield (return_list)


if __name__ == "__main__":
    print("=== Game Data Strem Processor ===")
    result = gen_event()
    for i in range(1000):
        name, action = next(result)
        print(f"Event {i}: Player {name} did action {action}")
    tenevent_list: list[tuple[str, str]] = []
    new_result = gen_event()
    for j in range(10):
        tenevent_list += [next(new_result)]
    print(f"Built list of 10 events: {tenevent_list}")
    printer = consume_event(tenevent_list)
    for _ in range(10):
        print(f"Remains in list: {next(printer)}")

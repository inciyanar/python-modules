import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    users: list[str] = ["hatice", "semih", "taheri", "mustafa"]
    actions: list[str] = [
        "coding", "vibing", "gaming", "printing", "copying", "pasting"
    ]
    while True:
        result: tuple[str, str] = (
            random.choice(users), random.choice(actions)
        )
        yield (result)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randrange(len(event_list))
        to_delete = event_list[index]
        event_list[:] = event_list[:index] + event_list[index + 1:]
        yield to_delete


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
    for event in consume_event(tenevent_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {tenevent_list}")

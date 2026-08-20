def checker(leftover: int) -> None:
    if leftover > 0:
        checker(leftover - 1)
        print(f"Day {leftover}")


def ft_count_harvest_recursive() -> None:
    day: str = input("Days until harvest: ")
    day_int: int = int(day, 10)
    checker(day_int)

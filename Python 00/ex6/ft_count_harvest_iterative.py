def ft_count_harvest_iterative() -> None:
    day: str = input("Days until harvest: ")
    day_int: int = int(day, 10)
    for i in range(1, day_int+1):
        print(f"Day {i}")

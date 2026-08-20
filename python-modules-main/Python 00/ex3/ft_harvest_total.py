def ft_harvest_total() -> None:
    first: str = input("Day 1 harvest: ")
    second: str = input("Day 2 harvest: ")
    third: str = input("Day 3 harvest: ")
    one: int = int(first, 10)
    two: int = int(second, 10)
    three: int = int(third, 10)
    print(f"Total harvest: {one + two + three}")

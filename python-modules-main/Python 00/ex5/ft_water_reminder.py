def ft_water_reminder() -> None:
    day: str = input("Days since last watering: ")
    i: int = int(day, 10)
    if i > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

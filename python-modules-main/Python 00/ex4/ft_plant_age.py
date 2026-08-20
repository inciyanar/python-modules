def ft_plant_age() -> None:
    str_age: str = input("Enter plant age in days: ")
    age: int = int(str_age, 10)
    if age <= 60:
        print("Plant needs more time to grow.")
    elif age > 60:
        print("Plant is ready to harvest!")

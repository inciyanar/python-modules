class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_num = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,", end="")
        print(f" {self.age_num} days years old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_num += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    temp_height: float = plant.height
    plant.show()
    for i in range(7):
        print(f"=== Day {i+1} ===")
        plant.show()
        plant.grow()
        plant.age()
    print(f"Growth this week: {round(plant.height - temp_height, 1)}cm")

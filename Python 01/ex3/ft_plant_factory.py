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
    garden = [("Rose", 25.0, 30),
              ("Oak", 200.0, 365),
              ("Cactus", 5.0, 90),
              ("Sunflower", 80.0, 45),
              ("Fern", 15.0, 120)
              ]
    print("=== Plant Factory Output ===")
    for i in range(5):
        name, height, age = garden[i]
        Plant(name, height, age).show()

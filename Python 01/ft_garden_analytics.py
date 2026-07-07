class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    @staticmethod
    def checker(age):
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

	@classmethod
    def anon(self):
        print(se)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, boolean: str):
        if boolean == "false":
             print(f"{self.name} has not bloomed yet")
        elif boolean == "true":
            print(f"{self.name} is blooming beautifully!")

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.season = harvest_season
        self.value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value :{self.value}")

    def grow(self, height_new: float, day: int):
        self.height = height_new
        self.age += day

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.checker(30)
    Plant.checker(400)
    print()
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "blue")
    flower.show()
    flower.bloom("true")
    flower.bloom("false")
    print()
    print("=== Tree")
    tree = Tree("Oak", 5.0, 10, 5.0)
    tree.show()
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    vegetable.grow(47.0, 20)
    vegetable.show()

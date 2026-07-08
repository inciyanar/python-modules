class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.Age = age
        self.growc: int = 0
        self.agec: int = 0
        self.showc: int = 0
        self.seed: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.Age} days old")
        self.showc += 1

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)
        self.growc += 1

    def age(self) -> None:
        self.Age += 1
        self.agec += 1

    @staticmethod
    def checker(age: int) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anon(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, boolean: str) -> None:
        if boolean == "false":
            print(f"{self.name} has not bloomed yet")
        elif boolean == "true":
            print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


def statics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant.growc} grow,", end="")
    print(f" {plant.agec} age, {plant.showc} show")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk = trunk_diameter
        self.shadec: int = 0

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              "{self.height}cm long and {self.trunk}cm wide.")
        self.shadec += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")

    def statics(self) -> None:
        statics(self)
        print(f"{self.shadec} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)

    def bloom(self, boolean: str) -> None:
        super().bloom(boolean)
        if boolean == "true":
            self.seed += 1
        print(f"Seeds: {self.seed}")


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
    statics(flower)
    flower.grow()
    flower.show()
    flower.bloom("true")
    statics(flower)
    print()

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    statics(tree)
    tree.produce_shade()
    statics(tree)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.bloom("false")
    sunflower.grow()
    sunflower.age()
    sunflower.show()
    sunflower.bloom("true")
    statics(sunflower)

    print("=== Anonymous")
    plant = Plant("selam", 15.0, 5)
    anonim = plant.anon()
    anonim.show()
    statics(anonim)

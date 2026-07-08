class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age_num = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,", end="")
        print(f" {self._age_num} days years old")

    def grow(self) -> None:
        self.height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age_num += 1

    def set_height(self, new: float) -> None:
        if new < 0:
            print(f"{self._name}: ", end="")
            print("Error, height cannot be negative integer value.")
            print("Height update rejected")
        else:
            self._height = new
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, new: int) -> None:
        if new < 0:
            print(f"{self._name}: ", end="")
            print("Error, age cannot be negative integer value.")
            print("Age update rejected")
        else:
            self._age_num = new
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_num


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-55)
    rose.set_age(-2)
    print()
    print("Current state:", end=" ")
    rose.show()

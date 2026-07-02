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

    def get_height(self) -> int:
        if self.height > 0:
            return self.height

    def get_age(self) -> int:
        if self.age > 0:
            return self.age



if __name__ == "__main__":
    print("=== Garden Security System ===")



tup1: tuple = ("selam", 555, "\n", '85')
# print(f"{tup1}")

tup2 = ("selam", 5)
print(tup2[0])
# tup3: tuple = tup1 + tup2
# print(f"{tup3}"

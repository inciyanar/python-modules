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





# def __repr__(self):
#         return "ğ" + self._name + "ğ"

# class Puple(tuple):
#     def __repr__(self):
#         s = ""
#         for e in self:
#             s += str(e) + ", "
#         return s


# class access:
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protacted = b
#         self.__private = c


# x = access("a", "b", "c")
# print(x.public)
# print(x._protacted)
# print(x._access__private)


# if __name__ == "__main__":
#     print("=== Garden Security System ===")


# tup1: tuple = 1, 5
# print(tup1)
# print(isinstance(tup1, tuple))
# list(["selam", 555, "asasd", '85'])

# a = Puple(tup1)
# print(f"{a} aa")

# # tup3: tuple = tup1 + tup2
# # print(f"{tup3}"

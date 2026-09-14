# class Plant:
#     def __init__(self, name: str):
#         self.name = name

#     @staticmethod
#     def show(name):
#         print("selam")

# class Worker(Plant):
#     def __init__(self, name:str, age: int, department: str):
#         super().__init__(name)
#         self.department= department
#     def show(self):
#         super().show()

# if __name__ == "__main__":
#     a = Plant.show("selam")

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
# # print


# from abc import ABC, abstractmethod


# class printer(ABC):
#     def __init__(self):
#         self.number = 0

#     def printer_func(self):
#         pass


# class abc_printer(printer):
#     def printer_func(self):
#         print("hi")


# if __name__ == "__main__":
#     obj = abc_printer()
#     obj.printer_func()
#     print(type(printer))

import abc
from typing import Protocol


class inci:
    def __init__(self):
        self.age = 21

    def ager(self):
        print(f"{self.age + 1}")


class yasin (abc.ABC):
    def ager(self):
        print(f"yasin {self.age - 1}")


class fatih (Protocol):
    pass


if __name__ == "__main__":
    first = inci()
    second = yasin()

    print(type(first))
    print(type(second))
    print(type(inci))
    print(type(yasin))
    print(type(fatih))
    print(type(yasin))

from dataclasses import dataclass


class Dog:
    tricks = []  # 인스턴스 변수

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")

d.add_trick("roll over")

print(d.tricks)


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


john = Employee("John Smith", "computer", 1000)

print(john)

from dataclasses import dataclass
@dataclass
class Person:
    name:str
    age:int
p1 = Person('mahmoud',25)
print(p1.name)
print(p1.age)
print(p1)
from dataclasses import dataclass
@dataclass(order=True)
class Person:
    name:str
    age:int
p1 = Person('Ahmed',28)
p2 = Person('mahmoud',25)
p3 = Person('Ahmed',28)
print( p1 == p2)
print( p1 == p3)
print( p1 > p2)
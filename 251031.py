from dataclasses import dataclass

@dataclass
class Member:
    section: str
    area_in2: float


m1 = Member("3X3X1/2", 3.20)

print(m1)
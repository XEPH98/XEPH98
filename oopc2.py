import math

class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def reset(self) -> None:
        self.move(0,0)
    #A method that accepts another point object.
    def calculate_distance(self, other:"Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    
p1 = Point()
p1.reset()
p2 = Point()
p2.move(5,0)
d22 = p2.calculate_distance(p1)
print(d22)
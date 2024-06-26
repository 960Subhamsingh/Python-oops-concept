from __future__ import annotations

class Box:
    def __init__(self, num1: int , num2: int):
        self.num1 = num1
        self.num2 = num2
    def __repr__(self) -> str:
        return "<class 'Box'>"
   

    def __str__(self) -> str:
        return f"Box =>  num1: {self.num1}, num2: {self.num2}"

    def area(self):
        return self.num1 * self.num2
    
    def __eq__(self, value: object) -> bool:
        "checks if two boxes are equal "
        if not isinstance(value, Box):
            return NotImplemented
        return self.num1 == value.num2  and self.num1 == self.num2
   
    def _add__(self, other: object ):
        if not isinstance(other, Box):
            return NotImplemented
        return self.area + other.area
    
obj = Box(12,45)
obj1 = Box(43,56)
print(obj)
print(obj.area())
print(obj==obj1) # check both ject are equal
print(object)
print(obj+obj1)
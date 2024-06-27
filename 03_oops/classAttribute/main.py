class A:
    def __init__(self, value=0):
        self.a = value
    def __repr__(self) -> str:
        return f'<A({self.value})>'
    def __add__(self, b):
        return self.a + b
     
    def __sub__(self, c):
        return self.a - c

a = A()
print(a + 6215 + 2342)
print(12344-546)

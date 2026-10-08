"""#00021  super() - call the NEXT class in the MRO (usually the parent)."""
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)            # reuse parent's setup, don't copy code
        self.breed = breed
    def speak(self):
        return super().speak() + " -> Woof!"   # extend, don't replace

d = Dog("Tommy", "Labrador")
print(d.name, d.breed)
print(d.speak())

# Without super(): works, but breaks with multiple inheritance
# Animal.__init__(self, name)   # hard-coded parent => fragile

# super() with multiple inheritance (cooperative)
class A:
    def __init__(self): print("A init"); super().__init__()
class B(A):
    def __init__(self): print("B init"); super().__init__()
class C(A):
    def __init__(self): print("C init"); super().__init__()
class D(B, C):
    def __init__(self): print("D init"); super().__init__()
D()
print([k.__name__ for k in D.__mro__])   # super() follows THIS order

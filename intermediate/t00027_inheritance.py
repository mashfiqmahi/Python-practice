"""#00027  Inheritance: single, multilevel, multiple, hierarchical."""
class Person:
    def __init__(self, name): self.name = name
    def intro(self): return f"I am {self.name}"

class Student(Person):                    # single inheritance
    def __init__(self, name, roll):
        super().__init__(name); self.roll = roll
    def intro(self): return super().intro() + f", roll {self.roll}"   # override

class GradStudent(Student):               # multilevel: Person -> Student -> GradStudent
    def thesis(self): return f"{self.name} writes a thesis"

g = GradStudent("Kazi", 101)
print(g.intro()); print(g.thesis())

class Teacher(Person):                    # hierarchical: Person has many children
    def intro(self): return f"Prof. {self.name}"

# Multiple inheritance: one class, many parents
class Swimmer:
    def move(self): return "swims"
    def skill(self): return "swimming"
class Flyer:
    def move(self): return "flies"
    def fly(self): return "flapping"
class Duck(Swimmer, Flyer): pass
d = Duck()
print(d.move(), d.skill(), d.fly())       # move() -> Swimmer wins (left to right)
print([c.__name__ for c in Duck.__mro__])

# Introspection
print(isinstance(g, Person), issubclass(GradStudent, Student), issubclass(Teacher, Student))
print(type(g).__name__, GradStudent.__bases__)

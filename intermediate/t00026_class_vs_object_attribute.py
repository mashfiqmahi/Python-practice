"""#00026  Class attribute (shared) vs object/instance attribute (per object)."""
class Student:
    school = "JU"                  # CLASS attribute - one copy for all
    count = 0

    def __init__(self, name):
        self.name = name           # OBJECT attribute - each object has its own
        Student.count += 1         # modify via the CLASS name

a, b = Student("Rahim"), Student("Nila")
print(a.school, b.school, Student.school)
print("students:", Student.count)
print(a.__dict__, "| class attrs:", [k for k in Student.__dict__ if not k.startswith("__")])

# Changing through the class affects everyone
Student.school = "DU"
print(a.school, b.school)

# Changing through an object creates a NEW object attribute (shadows the class one)
a.school = "BUET"
print(a.school, b.school, Student.school)
del a.school
print(a.school)                    # back to class value

# Trap: mutable class attribute is shared
class Team:
    members = []                   # shared by ALL teams!
    def add(self, m): self.members.append(m)
t1, t2 = Team(), Team()
t1.add("x"); print(t2.members)     # ['x'] surprise
class GoodTeam:
    def __init__(self): self.members = []

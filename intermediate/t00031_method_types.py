"""#00031  Instance vs class vs static methods."""
class Pizza:
    base_price = 200                          # class attribute

    def __init__(self, toppings):
        self.toppings = toppings

    def price(self):                          # INSTANCE method: needs self (one object)
        return self.base_price + 30 * len(self.toppings)

    @classmethod
    def margherita(cls):                      # CLASS method: gets cls; used as alternative constructor
        return cls(["cheese", "tomato"])
    @classmethod
    def set_base(cls, p):                     # change class-level data
        cls.base_price = p

    @staticmethod
    def is_valid_topping(t):                  # STATIC method: no self/cls, just a utility grouped here
        return t in {"cheese", "tomato", "mushroom", "olive"}

p = Pizza(["cheese"])
print(p.price())
m = Pizza.margherita(); print(m.toppings, m.price())
print(Pizza.is_valid_topping("olive"), p.is_valid_topping("pineapple"))
Pizza.set_base(250); print(p.price())

# Classmethod + inheritance: cls is the SUBCLASS
class BigPizza(Pizza): pass
print(type(BigPizza.margherita()).__name__)   # BigPizza  (a staticmethod couldn't do this)

# Typical classmethod: parse from string
class Date:
    def __init__(self, d, m, y): self.d, self.m, self.y = d, m, y
    @classmethod
    def from_string(cls, s):
        d, m, y = map(int, s.split("-")); return cls(d, m, y)
print(Date.from_string("05-10-2026").y)

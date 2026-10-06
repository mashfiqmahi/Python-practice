"""#00001  __str__  -> the *friendly* text of an object (for end users)."""

class Book:
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price

b = Book("Python 101", "Kazi", 450)
print(b)  # no __str__ -> ugly default: <__main__.Book object at 0x...>


class BookWithStr(Book):
    def __str__(self):
        return f"'{self.title}' by {self.author} (Tk {self.price})"


b2 = BookWithStr("Python 101", "Kazi", 450)
print(b2)               # print() calls str(b2) -> b2.__str__()
print(str(b2))          # same thing, explicit
print(f"Book: {b2}")    # f-strings also use __str__
print("Lists use repr, not str ->", [b2])   # see #00013

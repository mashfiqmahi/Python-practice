"""#00016  Type conversion (casting)."""
# Implicit (automatic): Python widens types
print(1 + 2.5, type(1 + 2.5))              # int + float -> float
print(True + True)                          # bool -> int : 2

# Explicit: you call int(), float(), str(), bool(), list() ...
print(int("42"), int(3.99), int("101", 2), int("ff", 16))   # int(3.99) truncates!
print(float("3.14"), str(100), bool(0), bool("hi"))
print(round(3.6), round(2.5), round(3.5))                   # banker's rounding

# Falsy values (everything else is True)
print([bool(v) for v in (0, 0.0, "", [], {}, set(), None)])

# collections
print(list("abc"), tuple([1, 2]), set([1, 1, 2]), list({1: "a"}))
print(dict([("a", 1), ("b", 2)]), dict(zip("ab", [1, 2])))

# chr / ord / bin / hex
print(ord("A"), chr(66), bin(10), hex(255), oct(8))

# Safe conversion pattern
def to_int(text, default=0):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default
print(to_int("12"), to_int("abc"), to_int(None), to_int("3.5"))
print(int(float("3.5")))                    # "3.5" needs float() first

# input() always returns str
# age = int(input("Age: "))

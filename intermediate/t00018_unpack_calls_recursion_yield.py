"""#00018  Packing/unpacking, function calling styles, recursion, yield."""

# ---------- 1) Unpacking ----------
a, b, c = [1, 2, 3]
first, *middle, last = [10, 20, 30, 40, 50]
print(a, b, c, "|", first, middle, last)
a, b = b, a                                   # swap, no temp variable
print("swapped:", a, b)
for i, (name, mark) in enumerate([("Rahim", 80), ("Nila", 90)], start=1):
    print(i, name, mark)

# ---------- 2) Function calling styles ----------
def intro(name, age=20, *hobbies, city="Dhaka", **extra):
    return f"{name}, {age}, {hobbies}, {city}, {extra}"

print(intro("Kazi"))                          # positional
print(intro(age=25, name="Kazi"))             # keyword (order doesn't matter)
print(intro("Kazi", 25, "chess", "cricket", city="Savar", team="JU"))

def power(x, y, /, *, mod=None):              # / = positional-only, * = keyword-only
    return pow(x, y, mod) if mod else x ** y
print(power(2, 10), power(2, 10, mod=1000))

args = (2, 3); kwargs = {"mod": 5}
print(power(*args, **kwargs))                 # PACK on call: * unpacks tuple, ** unpacks dict
print([*range(3), *"ab"], {**{"x": 1}, **{"y": 2}})   # merge containers

# ---------- 3) Recursion (function calls itself) ----------
def factorial(n):
    if n <= 1:                                # BASE CASE (must exist!)
        return 1
    return n * factorial(n - 1)               # smaller problem
print("5! =", factorial(5))

from functools import lru_cache
@lru_cache(maxsize=None)                      # memoization: remember results
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print("fib(50) =", fib(50))

def flatten(items):
    for x in items:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
print(list(flatten([1, [2, [3, 4]], 5])))
import sys; print("recursion limit:", sys.getrecursionlimit())

# ---------- 4) yield (generator) ----------
def countdown(n):
    while n > 0:
        yield n                               # pause here, hand out value, resume later
        n -= 1
gen = countdown(3)
print(next(gen), next(gen), next(gen))
try: next(gen)
except StopIteration: print("exhausted")

def read_big_numbers(limit):                  # lazy: never builds the whole list
    for i in range(limit):
        yield i * i
print(sum(read_big_numbers(1_000_000)))

def echo():                                   # send() talks INTO a generator
    received = None
    while True:
        received = yield received
e = echo(); next(e); print(e.send("hi"), e.send("bye"))

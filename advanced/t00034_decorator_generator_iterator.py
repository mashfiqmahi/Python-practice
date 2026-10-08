"""#00034  Iterator, Generator, Decorator (study in this order)."""

# ================= PART 1: ITERATOR =================
# iterable = has __iter__  |  iterator = has __iter__ AND __next__
nums = [10, 20]
it = iter(nums)                      # what a `for` loop does behind the scenes
print(next(it), next(it))
try: next(it)
except StopIteration: print("StopIteration -> loop ends")

class Countdown:                     # custom iterator
    def __init__(self, start): self.cur = start
    def __iter__(self): return self
    def __next__(self):
        if self.cur <= 0: raise StopIteration
        self.cur -= 1
        return self.cur + 1
print(list(Countdown(3)))

# ================= PART 2: GENERATOR =================
# A function with `yield` = an iterator written the easy way (lazy, tiny memory)
def fib():
    a, b = 0, 1
    while True:                      # infinite is fine - values made on demand
        yield a
        a, b = b, a + b
from itertools import islice
print(list(islice(fib(), 10)))

def read_lines(lines):               # pipeline of generators
    for l in lines: yield l.strip()
def only_errors(lines):
    for l in lines:
        if "ERROR" in l: yield l
log = ["ok\n", "ERROR disk\n", "ok\n", "ERROR net\n"]
print(list(only_errors(read_lines(log))))

# ================= PART 3: DECORATOR =================
# A decorator = a function that takes a function and returns an upgraded function.
import functools, time

def timer(func):
    @functools.wraps(func)           # keep original name/docstring
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - t:.5f}s")
        return result
    return wrapper

@timer                               # same as: slow_sum = timer(slow_sum)
def slow_sum(n):
    """Sum numbers up to n."""
    return sum(range(n))
print(slow_sum(1_000_000), slow_sum.__name__, slow_sum.__doc__)

# Decorator WITH arguments = one extra layer
def repeat(times):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            return [func(*a, **k) for _ in range(times)]
        return wrapper
    return deco
@repeat(3)
def hi(name): return f"hi {name}"
print(hi("Kazi"))

# Practical: login check
def require_login(func):
    @functools.wraps(func)
    def wrapper(user, *a, **k):
        if not user.get("logged_in"): raise PermissionError("login first")
        return func(user, *a, **k)
    return wrapper
@require_login
def dashboard(user): return f"Welcome {user['name']}"
print(dashboard({"name": "Kazi", "logged_in": True}))
try: dashboard({"name": "X"})
except PermissionError as e: print("Error:", e)

# Stacking: bottom decorator runs first
def bold(f): return lambda *a: f"<b>{f(*a)}</b>"
def italic(f): return lambda *a: f"<i>{f(*a)}</i>"
@bold
@italic
def text(s): return s
print(text("hey"))

# Class decorator + built-ins: @property @staticmethod @classmethod @lru_cache @dataclass
from functools import lru_cache
@lru_cache(maxsize=None)
def sq(n): print("computing", n); return n * n
sq(4); sq(4)                         # "computing" printed once

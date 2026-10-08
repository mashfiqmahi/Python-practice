"""#00035  Exception handling."""
def divide(a, b):
    try:
        result = a / b                       # risky code
    except ZeroDivisionError:
        print("cannot divide by zero"); return None
    except (TypeError, ValueError) as e:     # several types, keep the error object
        print("bad input:", e); return None
    else:
        print("no error happened"); return result   # runs only if NO exception
    finally:
        print("finally ALWAYS runs (cleanup)")      # close files, release locks...

print(divide(10, 2)); print(divide(1, 0)); print(divide("a", 2))

# raise your own errors
def set_age(age):
    if not isinstance(age, int): raise TypeError("age must be int")
    if age < 0: raise ValueError(f"age cannot be negative: {age}")
    return age
try: set_age(-5)
except ValueError as e: print("Caught:", e)

# custom exception
class InsufficientFunds(Exception):
    def __init__(self, balance, needed):
        super().__init__(f"balance {balance}, needed {needed}")
        self.balance, self.needed = balance, needed
try: raise InsufficientFunds(100, 500)
except InsufficientFunds as e: print(e, e.needed - e.balance)

# exception chaining
try:
    try: int("x")
    except ValueError as e: raise RuntimeError("config broken") from e
except RuntimeError as e: print(e, "| caused by:", repr(e.__cause__))

# re-raise, and hierarchy (catch specific BEFORE general)
try:
    try: {}["k"]
    except KeyError: print("logging..."); raise
except LookupError as e: print("KeyError is a LookupError:", repr(e))

# Python 3.11+: ExceptionGroup + except*
# EAFP: "Easier to Ask Forgiveness than Permission" - try first, handle failure
d = {"a": 1}
try: v = d["b"]
except KeyError: v = 0
print(v)
# NEVER write a bare `except:` that hides everything. Catch what you can handle.

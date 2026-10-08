"""#00033  Debugging toolbox."""
import logging, traceback, sys

# 1) print / f"{x = }"  - quickest
x = 42
print(f"{x = }")

# 2) assert - sanity checks that should NEVER fail
def average(nums):
    assert len(nums) > 0, "nums must not be empty"
    return sum(nums) / len(nums)
try: average([])
except AssertionError as e: print("AssertionError:", e)

# 3) logging - better than print (levels, timestamps, can switch off)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                    format="%(levelname)s | %(funcName)s | %(message)s")
log = logging.getLogger(__name__)
def buggy_discount(price, pct):
    log.debug("price=%s pct=%s", price, pct)
    result = price - price * pct          # BUG: pct=20 should be 0.20
    log.info("result=%s", result)
    return result
buggy_discount(100, 20)                   # logs show -1900 -> the bug is visible
def fixed_discount(price, pct):
    return price - price * pct / 100
print("fixed:", fixed_discount(100, 20))

# 4) read the traceback (bottom line = error, lines above = call path)
def a(): return b()
def b(): return 1 / 0
try: a()
except Exception:
    print(traceback.format_exc().splitlines()[-1])    # ZeroDivisionError: division by zero
    log.exception("caught with full traceback")       # logs error + traceback

# 5) pdb - the interactive debugger (not auto-run here)
# Put   breakpoint()   anywhere in your code  (or run: python -m pdb file.py)
# Commands:  n next line | s step into | c continue | l list code | p expr print
#            pp expr pretty-print | w where (stack) | b 12 breakpoint at line 12 | q quit
# VS Code: click left of a line number -> red dot -> press F5 (Debug).

# 6) Other tools
# python -X dev file.py        extra runtime checks / warnings
# python -m trace --trace f.py every line executed
# import timeit; timeit.timeit("sum(range(100))", number=10000)   measure speed
# pytest -x --pdb              drop into pdb on the first failing test

# Method: reproduce -> isolate (shrink the code) -> inspect values -> form hypothesis -> fix -> add a test.

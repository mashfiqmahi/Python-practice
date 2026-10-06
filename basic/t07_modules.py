"""#00007  How modules work: concept, import, statements.

A module = any .py file. `import` does 3 things the FIRST time:
  1) finds the file (searches sys.path)   2) runs it top to bottom
  3) caches it in sys.modules (so next import is instant, no re-run)
"""
import sys, importlib

import math                                  # style 1: import whole module
print(math.sqrt(16))

from math import ceil, floor                 # style 2: import specific names
print(ceil(2.1), floor(2.9))

import random as rnd                         # style 3: alias
print(rnd.randint(1, 1))

import mymath_utils                          # our own module (same folder)
from mymath_utils import area_circle as ac
print(mymath_utils.PI, ac(1))

import mymath_utils                          # 2nd import: NOT re-executed
print("cached?", "mymath_utils" in sys.modules)
importlib.reload(mymath_utils)               # force re-run (useful while developing)

print("file:", mymath_utils.__file__)
print("first search path:", sys.path[0])
print("names inside:", [n for n in dir(mymath_utils) if not n.startswith("__")])

# `from x import *` pulls everything - avoid it, it pollutes your namespace.
# `if __name__ == "__main__":` runs code only when file is executed directly.

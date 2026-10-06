"""#00004  Dynamic language vs compiled language.

Compiled (C, C++, Go): source -> machine code BEFORE running (fast, types checked early).
Python: source -> bytecode (.pyc) -> run by the Python Virtual Machine (PVM).
        Types are decided at RUN time => "dynamic".
"""
import dis

def add(a, b):
    return a + b

print("--- bytecode Python generated for add() ---")
dis.dis(add)          # you'll see LOAD_FAST a, LOAD_FAST b, BINARY_OP, RETURN_VALUE

# Dynamic: same function, different types, no declarations needed
print(add(2, 3), add("py", "thon"), add([1], [2]))

# Dynamic: a name can point to different types over time
x = 10;     print(type(x))
x = "ten";  print(type(x))

# Error shows up only when that line RUNS (a compiler would catch it earlier)
try:
    add(1, "a")
except TypeError as e:
    print("Runtime error:", e)

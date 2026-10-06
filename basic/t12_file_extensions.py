"""#00012  Python file extensions.

.py   normal source file
.pyc  compiled BYTECODE, auto-made inside __pycache__/ (e.g. hello.cpython-312.pyc)
.pyo  OLD optimized bytecode. REMOVED in Python 3.5 -> now hello.cpython-312.opt-1.pyc (python -O)
.pyw  script that runs without a console window (Windows)
.pyd  compiled extension DLL (C/C++ module on Windows)
.so   same as .pyd on Linux/Mac
.pyi  type-stub file (only type hints, for editors/mypy)
.ipynb Jupyter notebook
"""
import py_compile, tempfile, os

tmp = tempfile.mkdtemp()
src = os.path.join(tmp, "hello.py")
with open(src, "w") as f:
    f.write("print('hi')\n")

normal = py_compile.compile(src)                  # -> __pycache__/hello.cpython-3xx.pyc
opt1   = py_compile.compile(src, optimize=1)      # -> ...opt-1.pyc  (the modern ".pyo")
opt2   = py_compile.compile(src, optimize=2)      # -> ...opt-2.pyc  (also strips docstrings)
for p in (normal, opt1, opt2):
    print(os.path.relpath(p, tmp))

# Run from the terminal: python -m compileall .   |   python -O file.py
# .pyc is just a cache: it makes IMPORT faster (not the running of your script).

"""#00005  Files + os module (runs safely inside a temp folder)."""
import os, shutil, tempfile
from pathlib import Path

base = tempfile.mkdtemp()                    # throw-away folder
path = os.path.join(base, "notes.txt")

# --- write / append / read (always use `with` => auto close) ---
with open(path, "w", encoding="utf-8") as f:
    f.write("line 1\n")
    f.writelines(["line 2\n", "line 3\n"])
with open(path, "a", encoding="utf-8") as f:
    f.write("line 4\n")
with open(path, encoding="utf-8") as f:
    print("read():", repr(f.read()))
with open(path, encoding="utf-8") as f:
    for line in f:                            # memory-friendly: one line at a time
        print("->", line.strip())

# --- os module ---
print("exists:", os.path.exists(path), "| is file:", os.path.isfile(path))
print("size:", os.path.getsize(path), "bytes")
print("basename:", os.path.basename(path), "| ext:", os.path.splitext(path)[1])
os.makedirs(os.path.join(base, "sub", "deep"), exist_ok=True)
print("listdir:", sorted(os.listdir(base)))
os.rename(path, os.path.join(base, "renamed.txt"))
for root, dirs, files in os.walk(base):
    print("walk:", os.path.relpath(root, base), dirs, files)
print("env HOME:", os.environ.get("HOME"), "| cwd:", os.getcwd())

# --- modern way: pathlib ---
p = Path(base) / "hello.txt"
p.write_text("hi from pathlib")
print(p.read_text(), p.suffix, p.stem)

# --- delete ---
os.remove(os.path.join(base, "renamed.txt"))
shutil.rmtree(base)
print("cleaned up:", not os.path.exists(base))

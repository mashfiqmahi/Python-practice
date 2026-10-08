"""#00036  pickle = save Python objects to bytes/file (serialization)."""
import pickle, tempfile, os

data = {"name": "Kazi", "marks": [90, 85], "tags": {"ml", "py"}, "pt": (1, 2)}

# object <-> bytes
blob = pickle.dumps(data)
print(type(blob), len(blob))
print(pickle.loads(blob) == data)

# object <-> file  (binary mode 'wb' / 'rb' is REQUIRED)
path = os.path.join(tempfile.mkdtemp(), "data.pkl")
with open(path, "wb") as f: pickle.dump(data, f)
with open(path, "rb") as f: print(pickle.load(f))

# custom objects (class must be importable when loading)
class Student:
    def __init__(self, name, gpa): self.name, self.gpa = name, gpa
    def __repr__(self): return f"Student({self.name!r}, {self.gpa})"
s = Student("Nila", 3.9)
print(pickle.loads(pickle.dumps(s)))

# control what is saved
class Conn:
    def __init__(self): self.url, self.socket = "db://x", object()   # socket can't be pickled
    def __getstate__(self):
        d = self.__dict__.copy(); d.pop("socket"); return d
    def __setstate__(self, state):
        self.__dict__.update(state); self.socket = "reconnected"
c = pickle.loads(pickle.dumps(Conn())); print(c.url, c.socket)

# what can't be pickled: lambdas, open files, sockets, generators
try: pickle.dumps(lambda x: x)
except Exception as e: print("Error:", type(e).__name__)

print("highest protocol:", pickle.HIGHEST_PROTOCOL)
# !!! SECURITY: NEVER pickle.load() data from an untrusted source - it can run arbitrary code.
# For sharing with others/other languages use json (safe, text) instead.

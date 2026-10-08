"""#00028  Magic (dunder) methods - make your objects behave like built-ins."""
class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)       # v1 + v2
    def __sub__(self, o): return Vector(self.x - o.x, self.y - o.y)
    def __mul__(self, k): return Vector(self.x * k, self.y * k)           # v * 3
    def __rmul__(self, k): return self * k                                # 3 * v
    def __eq__(self, o): return (self.x, self.y) == (o.x, o.y)            # ==
    def __lt__(self, o): return abs(self) < abs(o)                        # <
    def __abs__(self): return (self.x ** 2 + self.y ** 2) ** 0.5
    def __neg__(self): return Vector(-self.x, -self.y)
    def __bool__(self): return bool(self.x or self.y)
    def __len__(self): return 2
    def __getitem__(self, i): return (self.x, self.y)[i]                  # v[0], also makes it iterable
    def __contains__(self, v): return v in (self.x, self.y)
    def __hash__(self): return hash((self.x, self.y))
    def __call__(self, k): return self * k                                # v(2)

v1, v2 = Vector(1, 2), Vector(3, 4)
print(v1 + v2, v2 - v1, v1 * 3, 3 * v1, -v1)
print(v1 == Vector(1, 2), v1 < v2, abs(v2))
print(bool(Vector(0, 0)), len(v1), v1[0], 2 in v1, list(v1))
print(v1(10), {v1: "hashable"})

# Context manager protocol: __enter__ / __exit__
class Timer:
    def __enter__(self):
        import time; self.t = time.perf_counter(); return self
    def __exit__(self, exc_type, exc, tb):
        import time; print(f"took {time.perf_counter() - self.t:.4f}s"); return False
with Timer(): sum(range(100000))

# Others to know: __new__, __del__, __iter__/__next__, __getattr__, __setattr__,
# __enter__/__exit__, __format__, __index__, __getstate__...
print([m for m in dir(Vector) if m.startswith("__") and m.endswith("__")][:8], "...")

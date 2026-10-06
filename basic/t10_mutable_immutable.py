"""#00010  Mutable vs Immutable.
Immutable (can't change in place): int float str tuple frozenset bool bytes
Mutable   (can change in place)  : list dict set bytearray custom objects
"""
# --- immutable: "changing" creates a NEW object ---
a = "hi"; print(id(a))
a += "!"; print(id(a), "<- different id, new string")
try:
    a[0] = "H"
except TypeError as e:
    print("Error:", e)

# --- mutable: same object changes ---
nums = [1, 2]; print(id(nums))
nums.append(3); print(id(nums), "<- same id", nums)

# Aliasing: two names, ONE list
x = [1, 2]; y = x
y.append(99)
print("x =", x, "(changed through y!)")

# Copy to avoid it
import copy
orig = [[1, 2], [3]]
shallow = orig.copy()            # copies outer list only
deep = copy.deepcopy(orig)       # copies everything
orig[0].append("X")
print("shallow:", shallow, "| deep:", deep)

# Tuple is immutable BUT can hold mutable things
t = ([1], 2)
t[0].append(5); print(t)

# dict keys must be immutable (hashable)
d = {(1, 2): "ok"}
try:
    d[[1, 2]] = "bad"
except TypeError as e:
    print("Error:", e)

# Famous bug: mutable default argument
def bad(item, bucket=[]):
    bucket.append(item); return bucket
print(bad(1), bad(2))            # [1] then [1, 2] (shared!)
def good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item); return bucket
print(good(1), good(2))          # [1] [2]

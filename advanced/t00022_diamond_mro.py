"""#00022  Diamond problem + MRO (Method Resolution Order, C3 algorithm).

        A
       / \
      B   C       D inherits B and C, both inherit A.
       \ /        Which hello() does D get? Python answers with the MRO.
        D
"""
class A:
    def hello(self): print("A.hello")
class B(A):
    def hello(self): print("B.hello"); super().hello()
class C(A):
    def hello(self): print("C.hello"); super().hello()
class D(B, C):
    def hello(self): print("D.hello"); super().hello()

D().hello()                              # D -> B -> C -> A  (A runs ONCE, not twice)
print([k.__name__ for k in D.__mro__])
print(D.mro())

# ---- C3 linearization written by hand ----
# L[D] = D + merge( L[B], L[C], [B, C] )
# merge rule: take the first head that does NOT appear in the TAIL of any other list; repeat.
def c3_merge(seqs):
    seqs, result = [list(s) for s in seqs if s], []
    while seqs:
        for seq in seqs:
            cand = seq[0]
            if not any(cand in s[1:] for s in seqs):
                break
        else:
            raise TypeError("inconsistent hierarchy")
        result.append(cand)
        seqs = [[x for x in s if x != cand] for s in seqs]
        seqs = [s for s in seqs if s]
    return result

def linearize(cls):
    if cls is object: return [object]
    bases = list(cls.__bases__)
    return [cls] + c3_merge([linearize(b) for b in bases] + [bases])

print([k.__name__ for k in linearize(D)])
assert linearize(D) == list(D.__mro__)   # matches Python's own answer

# Order of parents matters
class E(C, B): pass
print([k.__name__ for k in E.__mro__])   # E C B A object

# Impossible hierarchies are rejected
try:
    class X(A, B): pass                  # A before B contradicts B(A)
except TypeError as e:
    print("Error:", e)

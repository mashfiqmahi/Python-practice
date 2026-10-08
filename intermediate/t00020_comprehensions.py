"""#00020  Comprehensions: list, dict, set, generator."""
nums = range(1, 11)

# [expression for item in iterable if condition]
print([n * n for n in nums])
print([n for n in nums if n % 2 == 0])
print(["even" if n % 2 == 0 else "odd" for n in range(4)])    # if/else goes BEFORE for
print([c.upper() for c in "abc"])

# nested loops
print([(i, j) for i in range(2) for j in range(3)])
matrix = [[1, 2, 3], [4, 5, 6]]
print([x for row in matrix for x in row])                      # flatten
print([[row[i] for row in matrix] for i in range(3)])          # transpose

# dict comprehension {key: value for ...}
print({n: n ** 2 for n in range(5)})
words = ["apple", "kiwi", "banana"]
print({w: len(w) for w in words})
print({v: k for k, v in {"a": 1, "b": 2}.items()})             # invert dict

# set comprehension (unique)
print({len(w) for w in words})

# generator expression: ( ) -> lazy, memory friendly
g = (n * n for n in range(1_000_000))
print(next(g), next(g), sum(n for n in range(10)))

# Readability rule: if it needs more than 1 condition + 1 loop, use a normal for loop
primes = [n for n in range(2, 30) if all(n % d for d in range(2, int(n ** .5) + 1))]
print(primes)

"""#00017  map / filter / reduce - functional tools for lists."""
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map(func, iterable): transform EVERY item
squares = list(map(lambda n: n ** 2, nums))
print("map   :", squares)
print("map 2 lists:", list(map(lambda a, b: a + b, [1, 2], [10, 20])))
print("map str:", list(map(str.upper, ["a", "b"])))

# filter(func, iterable): KEEP items where func returns True
evens = list(filter(lambda n: n % 2 == 0, nums))
print("filter:", evens)

# reduce(func, iterable, start): fold many items into ONE value
# step by step: ((((1+2)+3)+4)+5)+6
total = reduce(lambda acc, n: acc + n, nums)
print("reduce sum:", total)
print("reduce max:", reduce(lambda a, b: a if a > b else b, nums))
print("reduce with start:", reduce(lambda acc, n: acc * n, nums, 1))   # factorial-like

# Chain them: sum of squares of even numbers
print("chain :", reduce(lambda a, b: a + b, map(lambda n: n * n, filter(lambda n: n % 2 == 0, nums))))

# map/filter return lazy iterators in Python 3 -> wrap with list()
m = map(abs, [-1, -2]); print(m, list(m))

# Pythonic alternative (often more readable):
print([n ** 2 for n in nums if n % 2 == 0], sum(n * n for n in nums if n % 2 == 0))

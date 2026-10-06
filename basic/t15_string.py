"""#00015  Strings: creation, indexing, slicing, methods, formatting."""
s = "Hello, Python"
print(len(s), s[0], s[-1])
print(s[0:5], s[7:], s[::-1], s[::2])      # [start:stop:step]

# Strings are immutable -> methods RETURN new strings
print(s.upper(), s.lower(), s.title(), s.swapcase())
print("  pad  ".strip(), "xxhixx".strip("x"))
print(s.replace("Python", "World"))
print(s.find("Py"), s.find("zzz"), s.count("l"))   # find -> -1 if missing
print(s.startswith("He"), s.endswith("on"), "Py" in s)

# split / join
words = "apple,banana,cherry".split(",")
print(words, "-".join(words))
print("a b  c".split(), "line1\nline2".splitlines())

# checks
print("123".isdigit(), "abc".isalpha(), "ab1".isalnum(), "  ".isspace())

# alignment
print("7".zfill(3), "hi".center(10, "*"), "hi".ljust(5, ".") + "|")

# formatting
name, age = "Kazi", 24
print(f"{name} is {age}")
print("{} is {}".format(name, age))

# raw + multiline + escape
print(r"C:\new\table", "tab\there", 'it\'s', "it's")

# join is MUCH faster than += in loops
parts = [str(i) for i in range(5)]
print("".join(parts))

# useful quick programs
word = "level"
print("palindrome" if word == word[::-1] else "not palindrome")
from collections import Counter
print(Counter("banana").most_common(2))

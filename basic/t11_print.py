"""#00011  print() command - all the useful options."""
import sys

print("Hello", "World")                   # separator default = space
print("a", "b", "c", sep="-")             # a-b-c
print("no newline", end=" | ")            # end default = "\n"
print("same line")
print("to stderr", file=sys.stderr)       # send to error stream
print("flush now", flush=True)            # useful for progress output

name, mark, pi = "Kazi", 87.456, 3.14159265
print("Name: %s, Mark: %.1f" % (name, mark))        # old style
print("Name: {}, Mark: {:.1f}".format(name, mark))  # .format
print(f"Name: {name}, Mark: {mark:.1f}")            # f-string (best)
print(f"{name!r}")                                  # repr inside f-string
print(f"{pi:.3f} | {1234567:,} | {0.256:.1%}")      # 3.142 | 1,234,567 | 25.6%
print(f"[{name:>10}] [{name:<10}] [{name:^10}]")    # right/left/center align
print(f"[{42:05d}] [{255:b}] [{255:x}] [{1e6:e}]")  # zero-pad, binary, hex, sci
x = 5
print(f"{x = }")                                    # debug style: x = 5
print("Tab\tseparated\nNew line", r"raw \n stays")
print(*[1, 2, 3])                                   # unpack list as arguments
print("""multi
line""")

"""#00032  Unicode support. Python 3 str = Unicode text; bytes = raw data."""
import unicodedata

bn = "বাংলা"
print(bn, len(bn))                           # 5 code points
print([hex(ord(c)) for c in bn])             # every char has a number (code point)
print(chr(0x09AC), "\u0995", "\N{GREEK SMALL LETTER ALPHA}", "😀")

# encode: str -> bytes   decode: bytes -> str   (always say which encoding!)
data = bn.encode("utf-8")
print(data, len(data), "bytes")              # Bangla letters take 3 bytes each in UTF-8
print(data.decode("utf-8"))
try:
    data.decode("ascii")
except UnicodeDecodeError as e:
    print("Error:", e)
print("café".encode("ascii", errors="replace"), "café".encode("ascii", errors="ignore"))

# normalization: same-looking text can be different code points
a, b = "é", "e\u0301"
print(a == b, len(a), len(b))
print(unicodedata.normalize("NFC", b) == a)

print(unicodedata.name("ক"), unicodedata.category("ক"))
print("ß".upper(), "İ".lower() == "i̇", "straße".casefold())   # use casefold() to compare text

# Files: ALWAYS pass encoding="utf-8"
import tempfile, os
p = os.path.join(tempfile.mkdtemp(), "bn.txt")
with open(p, "w", encoding="utf-8") as f: f.write("আমি বাংলায় গান গাই\n")
print(open(p, encoding="utf-8").read().strip())

"""#00037  Regular expressions (re module). Always use RAW strings r"..." """
import re

text = "Call Kazi at 01712-345678 or Nila at 01911-222333. Email: kazi@ju.edu.bd"

# search -> first match | match -> must match at START | fullmatch -> whole string
print(re.search(r"\d{5}-\d{6}", text).group())
print(re.match(r"Call", text) is not None, re.fullmatch(r"\d+", "123") is not None)

# findall / finditer
print(re.findall(r"\d{5}-\d{6}", text))
for m in re.finditer(r"[A-Z][a-z]+", text):
    print(m.group(), m.start(), m.end())

# Cheat sheet
#  .  any char     \d digit   \w word char   \s space      \D \W \S = opposite
#  ^  start        $  end     \b word edge
#  *  0+   +  1+   ?  0 or 1  {3}  exactly 3   {2,5} range
#  [abc] set  [^abc] not in set   (a|b) either   (...) group

# groups
m = re.search(r"(\d{5})-(\d{6})", text)
print(m.group(0), m.group(1), m.group(2), m.groups())
m = re.search(r"(?P<user>\w+)@(?P<domain>[\w.]+)", text)      # named groups
print(m["user"], m["domain"], m.groupdict())

# sub (replace) and split
print(re.sub(r"\d", "#", "a1b22"))
print(re.sub(r"(\w+)@(\w+)", r"\2 at \1", "kazi@ju"))        # back-references
print(re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "3 apples, 10 pears"))
print(re.split(r"[,;\s]+", "a, b;c  d"))

# greedy vs lazy
html = "<b>bold</b><i>it</i>"
print(re.findall(r"<.+>", html), re.findall(r"<.+?>", html))

# flags + compile (faster when reused)
print(re.findall(r"^\w+", "one\ntwo", re.M), re.search("PYTHON", "I love python", re.I).group())
phone = re.compile(r"^(?:\+88)?01[3-9]\d{8}$")      # Bangladeshi mobile number
for n in ("01712345678", "+8801911222333", "0121"): print(n, bool(phone.match(n)))

# validate email (simple)
email = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")
print(bool(email.match("kazi@ju.edu.bd")), bool(email.match("bad@")))

# lookahead
print(re.findall(r"\d+(?= taka)", "50 taka, 20 dollar, 70 taka"))

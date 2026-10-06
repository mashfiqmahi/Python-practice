"""#00008  Keywords = reserved words you cannot use as variable names."""
import keyword

print(len(keyword.kwlist), "keywords:")
print(keyword.kwlist)
print("soft keywords:", keyword.softkwlist)   # match, case, _, type
print(keyword.iskeyword("for"), keyword.iskeyword("print"))   # True False

# Quick meaning guide
groups = {
    "values":      "True False None",
    "logic":       "and or not is in",
    "branching":   "if elif else match",
    "loops":       "for while break continue",
    "functions":   "def return lambda yield",
    "classes":     "class",
    "errors":      "try except finally raise assert",
    "scope":       "global nonlocal",
    "import":      "import from as",
    "other":       "with pass del async await",
}
for k, v in groups.items():
    print(f"{k:10} {v}")

# class = 5   # SyntaxError: can't use a keyword as a name
# `print` is NOT a keyword (it's a built-in function) - you *can* overwrite it. Don't!

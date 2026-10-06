"""#00002  Comments  (this triple-quoted text at the top is a *docstring*)."""

# 1) Single-line comment: Python ignores everything after '#'
x = 10  # 2) inline comment (put 2 spaces before '#')

# 3) Multi-line comments: just use several '#' lines.
# Python has NO real block-comment syntax.
# (A bare triple-quoted string works but is really a string, not a comment.)

def area(r):
    """Docstring: describes WHAT the function does. Available at runtime."""
    return 3.14159 * r * r

print(area.__doc__)   # docstrings are stored in __doc__
help(area)            # help() prints the docstring nicely

# 4) Special tags people search for: TODO, FIXME, NOTE
# TODO: add input validation
# 5) Good comment explains WHY, not WHAT:
# BAD : x = x + 1  # add 1 to x
# GOOD: x = x + 1  # skip header row

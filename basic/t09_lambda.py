"""#00009  Lambda = tiny anonymous one-line function.  lambda args: expression"""

square = lambda x: x * x
print(square(5))                                  # same as def square(x): return x*x
print((lambda a, b: a + b)(2, 3))                 # call immediately
print((lambda x, y=10: x + y)(5))                 # default args work
grade = lambda m: "Pass" if m >= 40 else "Fail"   # conditional expression
print(grade(55), grade(20))

# Where lambdas shine: as `key=` or with map/filter
students = [("Rahim", 82), ("Karim", 67), ("Nila", 91)]
print(sorted(students, key=lambda s: s[1], reverse=True))
print(max(students, key=lambda s: s[1]))
print(list(map(lambda n: n * 2, [1, 2, 3])))
print(list(filter(lambda n: n % 2 == 0, range(10))))

# Classic trap: late binding in loops
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])                       # [2, 2, 2] (!)
funcs = [lambda i=i: i for i in range(3)]         # fix: freeze i as default
print([f() for f in funcs])                       # [0, 1, 2]

# Limits: only ONE expression, no statements. Use `def` when it gets complex.

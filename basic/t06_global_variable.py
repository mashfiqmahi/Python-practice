"""#00006  Global variables, `global`, and `nonlocal` (LEGB rule)."""
counter = 0                      # global variable

def read_only():
    print("read global:", counter)       # reading needs no keyword

def broken():
    try:
        counter += 1                      # Python thinks counter is LOCAL here
    except UnboundLocalError as e:
        print("Error:", e)

def increment():
    global counter                        # say: "I mean the global one"
    counter += 1

read_only(); broken(); increment(); increment()
print("after 2 increments:", counter)

def shadow():
    counter = 999                         # new LOCAL variable, global unchanged
    print("local:", counter)
shadow(); print("global still:", counter)

# nonlocal: for variables in an *enclosing function* (not global)
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter(); c(); c()
print("closure counter:", c())

# Scope order = LEGB: Local -> Enclosing -> Global -> Built-in
# Tip: avoid globals in big programs; pass arguments / return values instead.

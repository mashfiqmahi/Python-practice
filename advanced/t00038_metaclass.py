"""#00038  Metaclass: the class of a class.

Everything is an object. obj is made by its CLASS. A class is made by its METACLASS.
Default metaclass = type.     5 -> int -> type      obj -> Class -> type
"""
print(type(5), type(int), type(type))               # int, type, type

# 1) Make a class WITHOUT the `class` keyword: type(name, bases, namespace)
Dog = type("Dog", (), {"sound": "woof", "speak": lambda self: self.sound})
print(Dog().speak(), Dog.__name__)

# 2) Custom metaclass: runs when a CLASS is created
class Meta(type):
    def __new__(mcs, name, bases, ns):
        print(f"creating class {name}")
        ns["created_by"] = "Meta"                    # inject an attribute
        return super().__new__(mcs, name, bases, ns)
class Foo(metaclass=Meta): pass
print(Foo.created_by)

# 3) Enforce rules on every subclass
class MustHaveDoc(type):
    def __new__(mcs, name, bases, ns):
        if bases and not ns.get("__doc__"):          # skip the base class itself
            raise TypeError(f"{name} needs a docstring")
        return super().__new__(mcs, name, bases, ns)
class Base(metaclass=MustHaveDoc): pass
class Good(Base):
    """ok"""
try:
    class Bad(Base): pass
except TypeError as e: print("Error:", e)

# 4) Singleton via metaclass (controls object creation with __call__)
class Singleton(type):
    _inst = {}
    def __call__(cls, *a, **k):
        if cls not in cls._inst:
            cls._inst[cls] = super().__call__(*a, **k)
        return cls._inst[cls]
class Config(metaclass=Singleton): pass
print(Config() is Config())

# 5) Auto-registry of plugins
class Registry(type):
    classes = {}
    def __init__(cls, name, bases, ns):
        super().__init__(name, bases, ns)
        Registry.classes[name] = cls
class PluginA(metaclass=Registry): pass
class PluginB(PluginA): pass
print(list(Registry.classes))

# Simpler modern alternative for many cases: __init_subclass__ or class decorators
class Plugin:
    registry = []
    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw); Plugin.registry.append(cls.__name__)
class X(Plugin): pass
class Y(Plugin): pass
print(Plugin.registry)
# Rule: "Metaclasses are deeper magic than 99% of users should ever worry about." (Tim Peters)

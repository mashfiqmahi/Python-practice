"""#00030  Public / protected / private - by NAMING CONVENTION in Python."""
class Account:
    bank = "JU Bank"            # public

    def __init__(self, owner, balance):
        self.owner = owner      # public      : name           -> use freely
        self._branch = "Savar"  # protected   : _name          -> "internal, please don't touch" (convention only)
        self.__balance = balance  # private   : __name         -> name-mangled to _Account__balance

    def deposit(self, amt):
        self.__balance += amt
    def get_balance(self):
        return self.__balance
    def __audit(self):          # private method
        return "audit ok"
    def run_audit(self):
        return self.__audit()

class Savings(Account):
    def peek(self):
        return self._branch                 # protected: subclasses may use it
    def try_private(self):
        try: return self.__balance          # looks for _Savings__balance
        except AttributeError as e: return f"Error: {e}"

a = Account("Kazi", 1000)
print(a.owner, a._branch)                   # works (convention only)
try: print(a.__balance)
except AttributeError as e: print("Error:", e)
a.deposit(500); print(a.get_balance(), a.run_audit())

print([n for n in dir(a) if "balance" in n])  # ['_Account__balance'] <- mangled name
print(a._Account__balance)                    # still reachable! "private" = hard to hit by accident
s = Savings("Nila", 10); print(s.peek(), s.try_private())
# Python philosophy: "We are all consenting adults" - privacy is a signal, not a lock.

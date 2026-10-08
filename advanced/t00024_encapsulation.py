"""#00024  Encapsulation = bundle data + methods, and PROTECT the data's rules."""
class BankAccount:
    MIN_BALANCE = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = 0                 # hidden state
        self.__history = []
        if balance: self.deposit(balance)

    @property
    def balance(self):                     # read-only view
        return self.__balance

    def deposit(self, amount):
        if amount <= 0: raise ValueError("deposit must be positive")
        self.__balance += amount
        self.__history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0: raise ValueError("withdraw must be positive")
        if self.__balance - amount < self.MIN_BALANCE:
            raise ValueError("insufficient funds")
        self.__balance -= amount
        self.__history.append(("withdraw", amount))

    def statement(self):
        return list(self.__history)        # return a COPY so outsiders can't edit history

acc = BankAccount("Kazi", 1000)
acc.deposit(500); acc.withdraw(200)
print(acc.balance, acc.statement())

try: acc.balance = 1_000_000               # no setter -> blocked
except AttributeError as e: print("Error:", e)
try: acc.withdraw(10_000)
except ValueError as e: print("Error:", e)
acc.statement().append(("hack", 1))        # modifies the copy only
print(len(acc.statement()))

# Why? Rules (no negative balance, history log) live in ONE place. Callers can't break them.
# __slots__ also limits attributes (bonus):
class Tiny:
    __slots__ = ("x",)
t = Tiny(); t.x = 1
try: t.y = 2
except AttributeError as e: print("Error:", e)

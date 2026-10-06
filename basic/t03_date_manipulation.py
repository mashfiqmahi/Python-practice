"""#00003  Date manipulation with the datetime module."""
from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()
print("Today:", today, "| Now:", now)

d = date(2026, 10, 5)
print(d.year, d.month, d.day, d.strftime("%A"))      # Monday

# strftime = date -> string      strptime = string -> date
print(d.strftime("%d/%m/%Y"))          # 05/10/2026
print(d.strftime("%B %d, %Y"))         # October 05, 2026
parsed = datetime.strptime("25-12-2026 14:30", "%d-%m-%Y %H:%M")
print("Parsed:", parsed)

# Arithmetic with timedelta
print(d + timedelta(days=30))
print(d - timedelta(weeks=2))
deadline = date(2026, 12, 31)
print("Days left:", (deadline - d).days)
print("Is before deadline?", d < deadline)

# Useful tricks
print(d.replace(day=1))                      # first day of month
print(d.isoformat(), date.fromisoformat("2026-01-15"))
birth = date(2000, 3, 20)
age = d.year - birth.year - ((d.month, d.day) < (birth.month, birth.day))
print("Age:", age)

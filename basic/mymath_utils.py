"""Helper module used by t00007_modules.py"""
PI = 3.14159

def area_circle(r):
    return PI * r * r

if __name__ == "__main__":
    print("running directly:", area_circle(2))
else:
    print("mymath_utils imported as module named:", __name__)

from datetime import date
from utils import add, subtract
from utils import add, subtract, multiply
print("My name is Ashraful")
print("Today's date is:", date.today())

try:
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))

    print("Invalid test:", add("10", 5))
except TypeError as error:
    print("Error:", error)
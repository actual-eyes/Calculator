# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   print x, "+", y, "=", x + y

def subtract(x, y):
   print x, "-", y, "=", x - y

def multiply(x, y):
   print x, "*", y, "=", x * y

def divide(x, y):
   print x, "/", y, "=", x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

if choice == 1:
   add(input("Add this: "),input("to this: "))

elif choice == 2:
   subtract(input("Subtract this: "),input("from this: "))

elif choice == 3:
   multiply(input("Multiply this: "),input("by this: "))

elif choice == 4:
   divide(input("Divide this: "),input("by this: "))

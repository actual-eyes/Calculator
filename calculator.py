import math

def add(x, y):
   print x, "+", y, "=", x + y

def subtract(x, y):
   print x, "-", y, "=", x - y

def multiply(x, y):
   print x, "*", y, "=", x * y

def divide(x, y):
   print x, "/", y, "=", x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

   choice = (input("Enter choice(1/2/3/4):"))

   if choice == 1:
      add(float(input("Add this: ")),float(input("to this: ")))

   elif choice == 2:
      subtract(float(input("Subtract this: ")),float(input("from this: ")))

   elif choice == 3:
      multiply(float(input("Multiply this: ")),float(input("by this: ")))

   elif choice == 4:
      divide (float(input("Divide this: ")),float(input("by this: ")))
   else:
      if choice != (1, 2, 3, 4):
         print "Please choose 1, 2, 3, or 4."

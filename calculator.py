def add(x, y):
    x + y

def subtract(x, y):
    x - y

def multiply(x, y ):
    x * y

def divide(x, y):
    x / y

print "Select operation."
print "1. Add"
print "2. Subtract"
print "3. Multiply"
print "4. Divide"

choice = raw_input("Pick 1, 2, 3, or 4: ")


num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: "))

if choice == "1":
    print num1 + "+" + num2 + "=" + add(num1, num2)
elif choice == "2":
    print num1 + "-" + num2 + "=" + subtract(num1, num2)
elif choice == "3":
    print num1 + "*" + num2 + "=" + multiply(num1, num2)
elif choice == "4":
    print num1 + "/" + num2 + "=" + divide(num1, num2)
else:
    print "Invalid input"

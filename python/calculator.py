num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator '*,/,-,+': ")

def multiply():
    print(num1 * num2)

def divide():
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")

def minus():
    print(num1 - num2)

def plus():
    print(num1 + num2)

if operator == '*':
    multiply()
elif operator == '/':
    divide()
elif operator == '-':
    minus()
elif operator == '+':
    plus()
else:
    print("Do it correctly!")
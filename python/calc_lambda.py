a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
multiply=lambda a, b: a * b
divide=lambda a, b: a/b if b !=0 else "Cannot divide by zero!"
minus=lambda a, b: a - b
plus=lambda a, b: a + b
print(multiply(a, b))
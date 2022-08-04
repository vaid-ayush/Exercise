# Program to print the sum of two numbers if their product is greater than 1000; else print their product

a = int(input("Enter first no.: "))
b = int(input("Enter second no. : "))
if a * b < 1000:
    print(a * b)
else:
    print(a + b)

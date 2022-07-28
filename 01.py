'''Program to print the sum of two numbers if their product is greater than 1000; else print their product

a=int(input("Enter first no.: "))
b=int(input("Enter second no. : "))
if a*b<1000:
    print(a*b)
else:
    print(a+b)
'''


def mul(num1, num2):
    p = num1*num2
    if p < 1000:
        print(p)
    else:
        print(num1+num2)


mul(30, 20)
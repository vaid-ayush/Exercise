# Check Palindrome Number

x = int(input("Enter the number:"))
y = 0
z=x
while x > 0:
    rem = x % 10
    y = (y*10) + rem
    x = x//10

if z == y:
    print(True)
else:
    print(False)

def pal(num):
    rev=0
    orig=num
    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num=num//10

    if orig == rev:
        print("Number is pallindrome")
    else:
        print("Number is not pallindrome")

pal(121)
pal(120)

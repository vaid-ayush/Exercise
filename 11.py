# Write a Program to extract each digit from an integer in the reverse order

x = int(input("Enter the number"))

rev=0
while x > 0:
    rev = x % 10
    x = x//10
    print(rev, end=' ')

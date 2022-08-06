# Reverse a given integer number

x = int(input("Enter the number: "))
#x = 123974
rev = 0
while x > 0:
    rem = x % 10
    rev = rev * 10 + rem
    x = x // 10
print(rev)

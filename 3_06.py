# Count the total number of digits in a number

x = int(input("Enter the number"))
count = 0
while x != 0:
    x = x // 10
    count += 1

print(count)

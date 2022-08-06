# Sum of numbers upto n

i = int(input("Enter the number"))
print("Number is",i)

s = 0
for x in range(0,i+1):
    s += x

print("Sum is", s)

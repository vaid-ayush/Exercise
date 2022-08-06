# Write a program to print multiplication table of a given number

x = int(input("Enter the number"))
z=1
for i in range(1,x+1):
    for j in range(1,11):
        z = i * j
    print(z)

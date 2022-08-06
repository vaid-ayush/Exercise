# Calculate the cube of all numbers from 1 to a given number

num = int(input("Enter the number:"))
for i in range(1, num+1):
    x = i ** 3
    print("Cube of ", i , "is", x)
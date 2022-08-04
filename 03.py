# Write a program to accept a string from the user and display characters that are present at an even index number.

string = input("Enter the string:")
x = len(string)
print(type(x))
for i in range(0, x-1, 2):
    print(string[i])

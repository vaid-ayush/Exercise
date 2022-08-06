# Create a string made of the first, middle and last character

str = "Ayush"
a = len(str)
b = str[0]
c = str[a-1]
d = str[a//2]
print(b + c + d)

e = str[int(a/2)]
f = str[int(a/2)+1]
g = str[int(a/2)-1]
print(g+e+f)

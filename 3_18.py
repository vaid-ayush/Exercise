# Print the following pattern

n = 5

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

for j in range(n,0,-1):
    for k in range(0, j-1):
        print("*", end = " ")
    print(" ")
# for l in range(n-1,0,-1):
#     print(l*"* ",end="\n")
# print(" ")
# Print the following pattern

for i in reversed(range(6)):
    for j in range(i, 0, -1):
        print(j, end=" ")
        j -= 1
    print(" ")

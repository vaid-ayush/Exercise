# Print multiplication table form 1 to 10

def table(n):
    print("Table upto:", n)
    for i in range(1, n+1):
        for j in range(1, 11):
            x = i * j
            print(x, end=' ')
        print("\n")
table(10)

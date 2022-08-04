# downward Half-Pyramid Pattern with Star

def star(n):
    for i in range(n+1):
        print("*"*(n+1))
        n -= 1

star(6)

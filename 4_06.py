# Create a recursive function

def rec_func(n):
    if n:
        return n + rec_func(n-1)
    else:
        return 0


rec=rec_func(10)
print(rec)
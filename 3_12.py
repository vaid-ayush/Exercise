# Display Fibonacci series up to 10 terms

i = 0
j = 1
for k in range(11):
    print(i, end = ' ')
    r = i + j
    i = j
    j = r

# sum of the series upto n terms if n=3 output should be 3+33+333=369

n = 4
#j = (10**(n-1))*n
s=0
#for j in (1, n+1):
for i in range(1, n+1):
        j = (10**(n-i))*n
        s += j
#print(s)
z=s
for k in range(1, n):
    l = s//10
    #print(l)
    z = z + l
    #print(z)
    s=l
print(z)
#s = s//10
#print(s)

print(4444+444+44+4)

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)



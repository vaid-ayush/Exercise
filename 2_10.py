# Read line number 4 from the following file

with open("test.txt") as t:
    x = t.readlines()
    print(x[3])
    
# Append new string in the middle of a given string

def app(s1, s2):
    b = len(s1)
    a = int(b/2)
    x = s1[:a:]
    x = x + s2
    y = s1[a:]
    x = x + y
    print(x)


app("Ayush", "Vaid")

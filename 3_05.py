# Display numbers from a list using loop

i = [10, 20, 45, 23, 150, 350, 500, 560, 35, 45]
for x in i:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)




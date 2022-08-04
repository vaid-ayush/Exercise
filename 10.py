# Create a new list from a two list using the following condition

list1 = [10, 15, 20, 25, 45, 30,25,20]
list2 = [10, 25, 75, 85, 95, 80, 90]
list3 = []
for x in list1:

    if x % 2 == 0:
        list3.append(x)
    else:
        continue

for z in list2:

    if z % 2 != 0:
        list3.append(z)
    else:
        continue

print(list3)

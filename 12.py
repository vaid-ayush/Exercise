# Calculate income tax for the given income by adhering to the below rules

def income_tax(amount):
    t1 = 0.1
    t2 = 0.2
    y = amount - 10000
    z = amount - 20000
    b = 0
    c = 0

    if y > 0:
        b = y * t1
    if z > 0:
        c = z * t2

    return b+c


print(income_tax(50000))
print(income_tax(100000))
print(income_tax(20000))
print(income_tax(10000))
print(income_tax(16000))

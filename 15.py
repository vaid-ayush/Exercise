# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    print("Base:", base)
    print("Exponent:", exp)
    if exp > 0:
        x = base ** exp
        print(base,"raises to the power of", exp, "is:", x)


exponent(4, 6)
exponent(2,3)

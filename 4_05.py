# Create an inner function to calculate the addition in the following way



def func_1(a,b):
    def func_2(a,b):
        return a+b
    add = func_2(a,b)
    return add + 5000


res = func_1(2000, 3000)
print(res)


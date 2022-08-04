# Display numbers divisible by 5 from a list

def num(list):
    print("given list of numbers is ", list)
    print("Numbers divisible by 5 are:")
    for x in list:
        if x % 5 == 0:
            print(x)

num([10,20,30,40,55,12,34,56])

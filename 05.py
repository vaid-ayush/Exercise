#Check if the first and last number of a list is the same


def num(list):
    if list[0] == list[-1]:
        print(True)
    else:
        print(False)

num([10,20,30,40,50,10])
num([20,30,40,10,60])
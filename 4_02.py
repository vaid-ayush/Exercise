# function with variable length of arguments

def func(*args):
    for i in args:
        print(i)
func(10,20,30)
func("Ayush","Vaid")
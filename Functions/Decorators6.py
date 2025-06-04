
def numbers(func):
    def inner(*args):
        flag = True
        for i in args:
            if type(i) != int:
                flag = False
                break

            if flag:
                func(*args)            

            else:
                print("Non integer type")
    return inner

@numbers
def datatype(*args):
    print("Int data",args)

datatype(1,2,"yash",3,4,5,6,7,8)
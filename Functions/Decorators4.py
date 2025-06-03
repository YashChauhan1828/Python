def isValid(func):
    def inner(data,query):
        flag = False
        if query in data:
            flag = True

        if flag:
            func()
        else:
            print("Invalid query")
    return inner
@isValid
def getData():
    print("Data is valid..")

getData("YAsh","s")
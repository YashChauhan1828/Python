def isValid(func):
    def inner(data,query):
        flag = False
        if query in data:
            flag = True

        if flag:
            func(data)
        else:
            print("Invalid query")
    return inner
@isValid
def getData(data):
    print("Data is valid..",data)

getData("Yash","s")
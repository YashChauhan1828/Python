#task 1
str=[]
int=[]
boolean=[]
float=[]
def type_task(*agrs):
    for i in agrs:
        print(type(i).__name__)
        if type(i).__name__ == 'str':
            str.append(i)
        elif type(i).__name__ == 'int':
            int.append(i)
        elif type(i).__name__ == 'bool':
            boolean.append(i)
        else :
            float.append(i)

    return f"int {int} float:{float} boolean:{boolean} str:{str}"
type_task(100,True,20,20.89,100,"java",90.90)
print(type_task())

#task 2
def sum(*args):
    add=0
    for i in args:
        if type(i) == int or type(i)==float:
            add += i
    return add 
        


print(sum("yash",100,505.55,"java",False,90))

#task 3
def sum_mul(op,*args):
    add=0
    mul=1
    for i in args:
        if type(i) == int or type(i)==float:
            add += i
            mul *= i
    match op.lower():
        case "addition":
            return add
        case "multiplication":
            return mul

        


print("addition=",sum_mul("addition","yash",100,505.55,"java",False,90))
print("multiplication=",sum_mul("multiplication","yash",100,505.55,"java",False,90))
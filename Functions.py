#   Types Of Functions :-
#   1) Build-in-functions : min() , max() , len() , sum() , type() , dict() , list() , tuple() , set() , print() etc
#   2) User-defined-functions : we can define our own functions using def keyword.

# def calculateGmean(a,b):
#     return (a*b)/(a+b)    

# def isGreater(a,b):
#     if(a>b):
#         print("Number one is Greater")
#     else:
#         print("Number two is Greater")

# def isLess(a,b):
#     pass
#     # Code and Statement

# a = int(input("Enter The first number"))
# b = int(input("Enter the second number"))

# print(calculateGmean(a,b))
# isGreater(a,b)

# # Function Arguments
# # Arguments are the values that we pass to a function when we call it. They are also known
# # as parameters or arguments of a function.
# # Types:
# # 1)Default Arguments
# # 2)Variable Arguments
# # 3)Keyword Arguments
# # 4)Required Arguments


# # 5)Variable Length Arguments

# #   We can pass a variable number of arguments to a function using *args and **kwargs.
# def average(*number):
#     sum = 0
#     for num in number:
#         sum += num
#         return sum/len(number)
    
# print(average(5,6,3,1,0,6,4))    

def getmax(*args):
   print(max(args))
getmax(1,2,3,4,5,6,7,8,9)    

def userDetails(name,age,email,status):
    print(f"name:{name} age:{age} email:{email} status:{status}")

userDetails(name="yash", email="yash@gami.com", age=22 ,status="active")    
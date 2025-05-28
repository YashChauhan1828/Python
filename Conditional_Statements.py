''' If-Else Statements

a = int(input("Enter a Number"))
print("The number is : ",a)

if(a>18):
    print("Eligible for voting")
else:
    print("Not eligible for voting") '''

''' elif Statements

num = int(input("Enter The Number "))
print("Number is : " , num)
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is neutral")
print("I am happy")
'''

# Nested if Statements

num = int(input("Enter the number "))
print("Enter the number is : " , num)
if(num>0):
    print("Number is positive")
    if(num<=10 ):
        print("Number is between 0-10")
    elif(num>10 and num<=20):
        print("NUmber is between 11-20")
    else:   
        print("Number is Greater than 20 ")
elif(num<0):
     print("Number is negative")
else:
    print("Number is neutral")       
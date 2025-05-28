def factorial(n):
    if(n==0 or n==1):
        
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))

def fibonnaci(n):
        if(n==0 or n==1):
            return n
        else:
            return fibonnaci(n-1)+fibonnaci(n-2)
for i in range(0,10):
    print(fibonnaci(i))
    
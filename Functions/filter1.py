data = [1,2,3,4,5,6,7,8,9,10]

even = filter(lambda x : x%2==0,data)
print(list(even))

data = ["ram" , "shyam" , "yash" , "raj" , "rohit" , "varun"]
x1 = filter(lambda x : x.startswith("r") , data)
print(list(x1))

x2 = filter(lambda x : len(x)>4,data)
print(list(x2))

data = ["ram" ,"", "shyam" ,None,  "yash" , "raj" , "rohit" , None , "varun"]
x1 = filter(lambda x : x and x.startswith("r") , data)
print(list(x1))

x2 = filter(lambda x : x and len(x)>4,data)
print(list(x2))

x3 = filter(lambda x: x,data)
print(list(x3))
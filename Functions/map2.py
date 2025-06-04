data1 = [1,2,3]
data2 = [4,5,6]

sum = list(map(lambda x,y : x+y,data1 , data2))
print(sum)

firstname = ["yash" , "raj" , "varun"]
lastname = ["chauhan" , "patel" , "rizwani"]

name = list(map(lambda x,y : x+" "+y,firstname,lastname))
print(name)
nums = range(1,11)

ans = filter(lambda x: x>30,map(lambda x:x**2, nums))
print(list(ans))

data = ["ram" , "shyam" , "yash" , "raj" , "rohit" , "varun"]
ans1 = filter(lambda x: x.startswith("S"),map(lambda x: x.upper(),data))

print(list(ans1))
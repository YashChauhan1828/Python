marksheet={"Std1":{"marks":29,"Science":33,"Computer":35},"Std2":{"marks":35,"Science":37,"Computer":32}}
print(marksheet)

for i,j in marksheet.items():
    print(i)
    for sub,marks in j.items():
        print(f"sub = {sub} : marks = {marks}")
    
    print()
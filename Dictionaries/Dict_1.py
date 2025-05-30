data = {"opsindoor":["PM","HM","DM","AIR FORCE","NAVY","ARMY"],"URI":["PM","HM","DM","ARMY"]}

print(data)
opsindoor=data["opsindoor"]

for i,j in data.items():
    print(i,end=" ")
    for x in j:
        print(x,end=" ")
    print()       

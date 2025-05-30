def goa(name):
    print("Trip to goa")
    return "Kaju"

def Dubai(name):
    print("Trip to Dubai")
    return "Khajur"

def kashmir(name):
    print("Trip to kashmir")
    return "wollen clothes"

def trip(destination):
    print("Trip function called")
    x = destination("Yash")
    return x

data = None
budget = int(input("Enter your Budget for trip"))
if budget>60000:
    data = trip(kashmir)
elif budget>50000:
    data = trip(Dubai)
else:
    data = trip(goa)

print("data:" , data)
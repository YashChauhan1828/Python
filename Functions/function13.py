def tata(customer):
    print("tata Altroz car is bought")
    return "hackback"

def hyundai(customer):
    print("hyundai creta car is bought")
    return "suv"

def ford(customer):
    print("ford fiat car is bought")
    return "sedan"

def car(cb,customer):
    print("car is bought")
    return cb(customer)

customer = input("Enter customer name")
budget = int(input("Enter the budget for purchasing a car"))
if budget >=1000000:
    data = car(tata,customer)
elif budget >=1500000:
    data = car(hyundai,customer)
else:
    data = car(ford,customer)

print(data)
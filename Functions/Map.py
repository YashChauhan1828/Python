sales=[100,200,300,400]
discount = int(input("Enter the discount percentage: "))

final_price = list(map(lambda x : x-(x*discount)/100,sales))
print(final_price)
# Break Statement

# a = int(input("Enter the Number : "))
# for i in range(1,12):
#     print(a , "x" , i , "=" , a*(i) )
#     if(i == 10):
#         break   # Break the loop
# print("Out of loop")

# Continoue Statement

a = int(input("Enter the Number : "))
for i in range(1,12):
    if(i == 10):
         continue # Skip the statement
    print(a , "x" , i , "=" , a*(i) )
print("Out of loop")
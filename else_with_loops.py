# We can use else with loops
for  i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Loop finished")
#  Else will not be printed if the loop is breaked. Else will be printed if the loop is finished.
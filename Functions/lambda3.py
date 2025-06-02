users = ["bob","madam","naman"]

def palingdrome(x):
    flag = True
    for i in x:
        if i != i[::-1]:
            flag = False
    return flag

test = lambda x:palingdrome(x)
print(test(users))
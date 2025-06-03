def Order_food(func):

    def inner(noofpersons):
        print("Ordering food...")
        func(noofpersons)
    return inner



@Order_food
def throw_party(persons):
    print("Throw Party Function is called",persons)

throw_party(100)
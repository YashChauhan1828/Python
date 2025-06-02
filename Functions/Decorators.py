def Order_food(func):

    def inner():
        print("Ordering food...")
        func()
    return inner



@Order_food
def throw_party():
    print("Throw Party Function is called")

throw_party()
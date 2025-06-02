def authenticate(func):
    def inner():
        role = input("Enter your role: ")
        name = input("Enter your name")
        if role == "admin" and name == "admin":
            return func()
        else :
            print("Access denied")

    return inner




@authenticate
def access_data():
    print("User is acessing data")

access_data()
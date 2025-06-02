def outer():
    print("Outer function called ...")
    def inner():
        print("Inner function called ...")
    inner()
outer()
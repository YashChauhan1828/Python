x = int(input("Enter the number "))
match x:
    case 1:print("Hello")
    case 2:print("Hi")
    case 3:print("Hey")
   

    case _ if x!=90 :print("Not 90")
    case _ if x!=80 :print("Not 80")
    
    case _:print("Default")    

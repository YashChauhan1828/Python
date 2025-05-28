# String Methods
name="! !!!Yash!!! !!"
surname="Chauhan"
print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("Yash" , "Programmer"))  
print(name.split(" "))
a= "good MoRning"
print(a.capitalize())
print(a.center(50))
print(a.count("o"))
print(name.endswith("!!"))
print(a.endswith("od" , 0, 3))
str = "My   Name     Is  YASH"
print(str.find("is"))
# print(str.index("is"))
print(surname.isalnum())
print(surname.isalpha())
print(surname.islower())
print(surname.isprintable())
print(str.isspace())
print(str.istitle())
print(str.isupper())
print(str.startswith("!"))
print(str.swapcase())
print(str.title())
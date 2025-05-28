name="! !!!Yash!!! !!"
surname="Chauhan"
multiline_str = """ Hello!!
Good morning
We are learning 100 days of code.
"Building 100 streak of coding"."""
print(multiline_str)

print(name[0])

# Looping in string

print("For Loop")

for character in multiline_str:
    print(character)    

# Slicing in String

print(multiline_str[4:9])
print(name[:])
print(surname[:len(name)-3])
print(len(multiline_str))
print(len(name))
print(name[-3:-1])


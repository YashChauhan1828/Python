# Higher Order Function(With Argument)
def commerce(name):
    print(f"{name} has taken admission in commerce")

def science(name):
    print(f"{name} has taken admission in science")

def arts(name):
    print(f"{name} has taken admission in arts")

def admission(stream,name):
    print("Admission Function called")
    stream(name)

name = input("Enter your name")
percent = int(input("Enter your Percentage"))

if percent>80:
    admission(science,name)
elif percent>70:
    admission(commerce,name)
else:
    admission(arts,name)
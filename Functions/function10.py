
# Higher Order Function(Without Argument)
def commerce():
    print("User has taken admission in commerce")

def science():
    print("user has taken admission in science")

def arts():
    print("user has taken admission in arts")

def admission(stream):
    print("Admission Function called")
    stream()


percent = int(input("Enter your Percentage"))

if percent>80:
    admission(science)
elif percent>70:
    admission(commerce)
else:
    admission(arts)

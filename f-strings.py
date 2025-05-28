letter = "My name is {} and I am {} years old."
name = "John"
age=20
print(letter.format(name, age))  # Output: My name is John and I am 20
# f-string
letter = f"My name is {name} and I am {age} years old."
print(letter)  # Output: My name is John and I am 20 years old.
salary = 50000
wifesalary = 34500
income = f"My family income is {salary + wifesalary}"
print(income)
income = f"My salary is {{salary }}"
print(income)  # Output: My salary is {salary}
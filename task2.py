# Calculator using match-case and integer choice

choices = int(input("Enter the Number"))

def calculate(choices, x, y):
    match choices:
        case 1:
            return x + y
        case 2:
            return x - y
        case 3:
            return x * y
        case 4:
            if y == 0:
                return "Error: Cannot divide by zero"
            return x / y
        case _:
            return "Invalid operation"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter choice (1-4): "))

    if choice in choices:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate(choice, num1, num2)
        print(f"Result: {result}")
    else:
        print("Error: Invalid choice.")
except ValueError:
    print("Error: Please enter numbers only.")

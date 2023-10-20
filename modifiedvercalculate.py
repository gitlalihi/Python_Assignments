# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers with error handling for division by zero
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

#user input for two numbers
try:
    x = int(input("Enter your first number: "))
    y = int(input("Enter your  second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    # Display the menu
    print("Please select operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user for the operation
    z = input("Select  your operation (1/2/3/4): ")

    # Check if the operation is valid
    if z in ('1', '2', '3', '4'):
        z = int(z)
        if z== 1:
            result = add(x, y)
            print(f"{x} + {y} = {result}")
        elif z == 2:
            result = subtract(x, y)
            print(f"{x} - {y} = {result}")
        elif z == 3:
            result = multiply(x, y)
            print(f"{x} * {y} = {result}")
        elif z == 4:
            result = divide(x, y)
            print(f"{x} / {y} = {result}")
    else:
        print("Invalid operation. Please select a valid operation (1/2/3/4).")

x = int(input("Enter first number: "))
y= int(input("Enter second number: "))
# Function to add two numbers
def add(x, y):
    a = x + y
    return a
 # Function to subtract two numbers
def subtract(x,y):
    b = x - y
    return b 
 # Function to multiply two numbers
def multiply(x,y):
    c = x * y
    return c
 # Function to divide two numbers
def divide(x,y):
    d =  x / y
    return d 
print("Please select operation -\n" 
"1. Add\n" 
"2. Subtract\n" 
"3. Multiply\n" 
"4. Divide\n")
# Take input from the user
z = int(input("Select operations form 1, 2, 3, 4 :"))
if z == 1:
    print(x, "+", y, "=",add(x, y))
elif z == 2:
    print(x, "-", y, "=",subtract(x, y))
elif z == 3:
    print(x, "*", y, "=",multiply(x,y))
elif z == 4:
    print(x, "/", y , "=",divide(x,y))
else:
    print("Invalid input")
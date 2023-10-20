# user input
x = int(input("Enter a number:"))

# function to check whether the input number is odd or even
def odd_even(x):
    if x % 2 == 0:
        print(x,"\na even number")
    else:
        print(x,"\na odd number")

odd_even(x)        

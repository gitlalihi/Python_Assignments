#String reversal
string= str (input("Enter your senctence\n"))
x=0
#defining a function reversal(x)
def reversal(x):
    sReverse= x[::-1]  # slice the string backwards 
    return sReverse    # return the sliced string in a variable using the return keyword

string= reversal(string) # call the function reversal by passing input variable via the function 
# user defined function
# printing the result
print("Reversed string is\n", string)


    

       
    
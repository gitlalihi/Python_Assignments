# to count number of vowels in a string 
s1 = str(input("Enter your string"))
vowels=["a","e","i","o","u""A","E","I""O","U"] # creating a list
x = 0   # intailize x counting for every charachter to zero

for i in range(len(s1)):
    if s1[i] in vowels:
        x = x + 1

print("The number of vowels in your string is", x)  




    

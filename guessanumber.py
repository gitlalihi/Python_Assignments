import random
s= str(input("What is your name?"))

num=int()

flag = True
while flag:
    x = input("Enter your lower bound:")
    y = input("Enter your upper bound:")
    if (x.isdigit()) and (y.isdigit()):
        print("Lets play the game!")
        x = int(x)
        y = int (y)
        flag = False
    else:
        print("Invalid Input")

num = random.randint(x,y)
num_guessing= int(input("Enter your guessing number"))
def guess_num(num_guessing, num):
    

    if(num_guessing < num): 
        print(" Your input is too low")
    elif (num_guessing == num):
        print("You have guessed the number correctly ")
    elif(num_guessing > num):
        print("Your input is too high ")
    else:
        print("Your input  is invalid")


guess_num(num_guessing, num)

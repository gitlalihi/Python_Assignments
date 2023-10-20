num= int(input(" enter your number:"))
print("The multiplication table of your number is")
# defining a  function  to calculate the multilplication of your given number
def mulptiply_table(num):
    for i in range (1,11):
        x=int (num*i)
        print(num,"*",i,"=",x)

mulptiply_table(num)


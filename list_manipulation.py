# python programme  for list manipulation

numlist= list(("1","2","3","4","5"))
print(numlist)

def manipulate(numlist):
    # add an element to the end of the list
    numlist.append("6")# adding an integer
    
    numlist.append("true")# adding a boolean
    
    numlist.append("hello")# adding a string 
    print("The list  after adding new elements is :",numlist)  
    
    # To remove the element from a list
    numlist.pop()
    print("the list after removing an element: ",numlist) 
    
    print("The final modified list is :" ,numlist)

manipulate(numlist)    

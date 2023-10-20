def manipulate(numlist):
    # Append integers and a boolean to the list
    numlist.append(6)  # Append an integer
    numlist.append(True)  # Append a boolean

    # Append a string to the list
    numlist.append("hello")

    print("The list after adding new elements is:", numlist)

    # Remove a specific element from the list
    numlist.remove(True)

    print("The list after removing an element:", numlist)

    return numlist

numlist = ["1", "2", "3", "4", "5"]
manipulated_list = manipulate(numlist)
print("The final modified list is:", manipulated_list)


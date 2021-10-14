for element in grades:
    if(element < 38):
        print(element) 
    elif(str(element)[1] == "8" or str(element)[1] == "3"):
        print(element + 2)
    elif(str(element)[1] == "9" or str(element)[1] == "4"):
        print(element + 1)
    else:
        print(element)
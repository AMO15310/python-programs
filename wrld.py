from ast import operator


num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
#print("Do you want multiplication , division or addition of the two numbers ")
choice = input("Type (Mult) for multiplication , (Add) for addition and (Div) for division ")
if choice == "Mult" or choice == "mult":
    print (num1 * num2)
elif choice == "Add" or choice == "add":
    print (num1 + num2)
elif choice == "Div" or choice == "div" :
    print (num1 / num2)
else :
    print ("Check the instructions then try again")
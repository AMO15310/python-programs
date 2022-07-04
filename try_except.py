#first write the code to run 
try: 
    print(arr)
except NameError:
    print('arr is not defined')
else:
    print("code executed with no problems")
#The except code block will execute since a NameError was raised because arr is not defined

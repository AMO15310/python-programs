#Create a tuple
y = ("Orange","Apple","Banana","Lemon")
#To update the tuple convert it to a list first
x = list(y)
#Then update the list
x.append("Mango")
#convert back the list to a tuple
y = tuple(x)
print(y)

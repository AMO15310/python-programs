import numpy as np
from numpy import random
x = random.randint(10)
y = int(input("Please enter your lucky number from 0 to 10: "))
if x == y & y<=10:
    print("You won!!! Today is your lucky day")

else:
    print("Sorry the lucky number is " + str(x) + " Keep trying")

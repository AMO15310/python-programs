import numpy as np
from numpy import random
arr = np.array(["rock","paper","scissors"])
x = random.choice(arr)

y = input("Choose between 'rock' , 'paper' , x 'scissors': ")
y = y.lower()
if y == 'rock' and x == 'scissors':
    print("Hurray!!! You win! My guess was " +x)
elif y == 'scissors' and x == 'rock':
    print("Opps!! You should try again you guessed wrong my answer is " +x)
elif y == 'rock' and x == 'paper':
    print("Opps!! You should try again you guessed wrong my answer is " +x)
elif y == 'scissors' and x == 'paper':
    print("Hurray!!! You win! my guess was " +x)
elif y == 'paper' and x == 'scissors' :
    print("Opps!! You should try again you guessed wrong my answer is " +x)
elif y == 'paper' and x == 'rock' :
    print("Hurray!!! You win! My guess was " +x)
elif y == 'paper' and x == 'paper':
    print("Please try again my guess is the same as yours " +x)
elif y == 'rock' and x == 'rock' :
    print("Please try again my guess is the same as yours " +x)
elif y == 'scissors' and x == 'scissors' :
    print("Please try again my guess is the same as yours " +x)
else:
    print("please follow the instructions then try again")
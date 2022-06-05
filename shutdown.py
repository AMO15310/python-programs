#!/bin/python3
import os

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

if shutdown == 'no' or shutdown == "No":
    print("You have successfully aborted the shutdown")
    

elif shutdown == "yes" or shutdown == "Yes" :
    print("Your computer will shutdown")
    os.system("shutdown /s /t 1")


else:
    print("Please check the instructions and try again")

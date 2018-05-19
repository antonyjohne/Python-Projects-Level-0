""" This Program is Dice Simulator that produce an Output from 1-6
    everytime the User presses Enter. In order to close the Program,
    the User has to type "Exit" into the console.
"""

#Imports the random module to generate the random Integers
import random

#Initial Designer Print Statements
print(" Hi! Welcome to Dicey!")
print ("""

       .-------.    _______
      /   o   /|   /\\      \\
     /_______/o|  /o \\  o   \\
     | o     | | /   o\\______\\
     |   o   |o/ \\o   /o     /
     |     o |/   \\ o/  o   /
     '-------'     \\/____o_/

      """)


exit=False      #Set True When User types "Exit" into the console
count=0         #Count to keep track of Iterations/Dice rolls

#The Input is obtained below
enter=(input(("Press Enter to Roll (or) Type 'Exit' to Close. \n\n")).lower())

#Condition to check wether the user wants to Exit the program without Rolling the Dice
if (enter=="exit"):
    exit=True

#Checks for Enter and Produces a random integer using the random module
while(enter=="" or not exit):
    dice_number=random.randint(1,6)
    count = count + 1
    print(f"{count}>You got a {dice_number}")
    enter=(input("Press Enter to Roll Again! \n").lower())  #Obtain input from User again

    #If User inputs "Exit", Close the program.
    if (enter=="exit"):
        exit=True

    #If the User inputs anything else other than "Exit" Roll the dice again.
    elif(enter is not ""):
        print("\n")
        continue

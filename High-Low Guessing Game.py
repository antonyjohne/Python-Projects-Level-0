""" This is a Guessing Game, in which the User Guesses the Rrandom Value
    generated by the Computer
"""

#Import the required Modules
import random
import os

#Function to Clear console every New Game Session, using OS Module
def clear_screen():
    if(os.name == "nt"):
        os.system("cls")

    else:
        os.system("clear")


new_game=True

#Checks if the User wants to play. Runs atleast Once.
while (new_game==True):

    clear_screen()
    print("\nWelcome to High/Low Game!\nDo you have What is Takes to Soar High or Fall Low?\n")
    print('(Enter "Exit" to close the Program)\n\n')
    print("The Computer has Succesfully Generated a Random Number from 1 to 100.\n")

    #Generates a Random Number
    guess=random.randint(1,100)
    lives=5
    found=False
    inner_loop=False        #Used to Break out of a nested Loops

    while (lives>0 and not found):
        #Check for a Valid Digit or "Exit" as Input from User
        try:
            user_guess=input(f"(Lives = {lives})   Enter Your Guess: ").strip().lower()
            if(user_guess == "exit"):
                inner_loop=True
                break               #Breaks out of Inner Loop

            #Game Algorithm
            elif (user_guess.isdigit()):

                if(int(user_guess)>guess):
                    print("Your guess is High. Try Something Lower. \n")
                    lives-=1

                elif(int(user_guess)<guess):
                    print("Your guess is Low. Try Something Higher. \n")
                    lives-=1

                else:
                    print ("YAAY! You Found The Number! \n")
                    found=True

            #Raise Error if Input by User is Undefined
            else:
                raise (ValueError)

        except ValueError:
                print("Please Enter a Valid Number!\n")

    if(inner_loop==True):
        break                    #Breaks out of both Inner Loop and Outer loop at once.

    #User runs out of Lives
    elif (found==False):
        print (f"Game Over! The actual Number is {guess} \n\n")

    restart=input("Do you want to play again? (Y/N) : ").strip().lower()

    #Checks if the User wants to Play again
    if(restart == "n" or restart == "no"):
        new_game=False

##Assortment of functions to be used in main_game.py

#importing stuff
import os
from time import sleep
import sys

def intro():
    #this function will show the start computer screen.

    #Clear screen
    os.system('cls') #windows
    os.system('clear') #Mac

    print("""
    ___ __  __  __ __ ___   __  _  __  __ __
   / _]/  \|  V  | __| |  \| |/  \|  V  | __|
  | [/\ /\ | \_/ | _|  | | ' | /\ | \_/ | _|
   \__/_||_|_| |_|___| |_|\__|_||_|_| |_|___| \n""")
    input("  ------------PRESS ENTER TO START------------\n")
    computer() #calls computer function

def computer():
    #tester
    #print("  ___________________________________________")
    #print(" /                   XED                      \\")
    #print("|   ________________________________________   |")
    #print("|  |                                        |  |")
    #print("|  | Booting...                             |  |")
    #print("|  | Importing data sets...                 |  |")
    #print("|  | Understanding Labs...                  |  |")
    #print("|  |    Falied...                           |  |")
    #print("|  | Error Caught...Continuing...           |  |")
    #print("|  |                                        |  |")
    #print("|  |                                        |  |")
    #print("|  | >ENTER COMMAND:                        |  |")
    #print("|  |________________________________________|  |")
    #print("\\_____________________________________________/")

    #types it all out...
    typewriter("  ___________________________________________\n /                   XED                      \\\n|   ________________________________________   |\n|  |                                        |  |\n|  | Booting...                             |  |\n|  | Importing data sets...                 |  |\n|  | Understanding Labs...                  |  |\n|  |    Failed...                           |  |\n|  | Error Caught...Continuing...           |  |\n|  |                                        |  |\n|  | >ENTER NAME:                           |  |\n|  |________________________________________|  |\n\\_____________________________________________/\n")
    name=input("ENTER NAME: ")
    name_answer=input("Is "+name+" Correct? [y/n]")
    if name_answer=="y":
        pass
    else:
        #if name fails, game quits, lol
        print("Name Failed...System shutting down.\n")
        print("System too valuable for someone who\n"+
        "does not know their own name.\n")
        input("")
        sys.exit()

def typewriter(string):
    for i in string:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.01)
    print("")


intro()

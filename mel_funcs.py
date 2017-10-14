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
    #Clear screen
    os.system('cls') #windows
    os.system('clear') #Mac

    computer() #calls computer function

def computer():
    #tester
    #print("  ___________________________________________")
    #print(" /                   XED                      \\")
    #print("|   ________________________________________   |")
    #print("|  |                                        |  |")
    #print("|  | Searching database for name...         |  |")
    #print("|  | 0 results found.                       |  |")
    #print("|  |                                        |  |")
    #print("|  | Trying again...                        |  |")
    #print("|  | 0 results found.                       |  |")
    #print("|  |                                        |  |")
    #print("|  | Identity unconfirmed.                  |  |")
    #print("|  | UPF (Unconfirmed Person Force) Called. |  |")
    #print("|  |________________________________________|  |")
    #print("\\_____________________________________________/")

    #types it all out...
    typewriter("  ___________________________________________\n /                   XED                      \\\n|   ________________________________________   |\n|  |                                        |  |\n|  | Booting...                             |  |\n|  | Importing data sets...                 |  |\n|  | Understanding Labs...                  |  |\n|  |    Failed...                           |  |\n|  | Error Caught...Continuing...           |  |\n|  |                                        |  |\n|  | >ENTER NAME:                           |  |\n|  |________________________________________|  |\n\\_____________________________________________/\n")
    name=input("ENTER NAME: ")
    name_answer=input("Is "+name+" Correct? [y/n]: ")
    if name_answer=="y":
        print("Name Accepted.\nNow checking database for identity.")
        input("")
    else:
        #if name fails, game quits, lol
        print("Name Failed...System shutting down.\n")
        print("System too valuable for someone who\n"+
        "does not know their own name.\n")
        input("")
        sys.exit()

    #Clear screen
    os.system('cls') #windows
    os.system('clear') #Mac

    typewriter("  ___________________________________________\n /                   XED                      \\\n|   ________________________________________   |\n|  |                                        |  |\n|  | Searching database for name...         |  |\n|  | 0 results found.                       |  |\n|  |                                        |  |\n|  | Trying again...                        |  |\n|  | 0 results found.                       |  |\n|  | Identity unconfirmed.                  |  |\n|  | UPF (Unconfirmed Person Force) Called. |  |\n|  |________________________________________|  |\n\\_____________________________________________/\n")
    print(" "+name.upper()+": Hm...That doesn't look very good.")
    print(" "+name.upper()+": I should find out who I am, and fast.\n")
    input(">LOOK AROUND ROOM")

def typewriter(string):
    for i in string:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.01)
    print("")


intro()

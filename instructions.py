import time
import os

def instructions():
    valid_responses = ["yes","no"]
    yes_or_no = None
    while yes_or_no not in valid_responses:
        yes_or_no = input('Are you ready to play? Yes or No \n').lower().strip()
        time.sleep(1)
        os.system('clear')
        if yes_or_no == "yes":
            print('Welcome to the Mall Murder Madness Mystery')
            time.sleep(2)
            print('Collect all 6 items to win the game and decide the fate of the Predator.')
            time.sleep(2)
            print('Move commands: Go South, Go North, Go East, Go West')
            time.sleep(2)
            print("To add to your inventory: Type 'Get then items name' " )  
        else:
            print('Please come back and play. ')

instructions()

   

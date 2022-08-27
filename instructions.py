import time
import os

def instructions():
    valid_responses = ["yes","no"]
    yes_or_no = None
    while yes_or_no not in valid_responses:
        yes_or_no = input('Are you ready to play? (Yes/No) \n').lower().strip()
        time.sleep(1)
        os.system('clear')
        if yes_or_no == "yes":
            print('Welcome to the Mall Murder Madness Mystery')
            time.sleep(2)
            print('Collect all 5 items to win the game and decide the fate of the Predator.')
            time.sleep(2)
            print('Move commands: South, North, East, West')
            time.sleep(2)
           
        else:
            print('Please come back and play. ')

instructions()

   

import os
import sys
import time



def typewriter_affect_intro():
    beginning = "Suddenly, you hear an M16 rifle while window shopping at the mall. As you glance around and see people running. Realizing you're still a Marine, once a Marine, always a Marine 'Oohrah'. You need some things to stop the perpetrator. First, your shoes and clothes won't work. You'll need the new phone you came for and water. A compound bow (thankfully you were on the Archery team in high school) and handcuffs for a silent takedown before anyone else gets hurt. Retirement over! Let's go..."
    for char in beginning:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !=' ':
            time.sleep(0.1) #.1 second after each character
    os.system('clear')

typewriter_affect_intro()


# for loop is going over every character in the beginning into statement and print it.
# sys standard for system. 
# sys.stdout.write prints to the screen. Unlike the print function it does not print a new line. It is also supposed to print the number of characters at the end.
#sys.stdout.flush() pushes out all the data that has been buffered to that point to a file object. While using stdout, data is stored in buffer memory (for some time or until the memory gets filled) before it gets written to terminal. Using flush() forces to empty the buffer and write to terminal even before buffer has empty space.
# I don't need # os.system('clear') after if statement is executed.
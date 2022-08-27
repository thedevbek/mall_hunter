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



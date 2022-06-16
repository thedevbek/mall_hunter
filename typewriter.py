import sys,time,os

msg = "Suddenly, you hear an M16 rifle shot while window shopping in the mall.\n As you glance around and see people running.\n  You realize you are still a Marine, once a Marine, always a Marine 'Oohrah'.\n You need some things to stop the perpetrator. \n First your high heels and dress won't work.\n You'll need the new phone you came for and water.\n A compound bow and handcuffs for a silent takedown before anyone else gets hurt.\n Ready to save people? Let's go...\n "


def typewriter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !='\n':
            time.sleep(0.1) #.1 second after each character
        else:
            time.sleep(0.5) #.5 seconds between newline


os.system('clear')

typewriter(msg)

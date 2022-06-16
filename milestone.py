# data setup
rooms = {'Great Hall': {'name': 'Great Hall', 'go south': 'Bedroom',
        'text': 'You are in the Great Hall.'},
        
    'Bedroom': {'name': 'the bedroom', 'go east': 'Cellar', 'go north': 'Great Hall',
        'text': 'You are in the Bedroom.'},  
    'Cellar': {'name': 'the Cellar', 'go west': 'Bedroom',
        'text': 'You are in the Cellar.'}
    }
directions = ['go north', 'go south', 'go east', 'go west']
current_room = rooms['Great Hall']
 
# game loop
while True:
    # display current location
 
    print('You are in {}.'.format(current_room['name']))
   
    # get user input
    command = input('\nWhat do you do?')
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        elif rooms[2] == 'Cellar':
            print('Congratulations! You have reached the cellar and defeated the Dragon!')
            break
        else:
            # bad movement
            print('You cannot go that way.')
    # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # bad command
    else:
        print('Invalid input')
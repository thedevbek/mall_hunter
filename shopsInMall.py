

shops = {

        'Atrium':{'North': 'Foot_Locker', 'South': "Spencer's", 'West': 'Apple_Store', 'East': 'Sporting_Goods', 'item': 'There is no item in the Atrium.'}, 

        'Foot_Locker': {'South': 'Atrium', 'East': 'Food_Court', 'item': 'shoes'},

        'Food_Court':{'West': 'Foot_Locker', 'item': 'water'},

        "Macy's_Store":{'South': 'Sporting Goods', 'item': 'dark_clothes'},

        'Sporting_Goods':{ 'North': "Macy's_Store",'West': 'Atrium', 'item': 'compound_bow'},

        "Spencer's":{ 'East':'Game_Stop','item':'predator'}, 

        "Game_Stop":{'West':"Spencer's", 'item': 'There is nothing in this store to use. All you see are scared faces in this store.'},

        'Apple_Store':{ 'East':'Atrium', 'item': 'phone'}
    }





def get_command(location,inventory):
    direction = input("Please make a move or quit. ")
    if direction=='quit':
        return 'quit'
    direction = direction.split()[-1]   
    try:
        location = shops[location][direction]
    except KeyError:
        print('that is not a vaid move')
        return
    if location=='Game_Stop' or location=='Atrium':
        print(shops[location]['item'])
    elif location == "Spencer's":
        print("you moved to",location)
        print("you see",shops[location]['item'])
        if len(inventory)==5:
            print('you have found all items to defeat the beast')
            print("Congratulations!")
        else:
            print("you didn't find enough items to defeat the beast")
            print("RIP my friend")
        return 'quit'
    else:
        print("you see",shops[location]['item'])
        cmd = input("pick it up? (y/n)")
        if cmd =='y':
            if shops[location]['item'] in inventory:
                print('already have it')
            else:
                inventory.append(shops[location]['item'])
    return [location,inventory]

def play():
    start_shop = 'Atrium'
    end_shop = "Spencer's"
    start_item = 0
    location = start_shop
    inventory = []
    cmd = 0
    while cmd != 'quit':
        print("you are in",location)
        moves = list(shops[location].keys())
        moves.remove('item')
        print("valid moves are",moves)
        loc = get_command(location,inventory)
        if type(loc)==list:
            location,inventory = loc
                
# def status(start_shop, start_item):
    
#     if 'item' in shops:
#         print(f'You are starting in the {start_shop} with {start_item} items.')
#     return status
    
play()






from shops_dic import shops

starting_shop = 'Atrium'
starting_inventory = 0

def status(starting_shop,starting_inventory):
    starting_shops_dic = shops[starting_shop]
    if 'item' in shops[starting_shop]:
        print(f'You are starting in the {starting_shop} with {str(starting_inventory)} inventory') 
    return status
print(status(starting_shop, starting_inventory))
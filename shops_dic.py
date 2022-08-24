# from re import L
import sys, os



shops = {

        # 'Atrium':{'North': 'Foot_Locker', 'South': "Spencer's", 'West': 'Apple_Store', 'East': "Dick's_Sporting_Goods"}, ##Starting Room 

        # 'Foot_Locker': {'South': 'Atrium', 'East': 'Food_Court', 'item': 'shoes'},

        # 'Food_Court':{'West': 'Foot_Locker', 'item': 'water'},

        # "Macy's_Store":{'South': "Dick's Sporting Goods", 'item': 'dark_clothes'},

        # "Dick's s_Sporting_Goods":{ 'North': "Macy's_Store",'West': 'Atrium', 'item': 'compound_bow'},

        # "Spencer's":{ 'East':'Game_Stop','item':'predator'}, ##Surprise Surprise

        # 'Apple_Store':{ 'East':'Atrium', 'item': 'phone'}
        'Apple_Store':{ 'directions': 'East', 'item': 'phone'}

    }


directions = ' '
directions =  ('south', 'north', 'east', 'west')


shop = 'Atrium'
inventory = 0

current_shop = 'Apple_Store'
for shop in shops.items():
    # for direction in directions['East']:

        print(current_shop)
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 20:01:14 2022

@author: Ariel
"""

import random

class player:
    
    def __init__(self, name, pokemon_list, bag, money):
        self.name = name
        self.pokemon_list
        self.bag = bag
        self.money = money
        

class pokemon:
    
    def __init__(self, name, type_of_pokemon, nature, moves, health):
        self.name = name
        self.type_of_pokemon = type_of_pokemon
        self.nature = nature
        self.moves = moves
        self.health = health

ray_ray = pokemon('Ray Ray', "Rayquaza", 'Dragon', {'fly' : 70, 'dragon burst' : 150}, '170')

ariel = player('Ariel', [ray_ray], ['potion', 'full restore'], 31234141214)

def battle(player1, player2):
    

        
    
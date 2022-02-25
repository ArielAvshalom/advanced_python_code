#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:57:19 2022

@author: arielavshalom
"""
class square:
    pass

class player:
    pass

class bag:
    pass

class item:
    pass

class pokemon:
    
    def __init__(self, poke_id, poke_species, poke_name, attack_list, stat_dict): #base_stat_dict):
        self.id = poke_id
        self.species = poke_species
        self.name = poke_name
        self.attacks = attack_list
        self.stats = stat_dict
        #self.base_stats = base_stat_dict
    
class attack:
    
    def __init__(self, attack_id, attack_name, attack_power):
        self.id = attack_id
        self.name = attack_name
        self.power = attack_power

class stats:
    
    def __init__(self, base_health, base_attack, level):
        
        self.health = base_health + round(level*2.5)
        self.attack = base_attack + (level*.025)
        self.level = level
        

if __name__ == "__main__":
    
    firepunch = attack(1, 'Fire Punch', 75)
    torchic_stats = stats(27, 1, 5)
    
    fire_chicken = pokemon(1, 'torchic', 'Fire Chicken', [firepunch], torchic_stats)
    
    print(fire_chicken.id)
    print(fire_chicken.name)
    print(fire_chicken.attacks[0].name)
    
    
    
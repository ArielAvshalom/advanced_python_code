# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:51:04 2022

@author: Ariel
"""
import inspect
from pprint import pprint
from dataclasses import dataclass
import dataclasses

@dataclass(order = True, frozen=True)
class Comment:
    id: int
    text: str

class Comment2:
    id : int
    text : str


#pprint(inspect.getmembers(Comment, inspect.isfunction))

class shower_thoughts:
    def __init__(self, id: int, text: str, tmsp):
        self.id : int = id
        self.text: str = text
        self.tmsp = tmsp
        
    
    def __repr__(self):
        return "{}(id={},text={}, tmsp = {})".format(self.__class__.__name__, self.id, self.text, self.tmsp)
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text, self.tmsp) == (other.id, other.text, self.tmsp)
        else:
            return NotImplemented
        
    def __ne__(self, other):
        result = self.__eq__(other)
        
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
    #We would have to implement all of this.
    """
    __le__
    __ge__
    __lt__
    __gt__
    __hash__
    """
    
my_thought = shower_thoughts(1, 'Sometimes I wonder if Ed from Ed Edd and Eddy is controlling the universe and we are all in his mind', '2/14/22')
    
my_thought2 = shower_thoughts(1, 'Randomly hearing your favorite song on the radio is more satisfying than playing it directly from your ipod.', '2/15/22')


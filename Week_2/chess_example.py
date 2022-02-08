# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:59:06 2022

@author: Ariel
"""
import inspect
#what is self
#what is a class

#what is a decorator => syntactic sugar that lets you pass in values to functions and it's very pretty and nice.


#class classname:
    
class Chess_piece:
    #number_of_pieces = 32
    
    #def __new__()
    
    def __init__(self, power, name = 'King'): #self is this if refers to the object instantiated.
        self.name = name
        self.power = power










dimensions = [8,8]

actual_board = []

for row in range(dimensions[0]):
    actual_board.append([])
    for column in range(dimensions[1]):
        actual_board[-1].append([row,column])


class board:
    def __init__(self, board_dimensions = [8,8]):
        self.board_dimensions = board_dimensions
        self.actual_board = []
    
    def __str__(self):
        return 'you have a board'
    
    def __repr__(self):
        return str(self.actual_board)
    
    def create_board(self):
        initial_board_instance = self.actual_board #originally it was []
        
        for row in range(self.board_dimensions[0]):
            initial_board_instance.append([])
            for column in range(self.board_dimensions[1]):
                #print(column)
                if (row+column) % 2 == 0:
                    initial_board_instance[-1].append(['white'])
                else:
                    initial_board_instance[-1].append(['black'])
                
                if row == 0 and column == 0 or row == 0 and column == 7:
                    initial_board_instance[-1].append(Chess_piece(5, 'Rook'))
        
        
        return initial_board_instance
    
    def cake():
        print("Cake!!!")
        return None


if __name__ == "__main__":
    my_bishop = Chess_piece(3, "Bishop")
    my_king = Chess_piece(float('inf'))
    my_queen = Chess_piece(9, 'Queen')
    my_knight = Chess_piece(3, 'Horsey')
    
    my_board = board()
    my_board.create_board()
    #my_board.actual_board[0][0] = Chess_piece(5, 'Rook')
    
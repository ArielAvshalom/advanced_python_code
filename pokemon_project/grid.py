# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:16:45 2022

@author: Ariel
"""

#let's make a 10x10 grid.
my_grid = []
for row_idx in range(10):
    my_grid.append([])
    for col_idx in range(10):
        my_grid[-1].append(0)

player_position = (0,0)

my_grid[player_position[0]][player_position[1]] = 'X'

#if we don't have a prearranged grid
#grid[5][5] = 'Tree'

#you can define parts that you can automatically attach to your grid

def road(road_length, startx, starty, grid):
    
    for idx in range(road_length):
        grid[startx+idx][starty] = 3
    
    return grid

my_new_grid = road(4, 1,1,my_grid)

# my_grid[2:][5] = my_road

# for num in range(5):
#     my_grid[num][5] = my_road[num[0]][0]

        
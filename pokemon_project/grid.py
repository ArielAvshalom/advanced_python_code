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

player_position = [0,0]

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

player_direction = input('which way do you want to?')

if player_direction == 'w':
    new_player_position = player_position[:]
    new_player_position[0] = player_position[0]-1
    

    my_grid[new_player_position[0]][new_player_position[1]] = 'X'
    my_grid[player_position[0]][player_position[1]] = 0

x = [-1,1,0,0]
y = [0,0,-1,1]

x[2]
y[2]

my_test_grid = []
for row_idx in range(3):
    my_test_grid.append([])
    for col_idx in range(3):
        my_test_grid[-1].append(0)

start = [1,1]

my_test_grid[1][1] = 'P'
my_test_grid[1][0] = 'W'
my_test_grid[0][1] = 'N'
my_test_grid[1][2] = 'E'
my_test_grid[2][1] = 'S'

my_test_grid[start[0]][start[1]+1]


player_direction = input('which way do you want to?')

if player_direction == 'n':
    print(my_test_grid[start[0]+x[0]][start[1]+y[0]])
if player_direction == 'w':
    print(my_test_grid[start[0]+x[2]][start[1]+y[2]])

def pass_through_grid(current_player_position):
    pass
        
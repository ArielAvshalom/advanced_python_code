# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:12:46 2022

@author: Ariel
"""

#some code to get a adjacency list

"""
node : edgelist of the node

1 : [2,3]
2 : [1,4]
3 : 1,4 
4 : 2,3,5
5 : 4


What input do you envision?
(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4) ...
[(1,2), (1,3), (2,1), (2,4)]
We might also get that there are 5 nodes for example
"""
#import networkx

def make_adjacency_list(*args):
    """
    Parameters
    ----------
    *args : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    adjacency_list = dict()
    
    for edge_pair in args:
        node = edge_pair[0]
        
        if node in adjacency_list:
            adjacency_list[node].append(edge_pair[1])
        else:
            adjacency_list[node] = [edge_pair[1]]
            
    return adjacency_list


    
# if the input is (1,4) and you are expect 1 -> 4
# vs if it means that 4 -> 1
# if it means that 1->4 and 4->1

        
#input: 
#make_adjacency_list((1,2), (1,3), (2,1), (2,4), 1, 2, 3, 'abc', key = '123', key2 = 'my heart')
        

#make_adjacency_list((1,2), (1,3), (2,1), (2,4), 1, 2, 3, 'abc')
"""
 for arg in args:
        print(arg)
    print('done with args')
    for key_word_arg in kwargs:
        print(kwargs[key_word_arg])
"""

test_case = make_adjacency_list([(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4)])




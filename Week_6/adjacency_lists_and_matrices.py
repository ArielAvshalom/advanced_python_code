# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:12:46 2022

node : edgelist of the node

1 : [2,3]
2 : [1,4]
3 : 1,4 
4 : 2,3,5
5 : 4


What input do you envision?
(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4), (5,6) ...
[(1,2), (1,3), (2,1), (2,4)]
We might also get that there are 5 nodes for example

explaining args and kwargs:
    
     for arg in args:
            print(arg)
        print('done with args')
        for key_word_arg in kwargs:
            print(kwargs[key_word_arg])
    

@author: Ariel
"""

from pprint import pprint

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

#our code in this case is case 1 (1,4) means 1 -> 4

        
#input: 
#make_adjacency_list((1,2), (1,3), (2,1), (2,4), 1, 2, 3, 'abc', key = '123', key2 = 'my heart')
        

#make_adjacency_list((1,2), (1,3), (2,1), (2,4), 1, 2, 3, 'abc')




def count_nodes(*args):
    
    set_of_nodes = set()
    for edge_pair in args:
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1])
        
    return set_of_nodes, len(set_of_nodes)

#how would we fix an issue like off by one in this case?


def make_adjacency_matrix(*args):
   

    count = count_nodes(*args)[1]
    
    adjacency_matrix = []
    
    list_to_append = []
    
    for value in range(count+1):
        list_to_append.append(0)
    
    for value in range(count+1):
        adjacency_matrix.append(list_to_append[:])
    
    
    for edge_value in args:
        adjacency_matrix[edge_value[0]][edge_value[1]] = 1
    
    pprint(adjacency_matrix)
    
    return adjacency_matrix
    
    

if __name__ == "__main__":
    #implicit error example
    make_list_case = make_adjacency_list([(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4)])

    make_list_case = make_adjacency_list([(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4)])

    count_test_1 = count_nodes((1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4))
    
    #possible implicit error:
    count_test_2 = count_nodes((1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4), (5,6))
    
    make_matrix_case = make_adjacency_matrix((1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (4,2), (4,3), (4,5), (5,4), (5,6))
    
    
#Here is your assignment

#remember those cases from earlier? Now you have to do that

#I want you to write code for either other use case
#give me code for an adjacency list and matrix for both of those cases specifically functions
# (1,4) 4->1 and also the case of 1->4 and 4->1

#Write up those functions into a class for lists and a class for matrices

#besides creating a list and matrix, they should also do things like give me an edgelist, and give me a count of all nodes 

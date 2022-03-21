# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:27:16 2022



psuedocode

DFS(G, n):
    visited[n] = True
    
    for each e that connects n:
        if we didn't visit that edge
        run dfs on that edge
        
make dict of nodes
and set each node to be false initially

for each node in graph
    set node to be unvisited
    
for each node in graph
    try to run dfs


@author: Ariel
"""

def dfs(graph, start, visited = None):
    """
    
    What the heck is it doing....
    It's running dfs and here is how
    blah blah data structure etc
    blah blah...
    

    Parameters
    ----------
    graph : TYPE
        DESCRIPTION.
    start : TYPE
        DESCRIPTION.
    visited : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    visited : TYPE
        DESCRIPTION.

    """
    if visited is None:
        visited = set()
        #alternatively we can use a dict as well.
    visited.add(start)
    
    print(start)
    
    

    for nextnode in graph[start] - visited:
        dfs(graph, nextnode, visited)
        
    return visited

graph = {
    '0' : set(['1','9']),
    '1' : set(['0','8']),
    '2' : set(['3']),
    '3' : set(['2','4','6','7']),
    '4' : set(['3']),
    '5' : set(['6','7']),
    '6' : set(['3', '5']),
    '7' : set(['3','5','8','10','11']),
    '8' : set(['1','7','9']),
    '9' : set(['0','8']),
    '10' : set(['7','11']),
    '11' : set(['7', '10']),
    '12' : set(['13']),
    '13' : set(['12']),
    '14' : set()
    }

if __name__ == "__main__":
    answer = dfs(graph, '0')






















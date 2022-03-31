"""Prompt       Graph Theory Data Structures

In class we created an adjacency list and adjacency matrix function which takes any number tuple edge_pairs and returns either an adjacency list (dictionary where the values are lists) or an adjacency matrix (implemented as a list of lists)

In class when given an edge_pair like (1,4) we assumed that the pairing is that 1 -> 4 (ie node 1 has a directed edge to node 4). For this assignment, you're going to do the following:

Part 1:

Create two functions, one which will convert any number of tuple edge_pairs into an adjacency list and one which will convert them to an adjacency matrix.

The difference is that now, the functions will check for an input from the user which will indicate the direction of an edge tuple. It will take in a key value pair which will be named "direction" and expected inputs are:
    '->' for left to right 
    '<-' for right to left 
    '<>' for both directions

So your functions should be able to check for and do all of these. You can either use if elif else logic for this and input separate logic for each case or use helper functions or possibly a slightly more clever approach...

Once you've created these functions, you're going to do the following:

-----------<BONUS

Bonus point opportunity, create an additional matrix function using a numpy array. Please note that a numpy array is not mutable, so it isn't recommended that you use it in the class functions below.

>-----------

Part 2:

Create the following classes: a class for adjacency lists and a class for adjacency matrices

Each class should be initialized as an empty adjacency list or matrix. I recommend initializing the matrix as a nXn matrix based on the number of nodes in the graph. It is important to note that if a new node is added, the matrix will have to change to an n+1Xn+1 matrix.

The classes should have a function to initialize the graph based on a prior edge list (ie the function code above set up to accept data via a class).

-----------<BONUS

The edge_tuples you receive for this section are no longer pairs, now they are triplets like (1,4,7) where the first value is the first node, the second value is the second node and the third value is the cost to traverse this edge.  

You will get extra credit for implementing edge costs into your program.

>-----------

The classes should also have:
    1.  A function that given a new edge_pair adds it to the data structure. Note that the case of the edge pair (->, <- or <>) depends on how the original data structure was initialized. It may be a good idea to specify that during initialization of an instance of the class.

    2.  A function which returns the node with the most edges in the cases of (these should work for any type graph):
            A:  edges leaving the node
            B:  edges pointing toward the node
            C:  edges with the most nodes pointing both towards and away from the node. This means to count all of the edges entering and exiting the node. This would be easier to see with a matrix where you add up all of the vertical and horizontal values for a particular node. 
    
    3.  A set of functions that given a starting node returns 
            A:  a BFS search of the graph
            B:  a DFS search of the graph
            C:  given an ending node as well, generate one path from the starting node to the ending node

            -----------<BONUS

            D:  a Single Source shortest path from that node to every other node in O(elogn) time for the adjacency list implementation and O(n^2) for the matrix implementation (n means nodes and e means edges)

            You should use the above edge cost bonus question for calculating shortest paths

            /Bonus>-----------

Grading rubric:

This will be graded out of twenty points. There are 25 total possible points.

You can receive a total of 8 points for completing part 1 and for adding those functions to the classes in part 2

You can receive 4 points for completing each section of part 2

You can receive a total of 5 bonus points:
    1 for the numpy implementation
    1 for adding edge costs to your classes
    3 for completely solving 2.3.D

"""

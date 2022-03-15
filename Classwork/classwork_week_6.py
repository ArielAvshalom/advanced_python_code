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

Bonus point opportunity, create an additional matrix function using a numpy array. Please note that a numpy array is not mutable, so it isn't recommended that you use it in the class functions below.

Part 2:

Create the following classes: a class for adjacency lists and a class for adjacency matrices

Each class should be initialized as an empty adjacency list or matrix. I recommend initializing the matrix as a nXn matrix based on the number of nodes in the graph. It is important to note that if a new node is added, the matrix will have to change to an n+1Xn+1 matrix.

"""
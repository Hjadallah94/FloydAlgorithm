"""
This is a code showing an implemention of 
the Floyd Warshall Algorithm.
Floyd Warshall Algorithm is designed to find 
the shortest distance between two nodes in a graph.
The code is developed in a recursive form.
"""

# Importing the sys module
import sys


# The number of verticies in the matrix
v = 4

# Defining infinity
INF = sys.maxsize

""" 
The function 'floyd' is defined to perform the 
algorithm where i and j are the rows and columns 
respectively. k is the intermediate node by which a 
shortest distance between the vertecies can be calculated.
"""

# Floyd Warshall Algorithm 
def floyd(graph):

    """
    Beginning of our solution.
    Assuming no intermediate values.
    """

    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    """
    Adding the vertices in the range v.
    The rows i, culoms j, and intermediates k, 
    should be within the range v.
    After that, the shortest distance is computed
    """

    for i in range(v):

        for j in range(v):

            for k in range(v):

                # Solving for the shortest distance
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Calling the function that prints the solution
    shortest_path(distance)

"""
The following function is created to print 
the result of Floyd Warshall Algorithm.
Again, i and j are in the reange of the matrix.
The "end" in the print function is used to allow 
for the matrix to add a new string. 
"""

def shortest_path(distance):

    for i in range(v):

        for j in range(v):

            # If there are no intermediate nodes, the result is infinity
            if(distance[i][j] == INF):

                print(INF, end="  ")

            # Otherwise, the shortest distance is printed 
            else:
            
                print(distance[i][j], end="  ")

        # Print in the following line after a string of 4 characters is formed
        print(" ")

# The program calls the above function and computes the matrix defined as "graph"
# The nodes and distances of the matrix below are created

"""
             8
       (1)------->(4)
        |         /|\
      7 |          |
        |          | 2
       \|/         |
       (2)------->(3)
             5         
 """

graph = [[0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]]

floyd(graph)
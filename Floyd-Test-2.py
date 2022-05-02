"""
import sys
import itertools

def floyd_test(distance):

    INF = 10000
    graph = [[0, 7, INF, 8],
             [INF, 0, 5, INF],
             [INF, INF, 0, 2],
             [INF, INF, INF, 0]]
    
    MAX_LENGTH = len(graph[0])

    for k, i, j\
    in itertools.product\
    (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):

    
        distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
        
    if distance [i] == [j]:

        return distance [i,j] == 0

    elif distance [i,j] == min([j],[j], [i,k] + [k,j]):

        return floyd_test(graph)


    floyd_test(distance)

    print (floyd_test(graph))


    """


print ("Hello\nWorld")
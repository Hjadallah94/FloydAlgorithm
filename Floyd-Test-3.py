
V = 4
INF = 99999
 
def floydWarshall(graph):

    for dist in range(V):

        for k in range(V):
 
            for i in range(V):
 
                for j in range(V):

                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    solved(dist)

def solved(dist):
    
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print (INF, end=" ")
            else:
                print ((dist[i][j]), end=' ')

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
         

floydWarshall(graph)

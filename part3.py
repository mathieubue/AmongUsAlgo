# Python Program for Floyd Warshall Algorithm 
  
# Number of vertices in the graph 
V = 14 
  
# Define infinity as the large enough value. This value will be 
# used for vertices not connected to each other 
INF  = 99999
  
# Solves all pair shortest path via Floyd Warshall Algorithm 
def floydWarshall(graph): 

    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph)) 
      

    for k in range(V): 
  
        # pick all vertices as source one by one 
        for i in range(V): 
  
            # Pick all vertices as destination for the 
            # above picked source 
            for j in range(V): 
  
                # If vertex k is on the shortest path from  
                # i to j, then update the value of dist[i][j] 
                dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                ) 
    #printSolution(dist) 
    return dist
  
  
# A utility function to print the solution 
def printSolution(dist): 
    print ("Following matrix shows the shortest distances between every pair of vertices :" )
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%7s" %("INF"), end='')
            else: 
                print ("%7d\t" %(dist[i][j]), end='')
            if j == V-1: 
                print ('')
def diff(matrix1,matrix2):
    diff =[]
    for i in range(14):
        row =[]
        for j in range(14):
            row.append(matrix2[i][j]-matrix1[i][j])
        diff.append(row)
    return diff
            

matrix_crewmate = [[0, 1, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3 ,1 ,1], #cafe
           [1, 0, 3, 1, INF, INF, INF, INF, INF, INF, INF, INF ,INF ,INF], #weapons
           [INF, 3, 0, 2, 3, INF, INF, INF, INF, INF, INF, INF ,INF ,INF], #nav
           [INF, 1, 2, 0, INF, INF, INF, INF, INF, INF, INF, INF ,INF ,INF],#o2
           [INF, INF, 3, INF, 0, 1, INF, INF, INF, INF, INF, INF ,INF ,INF],#shield
           [INF, INF, INF, INF, 1, 0, 2, INF, INF, INF, INF, INF ,INF ,INF],#com
           [INF, INF, INF, INF, INF, 2, 0, 2, INF, INF, INF, INF ,INF ,1],#storage
           [INF, INF, INF, INF, INF, INF, 2, 0, INF, 2, INF, INF ,INF ,INF],#elec
           [INF, INF, INF, INF, INF, INF, INF, INF, 0, 2, 2, 2 ,INF ,INF],#cam
           [INF, INF, INF, INF, INF, INF , INF, 2, 2, 0, 2,INF, INF, INF],#lowerE
           [INF, INF, INF, INF, INF, INF, INF, INF, INF, 2, 0, 2 ,INF ,INF],#reac
           [3, INF, INF, INF, INF, INF, INF, INF, 2, INF, 2, 0 ,2 ,INF],#upperE
           [1, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2 ,0 ,INF],#medB
           [1, INF, INF, INF, INF, INF, 1, INF, INF, INF, INF, INF ,INF ,0]]#admin

matrix_impostor = [[0, 1, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3 ,1 ,0], #cafe
           [1, 0, 0, 1, INF, INF, INF, INF, INF, INF, INF, INF ,INF ,INF], #weapons
           [INF, 0, 0, 2, 0, INF, INF, INF, INF, INF, INF, INF ,INF ,2], #nav
           [INF, 1, 2, 0, INF, INF, INF, INF, INF, INF, INF, INF ,INF ,2],#o2
           [INF, INF, 0, INF, 0, 1, INF, INF, INF, INF, INF, INF ,INF ,1],#shield
           [INF, INF, INF, INF, 1, 0, 2, INF, INF, INF, INF, INF ,INF ,INF],#com
           [INF, INF, INF, INF, INF, 2, 0, 2, INF, INF, INF, INF ,INF ,1],#storage
           [INF, INF, INF, INF, INF, INF, 2, 0, 0, INF, INF, INF ,0 ,INF],#elec
           [INF, INF, INF, INF, INF, INF, INF, 0, 0, 2, 2, 2 , 0,INF],#cam
           [INF, INF, INF, INF, INF, INF, INF, 2, 2, 0, 0,INF,INF ,INF],#lowerE
           [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, 0 ,INF ,INF],#reac
           [3, INF, INF, INF, INF, INF, INF, INF, 2, INF, 0, 0 ,2 ,INF],#upperE
           [1, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, 2 ,0 ,INF],#medB
           [0, INF, 2, 2, 1, INF, 1, INF, INF, INF, INF, INF ,INF ,0]]#admin
print("Crewmate")
printSolution(floydWarshall(matrix_crewmate))
print("Impostors")
printSolution(floydWarshall(matrix_impostor))
print("diff")
printSolution(diff(floydWarshall(matrix_impostor),floydWarshall(matrix_crewmate)))
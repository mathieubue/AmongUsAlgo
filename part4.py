
class Graph():  
    def __init__(self, vertices):  
        self.graph = [[0 for column in range(vertices)] 
                            for row in range(vertices)]  
        self.V = vertices
    def isSafe(self, v, pos, path):  
        # Check if current vertex and last vertex  
        # in path are adjacent  
        if self.graph[ path[pos-1] ][v] == 0:  
            return False
      
        # Check if current vertex not already in path  
        for vertex in path:  
            if vertex == v:  
                return False
      
        return True
      
    # A recursive utility function to solve  
    # hamiltonian cycle problem  
    def hamCycleUtil(self, path, pos):  
      
        # base case: if all vertices are  
        # included in the path  
        if pos == self.V:  
            # Last vertex must be adjacent to the  
            # first vertex in path to make a cyle  
            if self.graph[ path[pos-1] ][ path[0] ] == 1:  
                return True

            else:  
                return False

        # Try different vertices as a next candidate  
        # in Hamiltonian Cycle. We don't try for 0 as  
        # we included 0 as starting point in hamCycle()  
        for v in range(0,self.V):  
      
            if self.isSafe(v, pos, path) == True:  
      
                path[pos] = v  
      
                if self.hamCycleUtil(path, pos+1) == True:  
                    return True
      
                # Remove current vertex if it doesn't  
                # lead to a solution  
                path[pos] = -1
      
        return False
      
    def hamCycle(self):  
        path = [-1] * self.V  
      
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path,1) == False:  
            print ("Solution does not exist\n") 
            return False

        self.printSolution(path)  
        return True
      
    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                 "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 
  
# Driver Code  
  

gcrew = Graph(14) 

gcrew.graph = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ,1 ,1], #cafe
           [1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0], #weapons
           [0, 3, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0 ,0 ,0], #nav
           [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0],#o2
           [0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0 ,0 ,0],#shield
           [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0 ,0 ,0],#com
           [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0 ,0 ,1],#storage
           [0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0],#elec
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,0 ,0],#cam
           [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2,0,0 ,0],#lowerE
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2 ,0 ,0],#reac
           [3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0 ,2 ,0],#upperE
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 ,0 ,0],#medB
           [1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0 ,0 ,0]]#admin 
  
# Print the solution  
gcrew.hamCycle();  
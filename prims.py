import networkx as nx 

#file = open("n100e466.txt", 'r')
#G=nx.read_weighted_edgelist(file, nodetype=int,encoding='utf-8')

#Visited set
visited = set()
#First node
current = 0
#Min spanning tree
mst = []
#Edge attribute weight
smallest_neighbor = []




def prims(G,current):
    visited = set()
    #First node
    current = 0
    #Min spanning tree
    mst = []
    #Edge attribute weight
    smallest_neighbor = []
    
    while len(mst) < G.number_of_nodes()-1:
        
        for vert in G.neighbors(current):
            
            if vert not in visited: 
                
                smallest_neighbor.append([G[current][vert]['weight'],current,vert]) 
                           
        
    
        #Sorted list to get lowest weight
        sortedList= sorted(smallest_neighbor, reverse=True) 
        nextvert= sortedList[-1][2]
        sortedList.pop()
        
        while nextvert in visited:
            nextvert= sortedList[-1][2]
            sortedList.pop()
        
        
        #if current not in visited:
        visited.add(current)
        visited.add(nextvert)
        mst.append((current, nextvert))    
        current = nextvert
        
    return mst





    
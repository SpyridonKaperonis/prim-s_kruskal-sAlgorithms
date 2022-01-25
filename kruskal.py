import networkx as nx
import pandas as pd



#G=nx.read_weighted_edgelist("n100e466.txt", nodetype=int,encoding='utf-8')

def kruskal(G):
    mst = []
    smallest_neighbor = []
    storage = []
    


    sets = dict()
    for i in range(100):
        sets[i]= set([i])
    


    for edge in G.edges():
        smallest_neighbor.append([edge])
    for i in range(G.number_of_edges()-1):
        n1 = smallest_neighbor[i][0][0]
        n2 = smallest_neighbor[i][0][1]
        storage.append([G[n1][n2]['weight'],n1,n2])
 
    
    sortedByweight = sorted(storage, reverse=True)
   

    #Adds items to mst
    while len(mst) < (G.number_of_edges() -1):
        if len(sortedByweight)==0:
            return mst
        w,u,v = sortedByweight.pop()
        if not v in sets[u]:
            mst.append((w,u,v))
            newset = sets[u]|sets[v]
            for n in newset:
                sets[n]=newset
    
    
    return mst




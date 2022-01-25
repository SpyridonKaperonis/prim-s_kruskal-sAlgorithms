# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:38:09 2020

@author: Spyridon Kaperonis
"""
import networkx as nx
import time
from kruskal import kruskal
from prims import prims

#Data to work
current=0
file466e ='n100e466.txt'
file984e ='n100e984.txt'
file1453e ='n100e1453.txt'
file1978e ='n100e1978.txt'
file2451e ='n100e2451.txt'
file2969e ='n100e2969.txt'
file3439e ='n100e3439.txt'
file3947e ='n100e3947.txt'
file4446e ='n100e4446.txt'

files = []
timeP = []
timeK = []




files.append([file466e, 466])
files.append([file984e, 984])
files.append([file1453e, 1453])
files.append([file1978e, 1978])
files.append([file2451e, 2451])
files.append([file2969e, 2969])
files.append([file3439e, 3439])
files.append([file3947e, 3947])
files.append([file4446e, 4446])





def countPrimsKruskals(IterNum, EdgesNum):
    Kavlist = []
    Pavlist = []
    count = 0
    averageP =0
    averageK = 0
    while count < IterNum: 
        for i in range(len(files)): 
            W=nx.read_weighted_edgelist(files[i][0], nodetype=int,encoding='utf-8')
            #Prims timing
            startP = time.perf_counter()
            prims(W, current)
            stopP = time.perf_counter()
            #Prims timing
            timingP = stopP - startP
            timeP.append([timingP, files[i][1]])
            
        for k in range(len(files)):    
            M=nx.read_weighted_edgelist(files[k][0], nodetype=int,encoding='utf-8')
            #Kruskasl timing
            startK = time.perf_counter()
            kruskal(M)
            stopK = time.perf_counter()
            #Kruskals timing
            timingK = stopK - startK
            timeK.append([timingK, files[k][1]])
    
        count+=1   
    for l in range(len(timeK)):
        if timeK[l][1] == EdgesNum:
            Kavlist.append(timeK[l][0])
        
    for m in range(len(timeP)):
        if timeP[m][1] == EdgesNum:
            Pavlist.append(timeP[m][0])
    #Average calc for prims edges results
    for n in Pavlist:
        averageP += n
        averageP = averageP / len(Pavlist)
    for p in Kavlist:
        averageK += p
        averageK = averageK / len(Kavlist)
        
    
    print("Iterations:", IterNum, "Edges: ",EdgesNum,"Kruskals: ",averageK)
    print("Iterations:", IterNum, "Edges: ",EdgesNum,"Prims: ",averageP)
    
        
    #print(averageP)
def printing():    
    print("Manual or autopilot?(type M or A accordingly) : ")
    MorA = input()

    if MorA == 'M' or MorA == 'm':
        print("Enter number of iterations: ")
        x = input()
        x = int(x)
        print("You can choose between 466, 984, 1453, 1978, 2451, 2969, 3439, 3947 or 4446. Enter number of edges: ")
        y = input()
        y = int(y)
        countPrimsKruskals(x, y)
        
    if MorA == 'A' or MorA =='a':
        countPrimsKruskals(100, 466)
        countPrimsKruskals(100, 984)
        countPrimsKruskals(100, 1453)
        countPrimsKruskals(100, 1978)
        countPrimsKruskals(100, 2451)
        countPrimsKruskals(100, 2969)
        countPrimsKruskals(100, 3439)
        countPrimsKruskals(100, 3947)
        countPrimsKruskals(100, 4446)
    
    else:
        printing()
    
printing()   




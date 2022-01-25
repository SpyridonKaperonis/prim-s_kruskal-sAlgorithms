# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:56:24 2020

@author: Spuro
"""

import networkx as nx
import pandas as pd
from collections import OrderedDict
from kruskal import kruskal
from prims import prims
#import itertools.combinations as comb


G=nx.read_weighted_edgelist("n100e466.txt", nodetype=int,encoding='utf-8')

current =0
df = [(1,2), (2,3), (3,1)]
headers = ["n1", "n2"]
dataframe = pd.DataFrame.from_dict(prims(G))
                                  
l= nx.from_pandas_edgelist(dataframe, source= 1, target= 2)
nx.draw(l)

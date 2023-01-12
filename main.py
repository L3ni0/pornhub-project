from pornhub_api import PornhubApi
import networkx as nx
import itertools
import pandas as pd
import matplotlib.pyplot as plt
from time_conv import *
from graph import PornGraph
from pyvis.network import Network

grap = PornGraph()
grap.from_csv('merged.csv')

list_qliques = grap.biggest_clique()
for i in list_qliques:
    print(i)

# grap.show('finally')


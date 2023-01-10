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
grap.show('fromcvs')


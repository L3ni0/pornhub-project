from pornhub_api import PornhubApi
import networkx as nx
import itertools
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from time_conv import *
from graph import PornGraph
import json
from pyvis.network import Network
import sys 
api = PornhubApi()

df = pd.DataFrame(columns=['pornstars','duration','title','date'])

videos = []
k=0
for idk_why in api.video.categories():
    for cat in idk_why[1]:
        
        if cat.category != 'red-head' and k == 0:
            continue
        k=1
        print(cat.category)
        for i in range(1,1001):
            
            try:
                data = api.search.search(
                    ordering="mostviewed",
                    period="all-time",
                    category=cat.category,
                    page=i
                )
            except:
                continue


            
            print(f'download {i}')
            for vid in data.videos:
                if vid.pornstars:
                    pornstar_names = '|'.join([x.pornstar_name for x in vid.pornstars])
                    videos.append([pornstar_names, vid.title, vid.duration,vid.publish_date.date()])


        df = pd.DataFrame(videos, columns=['pornstars','title','duration','date'])
        df.to_csv('23videos.csv')

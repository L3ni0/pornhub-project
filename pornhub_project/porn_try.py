from pornhub_api import PornhubApi
import networkx as nx
import itertools
import pandas as pd
import matplotlib.pyplot as plt
from time_conv import *
from graph import PornGraph
from pyvis.network import Network

api = PornhubApi()


df = pd.DataFrame(columns=['pornstar_1','pornstar_2','duration','titles'])
for i in range(1,10000):
    data = api.search.search(
        ordering="mostviewed",
        period="all-time",
        page=i
    )


    
    print(f'download {i}')
    for vid in data.videos:
        if vid.pornstars:
            for star1, star2 in itertools.combinations(vid.pornstars,2):
                lists = [*sorted([star1.pornstar_name, star2.pornstar_name]), str_to_seconds(vid.duration),f'{vid.title}']
                df.loc[len(df)] = lists

df_names = df.groupby(['pornstar_1','pornstar_2'])['titles'].apply('\n'.join).reset_index()
df_durations = df.groupby(['pornstar_1','pornstar_2'])['duration'].apply(sum)
df = pd.merge(df_names,df_durations, on =['pornstar_1','pornstar_2'])
df['duration'] = df['duration'].apply(sec_to_time)
df.to_csv('merged.csv')
print(df)



# G = PornGraph()
# for i in range(1,10):
#     
#     print(f'download {i}')
#     for vid in data.videos:
#         if vid.pornstars:
#             G.add_vid(vid)
        
#     print(i)

# G.show('test')

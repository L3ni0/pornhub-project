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

if __name__ == '__main__':

    api = PornhubApi()


    # downoad videos
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

    df_names = df.groupby(['pornstar_1','pornstar_2'])['titles'].apply('--'.join).reset_index()
    df_durations = df.groupby(['pornstar_1','pornstar_2'])['duration'].apply(sum)
    df = pd.merge(df_names,df_durations, on =['pornstar_1','pornstar_2'])
    df['duration'] = df['duration'].apply(sec_to_time)
    df.to_csv('merged.csv')
    print(df)

    all_stars =  api.stars.all_detailed()

    #download stars

    dictionary = {} # kochane api ma ciekawy format
    for one in list(all_stars): # nie dało się inaczej, po [0][0] itd wywala błąd
        for two in one:
            for star in two:
                for cos in star:
                    for idk in cos:
                        try:
                            print(idk.star_name, idk.star_thumb, idk.videos_count_all)
                            dictionary[idk.star_name.lower()] = [idk.star_thumb, idk.videos_count_all]
                            print()
                        except:
                            pass

    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df.to_csv('stars.csv')


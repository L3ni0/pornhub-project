import networkx as nx
import matplotlib.pyplot as plt
from time_conv import *
import itertools
import pandas as pd
from pyvis.network import Network

class PornGraph:


    def __init__(self) -> None:
        self.N = nx.Graph()
        


    def save_graph(self):
        nx.write_graphml(self.G, 'graph.graphml')

    def import_file(self,path:str):
        self.N = nx.read_graphml(path)
    
    def add_vid(self,vid):
        for star1, star2 in itertools.combinations(vid.pornstars,2):

            if not star1.pornstar_name in self.N.nodes:
                self.N.add_node(star1.pornstar_name)
            if not star2.pornstar_name in self.N.nodes:
                self.N.add_node(star2.pornstar_name)
            
            self.N.add_edge(star1.pornstar_name,star2.pornstar_name, value=str_to_seconds(vid.duration), title=f'{vid.title} time:{vid.duration}', date=str(vid.publish_date),physic=False)

    def from_csv(self,dir):
        df = pd.read_csv(dir)
        df_stars = pd.read_csv('stars.csv', index_col=0)
        names = df_stars.index.values.tolist() 
        for i,data in df.iterrows():
            if not data.pornstar_1 in self.N.nodes:

                if data.pornstar_1.lower() in names:
                    url, moveis = df_stars.loc[data.pornstar_1.lower()]
                    self.N.add_node(data.pornstar_1, shape='circularImage', image=url)
                else:
                    self.N.add_node(data.pornstar_1)
            if not pd.isna(data.pornstar_2):
                if not data.pornstar_2 in self.N.nodes:
                    if data.pornstar_2.lower() in names:
                        url, moveis = df_stars.loc[data.pornstar_2.lower()]
                        self.N.add_node(data.pornstar_2, shape='circularImage', image=url)
                    else:
                        self.N.add_node(data.pornstar_2)
                self.N.add_edge(data.pornstar_1, data.pornstar_2, value=time_to_sec(data.duration), title=f'{data.titles, data.duration}')

            else:
                self.N.add_edge(data.pornstar_1, data.pornstar_1, value=time_to_sec(data.duration), title=f'{data.titles, data.duration}')
        # deleting non connected nodes
        nodes = max(nx.connected_components(self.N), key=len)
        self.N = nx.subgraph(self.N, nodes)  

        self.diameter = nx.diameter(self.N)
        self.density = nx.density(self.N)


    def biggest_clique(self):

        def check(big_list, sublist):
            for test in big_list:
                if sublist in test and test != sublist:
                    return False
            
            return True

        cliques = [*nx.find_cliques(self.N)]

        return [x for x in cliques if check(cliques,x)]
        


    def show(self,name='graph'):

        self.G = Network(height="1450px", width="100%", bgcolor="#222222", font_color="white")
        self.G.from_nx(self.N)
        self.G.set_edge_smooth('straightCross')
        self.G.barnes_hut(central_gravity=0.5,spring_length=700)
        self.G.show_buttons()
        self.G.show(f'{name}.html')


graph = PornGraph()
graph.from_csv('converted.csv')
graph.show('stest')
import networkx as nx
import matplotlib.pyplot as plt
from time_conv import str_to_seconds
import itertools
from pyvis.network import Network

class PornGraph:


    def __init__(self) -> None:
        self.G = Network()


    def save_graph(self):
        nx.write_graphml(self.G, 'graph.graphml')

    def import_file(self,path:str):
        self.G = nx.read_graphml(path)
    
    def add_vid(self,vid):
        for star1, star2 in itertools.combinations(vid.pornstars,2):

            if not star1.pornstar_name in self.G.nodes:
                self.G.add_node(star1.pornstar_name)
            if not star2.pornstar_name in self.G.nodes:
                self.G.add_node(star2.pornstar_name)
            
            self.G.add_edge(star1.pornstar_name,star2.pornstar_name, value=str_to_seconds(vid.duration), title=f'{vid.title} time:{vid.duration}', date=vid.publish_date)

    def show(self,name='graph'):
        self.G.show(f'{name}.html')
  
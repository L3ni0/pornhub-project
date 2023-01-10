import networkx as nx
import matplotlib.pyplot as plt
from time_conv import str_to_seconds
import itertools
from pyvis.network import Network

class PornGraph:


    def __init__(self) -> None:
        self.G = Network(height="1450px", width="100%", bgcolor="#222222", font_color="white")
        self.G.set_edge_smooth('straightCross')
        self.G.barnes_hut(central_gravity=0.5,spring_length=700)
        


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
            
            self.G.add_edge(star1.pornstar_name,star2.pornstar_name, value=str_to_seconds(vid.duration), title=f'{vid.title} time:{vid.duration}', date=str(vid.publish_date),physic=False)

    def show(self,name='graph'):
        self.G.show_buttons()
        self.G.show(f'{name}.html')
  
import networkx as nx
import matplotlib.pyplot as plt

class PornGraph:


    def __init__(self) -> None:
        self.G = nx.Graph()


    def save_graph(self):
        nx.write_graphml(self.G, 'graph.graphml')

    def import_file(self,path):
        self.G = nx.read_graphml(path)

    def display(self):
        nx.draw(self.G)
        plt.show()
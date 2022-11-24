from turtle import pos, position
import itertools
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


class Graph():

    def __init__(self,n):
        self.nodes = tuple([*range(n)])

        
        self.positions =  {}
        for i in range(n):
            while (x:=random.randint(0,100),y:=random.randint(0,100)) in self.positions.keys():
                pass
            self.positions[i] = (x,y)


        self.init_graph()

    def init_graph(self):
        self.G = nx.Graph()
        self.G.add_nodes_from(self.nodes)

    def euklides_dist(self,n1,n2):
        x_dist = self.positions[n1][0] - self.positions[n2][0]
        y_dist = self.positions[n1][1] - self.positions[n2][1]
        return np.sqrt(np.abs(x_dist)**2+np.abs(y_dist)**2)

    def geo_rule(self):
        self.init_graph()

        #makin list of closest nodes
        distances = {}
        for n1,n2 in itertools.combinations(self.nodes,2):
            distances[(n1,n2)] = self.euklides_dist(n1,n2)

        distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        
        key = list(distances.keys())
        self.G.add_edge(key[0][0],key[0][1])
        i = 1
        while not nx.is_connected(self.G):
            self.G.add_edge(key[i][0],key[i][1])
            i += 1
        

        nx.draw(G=self.G, pos=self.positions)
        plt.show()



g1 = Graph(30)
g1.geo_rule()
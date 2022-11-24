import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['shrek','fiona','osioł','farquad','ciastek','żwirek','muchomorek','smoczyca','pinokio','świnki','wilk'])


G.add_edges_from([('shrek','fiona'),('shrek','osioł'),('fiona, osioł'),('fiona','farquad'),('shrek','farquad'),('sh')])


nx.draw(G,with_labels=True)
plt.show()
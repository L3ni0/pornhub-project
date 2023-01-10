from pyvis.network import Network

n  = Network()

n.add_node(1)
n.add_node(2)
n.add_edge(1,2,value=1)
n.add_edge(1,2,value=5)

n.save_graph('ss.html')
import networkx as nx
import matplotlib.pyplot as plt
import random


def random_connected_graph(n,k):
    """creating random connected graph
       n - number of nodes
       k - number of edges   n<=k"""

    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from([(x,x+1) for x in range(n-1)])
    k -=n
    while k > 0:
        if (l:= random.randint(0,n-1)) != (p := random.randint(0,n-1)) and(  (l,p) not in G.edges or (l,p) not in G.edges) :
            G.add_edge(l,p)
            k -= 1
    
    return G

G = random_connected_graph(10,24)





print(G.edges)

# znajdowanie najkrotszych Scieżek
shortest_paths = []
for i in range(len(G.nodes)):        
    for j in range(len(G.nodes)): 
        if i != j:
            w = nx.all_shortest_paths(G=G, source=i,target=j)
            shortest_paths.append(next(w))
            

avg_shortes_path = sum([len(x)-1 for x in shortest_paths])/len(shortest_paths)
print(f'srednia najkrotszych = {avg_shortes_path}')

# wyliczanie opóźnienia
for i in range(len(G.nodes)):
    F = len(shortest_paths)
    fl = sum([i in x  for x in shortest_paths]) 

    print(f'opoznienie krawedzi {i}  wynosi {1/((F+1)-fl)}')



# rysowanie grafu
print(G.edges)
nx.draw(G)
plt.show()
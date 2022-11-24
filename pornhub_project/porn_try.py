from pornhub_api import PornhubApi
import sqlalchemy as db
import pandas as pd
import networkx as nx
import itertools
import matplotlib.pyplot as plt
from time_conv import str_to_seconds
from graph import PornGraph
from pyvis.network import Network

# engine = db.create_engine('postgresql://postgres:dominik123@localhost/postgres')
# conn = engine.connect()
api = PornhubApi()

# conn.execute('CREATE TABLE IF NOT EXISTS data (vid_id text PRIMARY KEY, pornstars text, title text)')
# print(pd.read_sql("SELECT * FROM information_schema.columns WHERE table_name = 'data'", engine))


data = api.search.search(
    ordering="mostviewed",
    period="all-time",
)


G= nx.Graph()

for vid in data.videos:
    if vid.pornstars:
        for star1, star2 in itertools.combinations(vid.pornstars,2):

            if not star1.pornstar_name in G.nodes:
                G.add_node(star1.pornstar_name)
            if not star2.pornstar_name in G.nodes:
                G.add_node(star2.pornstar_name)
            
            G.add_edge(star1.pornstar_name,star2.pornstar_name, wage=str_to_seconds(vid.duration), name=vid.title)
        # print(vid.title)
        # print(vid.pornstars)
        # print(vid.video_id)
        # print(vid.duration)
        # print(vid.publish_date)

nx.write_graphml(G, 'graph.graphml')
nt = Network()
nt.from_nx(G)
nt.show('nx.html')
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


G = PornGraph()

for vid in data.videos:
    if vid.pornstars:
        G.add_vid(vid)
        
G.show('nx.html')
import pandas as pd

df = pd.read_csv('merged.csv',index_col=None)
df = df.head(20)
for i,data in df.iterrows():
    print(data)

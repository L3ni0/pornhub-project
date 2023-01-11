import pandas as pd

df = pd.read_csv('stars.csv', index_col=0)
url, moveis = df.loc['AJ Applegate']
print(url)


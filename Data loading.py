 import pandas as pd

df = pd.read_csv("metadata.csv", low_memory=False)
print(df.shape)
df.head()

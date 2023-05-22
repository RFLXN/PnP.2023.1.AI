import pandas as pd

df = pd.read_csv('data/world_cities.csv')

# 여기에 코드를 작성하세요
len(df["City / Urban area"].unique())
len(df["Country"].unique())

df["Den"] = df["Population"] / df["Land area (in sqKm)"]
filtered = df.loc[df["Den"] >= 10000]

len(filtered["City / Urban area"])

df.sort_values("Den")
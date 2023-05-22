import pandas as pd

df = pd.read_csv('data/world_cities.csv')

# 여기에 코드를 작성하세요
counts = df["Country"].value_counts()
counts[counts == 4]
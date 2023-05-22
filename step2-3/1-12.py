import pandas as pd

df = pd.read_csv('data/starbucks_drinks.csv')

# 여기에 코드를 작성하세요
df.plot.box(y="Calories")
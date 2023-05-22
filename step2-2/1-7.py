import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 여기에 코드를 작성하세요
df.loc[2012:2017, "KBS":"SBS"]
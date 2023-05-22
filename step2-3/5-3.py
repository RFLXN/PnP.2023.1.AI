import pandas as pd

df = pd.read_csv('data/museum_1.csv')

# 여기에 코드를 작성하세요
univ = df["시설명"].str.contains("대학")

df.loc[univ, "분류"] = "대학"
df.loc[~univ, "분류"] = "일반"
df
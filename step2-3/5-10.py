import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 여기에 코드를 작성하세요
male = df["gender"] == "M"
female = df["gender"] == "F"

df.loc[male, "gender"] = 0
df.loc[female, "gender"] = 1

df.groupby("occupation").mean()["gender"].sort_values(ascending=False)
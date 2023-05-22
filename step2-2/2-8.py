import pandas as pd

df = pd.read_csv('data/Puzzle_before.csv')

# 여기에 코드를 작성하세요
df["A"] = df["A"] * 2
df[df.loc[:, "B":"E"] < 80] = 0
df[df.loc[:, "B":"E"] >= 80] = 1
df.loc[2, "F"] = 99
# 테스트 코드
df

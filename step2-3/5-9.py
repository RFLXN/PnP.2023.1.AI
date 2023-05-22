import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 여기에 코드를 작성하세요
group = df.groupby("occupation")
group.mean().sort_values(by="age")
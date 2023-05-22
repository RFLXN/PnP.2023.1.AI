import pandas as pd

df = pd.read_csv('data/museum_2.csv')

# 여기에 코드를 작성하세요
area_num = df["운영기관전화번호"].str.split("-", n=2, expand=True)

df["지역번호"] = area_num[0]
df
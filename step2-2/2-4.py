import pandas as pd

df = pd.read_csv('data/body_imperial1.csv', index_col=0)

# 여기에 코드를 작성하세요
df.iloc[1, 1] = 200
df.drop(21, axis="index", inplace=True)
df.loc[20] = [70, 200]
# 테스트 코드
df
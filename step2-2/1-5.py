import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 여기에 코드를 작성하세요
df = pd.merge(samsong_df[["요일", "문화생활비"]], hyundee_df[["요일", "문화생활비"]], on="요일")
df.columns = ["day", "samsong", "hyundee"]
df
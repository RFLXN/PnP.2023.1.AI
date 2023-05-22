import pandas as pd
import seaborn as sns

df = pd.read_csv('data/survey.csv')

# 여기에 코드를 작성하세요
sns.clustermap(df.loc[:, "Horror":"Action"].corr())
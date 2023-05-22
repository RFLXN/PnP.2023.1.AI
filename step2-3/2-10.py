import pandas as pd
import seaborn as sns

df = pd.read_csv('data/insurance.csv')

# 여기에 코드를 작성하세요
sns.catplot(data=df, kind="violin", x="smoker", y="charges")

import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')

# 여기에 코드를 작성하세요
filter = (df["gender"] == "Male") & (df["job_category"] == "Managers")
except_all = filter & (df["race_ethnicity"] != "All")
df.loc[except_all, ["race_ethnicity", "count"]].plot.bar(x="race_ethnicity", y="count")
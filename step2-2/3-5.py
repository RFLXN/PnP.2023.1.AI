import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 여기에 코드를 작성하세요
df["status"] = "allowed"

it_filter = (df["course name"] == "information technology") & (df["year"] == 1)
df.loc[it_filter, "status"] = "not allowed"

commerce_filter = (df["course name"] == "commerce") & (df["year"] == 4)
df.loc[commerce_filter, "status"] = "not allowed"

counts = df["course name"].value_counts()
counts_filter = counts[counts < 5]
counts_names = list(counts_filter.index)

for name in list(counts_names):
    filter = df["course name"] == name
    df.loc[filter, "status"] = "not allowed"

# 테스트 코드
df
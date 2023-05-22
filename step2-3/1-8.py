import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 여기에 코드를 작성하세요
adobe = df["company"] == "Adobe"
except_zero = df["count"] != 0
except_totals = (df["job_category"] != "Totals") & (df["job_category"] != "Previous_totals")
race = df["race"] == "Overall_totals"
filter = adobe & except_zero & except_totals & race

category = df.loc[filter, ["count", "job_category"]]
category.set_index("job_category", inplace=True)
category.plot.pie(y="count")
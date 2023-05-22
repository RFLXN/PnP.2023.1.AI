import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 여기에 코드를 작성하세요
rooms = list(df["room assignment"].unique())

for room in rooms:
    courses = df[df["room assignment"] == room]["course name"].unique()
    sorted = list(pd.Series(courses).sort_values())
    for i in range(len(sorted)):
        course_name = sorted[i]
        rp = room.replace(" room", "")
        room_name = f"{rp}-{str(i+1)}"
        df.loc[df["course name"] == course_name, "room number"] = room_name

df.loc[df["room assignment"] == "not assigned", "room number"] = "not assigned"

df.drop(columns=["room assignment"], inplace=True)
# 테스트 코드
df
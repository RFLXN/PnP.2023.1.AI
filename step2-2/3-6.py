import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')


# 여기에 코드를 작성하세요

def set_room(course_names, room_name):
    for name in course_names:
        filter = (df["course name"] == name) & (df["status"] == "allowed")
        df.loc[filter, "room assignment"] = room_name


counts = df["course name"].value_counts()

aud = list(counts[counts >= 80].index)
set_room(aud, "Auditorium")

lg = list(counts[(counts >= 40) & (counts < 80)].index)
set_room(lg, "Large room")

md = list(counts[(counts >= 15) & (counts < 40)].index)
set_room(md, "Medium room")

sm = list(counts[(counts >= 5) & (counts < 15)].index)
set_room(sm, "Small room")

df.loc[df["status"] == "not allowed", "room assignment"] = "not assigned"

# 테스트 코드
df

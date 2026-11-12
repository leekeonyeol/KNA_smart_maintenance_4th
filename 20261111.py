import numpy as np
import pandas as pd 

# 실습 1번 
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# print(df_shot["비스킷두께"] >= 16) 
# print(df_shot[df_shot["비스킷두께"] >= 16])
# a = df_shot[df_shot["비스킷두께"] >= 16]
# b = df_shot[df_shot["비스킷두께"] < 16]
# c = df_shot[df_shot["비스킷두께"].isna()]
# print(len(a))
# print(len(b))
# print(len(c))

# 실습 2번
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# condition = (df_shot["비스킷두께"] >= 16) & (df_shot["사이클타임"] >= 25)
# print(condition.sum())
# condition_1 = (df_shot["비스킷두께"] >= 16) | (df_shot["사이클타임"] >= 25)
# print(condition_1.sum())
# condition_2 = ~(df_shot["품질등급"] == "불량")
# print(condition_2.sum())

# 복습
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# print(df_shot["설비ID"].head(1).tolist())
# print(df_shot["설비ID"].str.split("-").head(1).tolist())

# line = df_shot["설비ID"].str.split("-").str[1]
# numb = df_shot["설비ID"].str.split("-").str[2]
# print((line == "A").sum(), (line == "B").sum())
# print(df_shot["설비ID"].str.replace("-"," ", regex=False).head(1).tolist()) 
# #  regex=False 는 글자를 그대로 취급

# 실습 3번
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# a = df_shot["품질등급"].isin(["불량","주의"])
# print(a.sum())
# b = df_shot["비스킷두께"].between(10,16)
# print(b.sum())
# c = df_shot["설비ID"].str.contains("A")
# print(c.sum())
# d = df_shot["설비ID"].str.contains("A-01")
# print(d.sum())

# 실습 4번
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# print(df_shot.sort_values(["비스킷두께"], ascending=False))
# print(df_shot.sort_values(["품질등급", "사이클타임"], ascending=[True, False]).head(5))

# # 실습 5번
# df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# print(df_shot[~(df_shot["품질등급"] == "양품") & (df_shot["비스킷두께"] >= 16)])
# a = df_shot[~(df_shot["품질등급"] == "양품") & (df_shot["비스킷두께"] >= 16)]
# print(a.sort_values(["비스킷두께"], ascending=False))
# b = a.sort_values(["비스킷두께"], ascending=False)
# print(b[["품질등급", "비스킷두께", "실린더압력"]].head(5))
# print(a["품질등급"].isna().sum())

# 
# import pandas as pd
# log = pd.read_csv('data/13_diecasting_shot.csv')
# master = pd.read_csv('data/13_diecasting_master.csv')
# three = log.head(3)[['샷', '설비ID', '비스킷두께']] # 앞 세 줄 · 세 칸만
# print(three.to_string(index=False))
# # 샷 설비ID 비스킷두께
# # 1 DIE-A-01 10.0
# # 2 DIE-B-01 11.0
# print(three.merge(master, on='설비ID').to_string(index=False)) # to_string = 모든 행을 줄임없이 보여준다, index = False는 번호, 이름표 부여를 하지않는다.
# # 샷 설비ID 비스킷두께라인 도입연도 정격형체력담당반
# # 1 DIE-A-01 10.0 A 2018 280 1반
# # 2 DIE-B-01 11.0 B 2020 320 2반

# print(log.shape, master.shape) # (200, 8) (5, 5)
# merged = log.merge(master, on='설비ID') # on = 두 표를 잇는 키 열
# print(merged.shape) # (185, 12)
# # 열은 8 + 5 - 1 = 12 키 열 설비ID 는 한 번만 남는다
# print(merged[['샷', '설비ID', '라인', '도입연도']].head(2).to_string(index=False))
# # 샷 설비ID 라인 도입연도
# # 1 DIE-A-01 A 2018
# # 2 DIE-B-01 B 2020

# 실습 1번
# log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")
# print(log.shape, master.shape) # (200, 8) (5, 5)
# print(log.columns.tolist(), master.columns.tolist()) # "설비ID"
# merged = log.merge(master, on="설비ID")
# print(merged.shape)

# 실습 2번
# log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")

# merged = log.merge(master, on="설비ID")
# print(merged.shape)
# merged_1 = log.merge(master, on="설비ID", how="left")
# print(merged_1.shape)
# merged_2 = log.merge(master, on="설비ID", how="outer")
# print(merged_2.shape)
# # inner는 짝이 있는 행만
# # left는 짝이 있는 행 + 왼쪽에만 있는 행
# # outer는 짝이 있는행 + 왼쪽에만 있는 행 + 오른쪽에만 있는 행
# print(merged_1["설비ID"][merged_1["라인"].isna()])
# print(merged_1["라인"].isna().sum())
# print(merged_2["설비ID"][merged_2["샷"].isna()])

# 실습 3번
log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
data_1 = log.iloc[0:100].reset_index(drop=True)
data_2 = log.iloc[100:].reset_index(drop=True)
print(data_1.shape, data_2.shape)
concated = pd.concat([data_1, data_2])
print(concated, len(concated.loc[0]))
concated_1 = pd.concat([data_1, data_2], ignore_index=True)
print(concated_1.index[-1])

# 실습 4번
log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")
merged = log.merge(master, on="설비ID", how="left")
print(merged[merged["라인"].isna()])
merged_1 = merged[merged["라인"].isna()]
print(merged_1[merged_1["품질등급"] != "양품"])
merged_2 = merged_1[merged_1["품질등급"] != "양품"]
print(merged_2.sort_values(["비스킷두께"], ascending=False))


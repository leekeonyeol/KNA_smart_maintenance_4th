import numpy as np
import pandas as pd

small = pd.read_csv("data/13_diecasting_small_24_261110_3.csv", sep=",", encoding="utf-8")
log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")

# 문제 1번
# print(type(small["형체력"])) # series
# print(small["형체력"].head(3).tolist()) # 앞 세개 리스트
# print(type(small[["형체력","실린더압력"]])) # dataframe
# print(small[["형체력","실린더압력"]].shape) # (30,2)

# 문제 2번
# a = small.head(5)
# b = small.loc[0:4, ["실린더압력","형체력"]]
# c = small.iloc[0:5, [2,6]]
# print(b.shape == c.shape)

# 문제 3번
# s = small.sort_values("형체력", ascending=False)
# print(s.loc[0,"샷"], s.iloc[0,0])
# t = s.reset_index(drop=True)
# print(t.loc[0,"샷"], t.iloc[0,0])
# print(s.reset_index().shape)

# 문제 4번
# a = log["비스킷두께"] >= 16
# print(a.sum(), len(log[a]))
# b = log["비스킷두께"] < 16
# print(b.sum(), log["비스킷두께"].isna().sum())

# 문제 5번
# a = (log["비스킷두께"] >= 16) & (log["사이클타임"] >= 25)
# print(a.sum())
# print((~(log["품질등급"] == "불량")).sum())

# 문제 6번
# print(log["품질등급"].isin(["주의","불량"]).sum())
# print(log["비스킷두께"].between(10,16).sum())
# print(log["설비ID"].str.contains("A").sum()) # 문자를 검색하므로 str이 중요! 
# print((log["설비ID"] == "DIE-A-01").sum())

# 문제 7번
# print(log.sort_values("비스킷두께", ascending=False)["샷"].head(5).tolist())
# print(log.sort_values(["품질등급", "사이클타임"], ascending=[True, False]).head(5)["샷"].tolist())
# m = log.sort_values(["품질등급", "사이클타임"], ascending=[True, False]).head(5)["샷"].tolist()

# 문제 8번
# print(log.shape, master.shape)
# merged = log.merge(master, on="설비ID") # 기본은 inner
# print(merged.shape)
# print(merged[["샷","설비ID","라인","도입연도"]].head(2).to_string(index=False))

# 문제 9번
# merged_1 = log.merge(master, on="설비ID", how="inner")
# merged_2 = log.merge(master, on="설비ID", how="left")
# merged_3 = log.merge(master, on="설비ID", how="outer")

# print(merged_2["라인"].isna().sum())
# print(merged_2["설비ID"][merged_2["라인"].isna()].head(1).tolist())
# print(merged_3[merged_3["샷"].isna()]["설비ID"])

# 문제 1번
log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")

# print(log.shape, master.shape)

# print(log.columns.tolist())
# print(master.columns.tolist()) # 설비ID

# merged = log.merge(master, on="설비ID")
# print(merged.shape)
# print(merged.head(2))

# 문제 2번
# merged = log.merge(master, on="설비ID", how="inner")
# print(len(merged))
# merged_1 = log.merge(master, on="설비ID", how="left")
# merged_2 = log.merge(master, on="설비ID", how="outer")
# print(merged_1["라인"].isna().sum())
# unmatched = merged_1[merged_1["라인"].isna()]
# print(unmatched["설비ID"].head(2).tolist())

# 문제 3번
# log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# a = log.iloc[:100].reset_index(drop=True)
# b = log.iloc[100:].reset_index(drop=True) 
# combine = pd.concat([a,b], ignore_index=True)
# print(combine.loc[0])
# print(combine.index[-1])

# 문제 4번
# log = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
# master = pd.read_csv("data/13_diecasting_master_24_261110_1.csv", sep=",", encoding="utf-8")

# merged = log.merge(master, on="설비ID", how="left")
# blank = merged[merged["라인"].isna()]
# print(len(merged) - len(blank))
# print(len(merged[merged["품질등급"] != "양품"]))
# a = merged[merged["품질등급"] != "양품"]
# print(a.sort_values(["비스킷두께"], ascending=False).head(5).to_string(index=False))
import pandas as pd
import numpy as np

# 실습 1번
df_comp = pd.read_csv("data/12_metro_compressor_22_261109_1.csv", sep=",", encoding="utf-8")
# print(df_comp.head())
# print(df_comp.tail())
# print(df_comp.head(3), df_comp.tail(10))
# print(df_comp["오일온도"]) # dataframe의 하나의 series

# 실습 2번
df_digital = pd.read_csv("data/12_metro_digital_22_261109_3.csv", sep=",", encoding="utf-8")
# a = df_digital.shape
# b = df_digital.columns.tolist() # 열의 목록을 보여준다.
# c = df_digital.dtypes
# d = df_digital.head()
# print(f"이 표는 {a}의 형태이고, 열 목록은 {b}이고, 자료형은 {c}이고, 상위 5줄은 {d}이다. ")

# 실습 3번
# print(df_comp.info())
# RangeIndex: 200 entries, 0 to 199
# 4   오일온도    199 non-null    float64

# cur = df_comp["모터전류"].values
# print(round(float(np.mean(cur)),2))
# print(df_comp.describe()) # info()는 dataframe, describe()는 dataframe 내부 

# 실습 4번
# print(df_comp.describe())
# print(df_comp["배출압력"].values)
# print(df_comp["가동상태"].values)
# a = df_comp["배출압력"].values # 배열, df_comp["배출압력"] = dataframe
# b = df_comp["가동상태"].values # 배열
# print(round(float(np.mean(a[b == "가동"])),2))
# print(round(float(np.mean(a[b == "정지"])),2))

# 실습 5번
# df_comp = pd.read_csv("data/12_metro_compressor_22_261109_1.csv", sep=",", encoding="utf-8")
# df_digital = pd.read_csv("data/12_metro_digital_22_261109_3.csv", sep=",", encoding="utf-8")
# print(df_comp.shape, df_digital.shape)
# print(df_comp.dtypes, df_digital.dtypes)
# # (str, float), (str, int)
# print(df_comp.info(), df_digital.info()) 
# # 결측 1건, 결측 0건 
# print(np.unique(df_digital["저압스위치"]))

# 실습 6번
# df_small = pd.read_csv("data/12_metro_small_22_261109_4.csv", sep=",", encoding="utf-8")
# print(df_small.head(3))
# print(df_small.shape)
# print(df_small.info())
# #  4   오일온도    29 non-null     float64 : 결측 1건
# print(df_small.describe())

# a = len(df_small)
# b = df_small["오일온도"].count()
# print(a - b)

# 실습 1번
# df_small = pd.read_csv("data/13_diecasting_small_24_261110_3.csv", sep=",", encoding="utf-8")
# print(df_small["형체력"])
# print(df_small[["형체력", "실린더압력"]].shape)
# print(df_small[["형체력"]])

# sorted = df_small.sort_values("형체력", ascending=False)
# print("정렬 후 인덱스 앞 4개:", sorted.index[:4].tolist())
# print("정렬 후 iloc[0] 샷:", int(sorted.iloc[0]["샷"]))
# print("정렬 후 loc[0] 샷:", int(sorted.loc[0, "샷"]))

# 실습 2번
df_small = pd.read_csv("data/13_diecasting_small_24_261110_3.csv", sep=",", encoding="utf-8")

# a = df_small["샷"]
# # print(a.loc[0])
# # print(a.iloc[0])

# b = df_small.sort_values("형체력", ascending=False) # 내림차순
# print(int(b.loc[0,"샷"]))
# print(int(b.iloc[0]["샷"]))

# # 실습 3번
# df_small = pd.read_csv("data/13_diecasting_small_24_261110_3.csv", sep=",", encoding="utf-8")
# print(df_small.columns.tolist())
# print(df_small.loc[0:4, ["실린더압력","형체력"]])
# print(df_small.iloc[0:5, [2,6]])

# 실습 4번
df_shot = pd.read_csv("data/13_diecasting_shot_24_261110_2.csv", sep=",", encoding="utf-8")
print(df_shot.shape)
print(df_shot.columns.tolist())
print(df_shot.loc[0:9, ["설비ID", "비스킷두께", "품질등급"]])
print(df_shot.iloc[-5:, [1,5,7]])
# 결국 loc,iloc는 "행"을 보여주기 위함
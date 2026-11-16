import numpy as np
import pandas as pd

# 실습 2번
# df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
# print(df_15.shape)
# print(df_15.head(3))
# print(df_15.info()) # 정보 제공
# print(df_15.describe()) # 값을 묘사

# 실습 3번
# df_15 = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8")
# print(df_15.isna().sum())
# NA_RULES = {"배럴온도":[999],"스크루속도":[-999]}
# updated = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8", na_values=NA_RULES)
# print(updated.isna().sum())
# NA_RULES["사출압력"] = [0]
# updated_1 = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8", na_values=NA_RULES)
# print(updated_1.isna().sum())

# 실습 4번
# df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
# count = df_15.isna().sum()
# count_1 = count[count > 0]
# a = count_1 / len(df_15)
# print(a, count_1)

# 실습 5번
# df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")

# a = df_15.isna().sum()
# b = len(df_15)
# isnot = (a / b) * 100
# print(isnot[isnot > 0].sort_values(ascending=False).head(3))

# row_missing = df_15.isna().sum(axis=1)
# print(row_missing[row_missing == 0].count())
# print(row_missing[row_missing > 0].count())
# print(row_missing[row_missing >= 5].count())

# 실습 6번
# df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")

# print(df_15[["최대사출속도","감압시간"]].isna().sum())
# print(df_15[["최대사출속도","감압시간"]].isna().head(10))
# both_na = (df_15["최대사출속도"].isna()) & (df_15["감압시간"].isna())
# print(both_na.sum())
# print(both_na.sum() / len(df_15) * 100)
# print(df_15.loc[both_na,["측정시각", "사출기"]])
# a = df_15[["최대사출속도","감압시간"]].isna().sum(axis=1)
# print((a==1).sum())
# print((a==2).sum())

# 실습 7번
df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")

sum_na = df_15.isna().sum()
print(sum_na[sum_na > 0])
sum_na = pd.DataFrame({"결측열" : sum_na})
print(sum_na)
print(sum_na.loc[ sum_na > 0, "결측열"])
# print(df_15.loc[:,])
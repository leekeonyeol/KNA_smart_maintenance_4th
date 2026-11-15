import pandas as pd

# 실습 2번
df_15 = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
print(df_15.shape)
print(df_15.head(3))
print(df_15.info())
print(df_15.describe())
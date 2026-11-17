import pandas as pd

df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv")
log_row = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv")

# 실습 1번
# print(df.shape)
# print(df.dropna().shape)
# print(df.dropna(axis=1).shape)

# 실습 2번
# print(df.dropna(how="all").shape)
# print(df.dropna(thresh=20).shape)
# print(df["불량여부"].isna().sum())
# print(df.dropna(subset=["불량여부","감압시간"],how="any"))

# 실습 3번
# feature_cols =  df.columns.tolist()
# print(feature_cols)

# a = df[feature_cols].isna().sum() / len(df) * 100
# print(a.round(1))

# b = a[a >= 40]
# print(b.index.tolist())
# c = b.index.tolist()

# d = df.drop(columns = c)
# print(d.shape)

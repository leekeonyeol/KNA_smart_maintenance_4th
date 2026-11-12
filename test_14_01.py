import pandas as pd 
import numpy as np

# 실습 1번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# print(df_comp["밸브상태"].value_counts())
# print(df_comp["밸브상태"].value_counts(normalize=True).round(2))

# 실습 2번
# df_comp = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")
# print(df_comp["검사결과"].value_counts())
# print(df_comp["검사결과"].value_counts(normalize=True).round(2))

# 실습 3번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# a = pd.cut(df_comp["진동"], bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"], right=True)
# print(a.value_counts())

# 실습 4번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# print(df_comp["냉각기상태"].value_counts())
# print(df_comp.groupby("냉각기상태")["온도"].mean().round(2))
# print(df_comp.groupby("냉각기상태")["온도"].max())
# print(df_comp.groupby("냉각기상태")["온도"].mean().round(2).loc["고장"] - df_comp.groupby("냉각기상태")["온도"].mean().round(2).loc["정상"])

# 실습 5번
df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
print(df_comp["밸브상태"].value_counts())
broken = df_comp[df_comp["result"] == "고장"]
print(broken["밸브상태"].value_counts())
print((broken["밸브상태"].value_counts() / df_comp["밸브상태"].value_counts()).round(3) )
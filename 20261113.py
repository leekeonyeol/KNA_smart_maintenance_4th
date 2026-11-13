import pandas as pd 
from pathlib import Path

# df_comp = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")
# df_comp_1 = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# 실습 1번
# print(df_comp["검사결과"].value_counts())
# print(df_comp.groupby("검사결과")["온도"].agg(["mean","std","max"]))
# print(df_comp.groupby("검사결과").agg(평균온도=("온도","mean"),
#                               평균냉각효율=("냉각효율","mean"),
#                               측정수=("검사결과","count")))

# 복습
# print(df_comp_1.groupby("냉각기상태")["온도"].transform("mean"))

# marked = df_comp_1.copy()
# marked["그룹평균"] = df_comp_1.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
# print(marked.groupby("냉각기상태")["편차"].sum().round(10))

# 복습
# temp_table = pd.pivot_table(df_comp_1, index="밸브상태", columns="운전부하", values="온도", margins=True, margins_name="전체")
# print(temp_table.round(2))

# 실습 2번
# marked = df_comp_1.copy()
# temp = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["그룹평균"] = temp

# marked["편차"] = marked["온도"] - marked["그룹평균"] # 편차 열

# print(marked[marked["편차"].abs() == marked["편차"].abs().max()])
# print(marked.loc[marked["편차"].abs().idxmax()])

# temp_table = pd.pivot_table(df_comp_1, index="밸브상태", columns="운전부하", values="온도", margins=True, margins_name="전체")
# print(temp_table)

# 복습
# print((df_comp_1["온도"].corr(df_comp_1["진동"])).round(3)) # 0.931 강한 양의 관계 즉, 선형적이다.
# valid = df_comp_1[["온도","냉각효율"]]

# 실습 3번
# print(round(df_comp_1["온도"].corr(df_comp_1["진동"]),3))
# print(round(df_comp_1["온도"].corr(df_comp_1["냉각효율"]),3))
# print(round(df_comp_1["온도"].corr(df_comp_1["압력"]),3))

# print(df_comp_1[["온도","냉각효율","진동","압력"]].corr())

# 실습 1번
# log = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8")
# print(log.shape)
# a = log.isna()
# print(a.sum())
# b = log["사출압력"] == 0
# c = log["스크루속도"] == -999
# d = log["배럴온도"] == 999
# print(b.sum(), c.sum(), d.sum())

# # 실습 2번
# operation = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8")

# 복습
log = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
sensor_cols = log.select_dtypes(include="number").columns.tolist()
# print(sensor_cols)

corr_matrix = log[sensor_cols].corr()

rows = []
for i in range(len(sensor_cols)) :
    for j in range(i + 1, len(sensor_cols)) :
        a = sensor_cols[i]
        b = sensor_cols[j]
        rows.append({"지표1" : a, "지표2" : b, "상관계수" : corr_matrix.loc[a,b]})

pair_table = pd.DataFrame(rows)
pair_table["절댓값"] = pair_table["상관계수"].abs()
print(pair_table)
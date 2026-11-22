import pandas as pd 
import numpy as np

# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# df_comp_1 = pd.read_csv("data/14_hydraulic_std_26_261112_3.csv", sep=",", encoding="utf-8")

# 실습 1번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# print(df_comp["밸브상태"].value_counts())
# print(df_comp["밸브상태"].value_counts(normalize=True).round(2))

# print(df_comp["밸브상태"].value_counts())
# print(df_comp["운전부하"].value_counts(normalize=True))

# 실습 2번
# df_comp = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")
# print(df_comp["검사결과"].value_counts())
# print(df_comp["검사결과"].value_counts(normalize=True).round(2))

# 실습 3번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# a = pd.cut(df_comp["진동"], bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"], right=True)
# print(a.value_counts())
# a = pd.cut(df_comp["진동"], bins=[0,0.6,0.7,10], labels=["약함","보통","강함"], right=True)
# print(a.value_counts())

# 실습 4번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# print(df_comp["냉각기상태"].value_counts())
# print(df_comp.groupby("냉각기상태")["온도"].mean().round(2))
# print(df_comp.groupby("냉각기상태")["온도"].max())
# print(df_comp.groupby("냉각기상태")["온도"].mean().round(2).loc["고장"] - df_comp.groupby("냉각기상태")["온도"].mean().round(2).loc["정상"])

# group = df_comp.groupby("냉각기상태")["온도"].mean().round(2)
# print(group)
# maxed = df_comp.groupby("냉각기상태")["온도"].max()
# print(maxed)
# print(group.loc["고장"] - group.loc["정상"])

# 실습 5번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# print(df_comp["밸브상태"].value_counts())
# broken = df_comp[df_comp["result"] == "고장"]
# print(broken["밸브상태"].value_counts())
# print((broken["밸브상태"].value_counts() / df_comp["밸브상태"].value_counts()).round(3) )


# 복습
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")

# sensor_cols = df_comp.select_dtypes(include="number").columns.tolist()
# corr_matrix = df_comp[sensor_cols].corr()
# rows = []

# for i in range(len(sensor_cols)) :
#     for j in range(i + 1, len(sensor_cols)) :
#         a = sensor_cols[i]
#         b = sensor_cols[j]
#         rows.append({"지표1": a, "지표2" : b, "상관계수" : corr_matrix.loc[a,b]})

# pair_table = pd.DataFrame(rows)
# pair_table["절댓값"] = pair_table["상관계수"].abs()
# print(pair_table)

# 실습 4번
# df_comp = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")
# sensor_cols = df_comp.select_dtypes(include="number").columns.tolist()
# corr_matrix = df_comp[sensor_cols].corr()
# rows = []

# for i in range(len(sensor_cols)) :
#     for j in range(i + 1, len(sensor_cols)) :
#         a = sensor_cols[i]
#         b = sensor_cols[j]
#         rows.append({"지표1" : a, "지표2" : b, "상관계수" : corr_matrix.loc[a,b]})

# pair_table = pd.DataFrame(rows)
# pair_table["절댓값"] = pair_table["상관계수"].abs()
# print(pair_table.shape)
# print((pair_table["절댓값"] >= 0.4).sum())
# print((pair_table["절댓값"] >= 0.95).sum())
# print(pair_table[pair_table["절댓값"] >= 0.95].head(5))

# 복습
# df_comp = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")
# print(df_comp.groupby("검사결과")["온도"].mean().round(2))
# print(df_comp.groupby("검사결과")["온도"].agg(["mean", "std", "max"]).round(2))
# print(df_comp.groupby("검사결과").agg(평균온도 = ("온도","mean"), 평균진동 = ("진동","mean")))

# 실습 5번
# df_comp = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
# df_comp_1 = pd.read_csv("data/14_hydraulic_std_26_261112_3.csv", sep=",", encoding="utf-8")

# merged = df_comp.merge(df_comp_1, on="냉각기상태", how="left")
# print(merged.shape)
# cutted = pd.cut(merged["온도"], bins=[0,40,50,200], labels=["낮음","보통","높음"], right=True)
# print(cutted.value_counts())
# total = merged.groupby("냉각기상태").agg(측정수=("온도","count"),평균온도=("온도","mean"),온도표준편차=("온도","std"),
#                             평균냉각효율=("냉각효율","mean"), 평균위험도=("위험도","mean"),
#                             평균점검주기=("권장점검주기","mean"))
# print(total)

df = pd.read_csv("data/14_hydraulic_26_261112_1.csv", sep=",", encoding="utf-8")
spec = pd.read_csv("data/14_hydraulic_std_26_261112_3.csv", sep=",", encoding="utf-8")
qc = pd.read_csv("data/14_hydraulic_qc_26_261112_2.csv", sep=",", encoding="utf-8")

# 문제 1번
# print(df_comp["밸브상태"].value_counts())

# 문제 2번
# print(df_comp["result"].value_counts())
# print(df_comp["result"].value_counts(normalize=True, dropna=False).round(3))

# 문제 3번
# cutted = pd.cut(df_comp["온도"], bins=[0, 40, 50, 200], labels=["낮음","보통","높음"], right=True)
# print(cutted.value_counts())
# print(cutted.isna().sum())

# 문제 4번
# print(df_comp.groupby("냉각기상태")["온도"].agg(["mean","max"]).round(2))

# 문제 5번
# print(df_comp["온도"].corr(df_comp["진동"]))
# print(df_comp[["온도","진동","압력","냉각효율"]].corr())

# 문제 6번
# summary = df_comp.groupby("냉각기상태").agg(평균온도=("온도","mean"),온도표준편차=("온도","std"))
# print(summary.loc["고장","평균온도"] - summary.loc["정상","평균온도"])

# 문제 7번
# a = pd.crosstab(df_comp["냉각기상태"],df_comp["운전부하"])
# print(a)
# b = pd.pivot_table(df_comp, index="냉각기상태", columns="운전부하", values="온도", aggfunc="mean", margins=True, margins_name="전체")
# print(b)
# print(a.loc["정상","저부하"])

# 문제 8번
# total = df_comp["밸브상태"].value_counts()
# print(total)
# fail = df_comp["밸브상태"][df_comp["result"] == "고장"]
# failed = fail.value_counts()
# print(failed)
# a = failed / total
# print(a.sort_values(ascending=False))
# top = a.sort_values(ascending=False).index[0]
# print(top)

# 문제 9번
# marked = df_comp.copy()

# group = marked.groupby("냉각기상태")["온도"].transform("mean")
# margin = marked["온도"] - group
# marked["그룹평균"] = group
# marked["편차"] = margin
# print(marked)

# print(marked.loc[marked["편차"].abs() == marked["편차"].abs().max(), ["냉각기상태","온도","그룹평균","편차"]])
# print(marked.groupby("냉각기상태")["편차"].sum())

# 문제 10번
# temp_table = pd.pivot_table(df_comp, index="밸브상태", columns="운전부하", values="온도", aggfunc="mean", margins=True, margins_name="전체")
# print(temp_table.shape)
# print(temp_table.loc["전체","전체"].round(2))

# 문제 11번
# print(qc["검사결과"].value_counts())
# print(qc["검사결과"].value_counts(normalize=True))

# sensor_cols = qc.select_dtypes(include="number").columns.tolist()
# cor_matrix = qc[sensor_cols].corr()
# rows = []

# for i in range(len(sensor_cols)) :
#     for j in range(i+1, len(sensor_cols)) :
#         a = sensor_cols[i]
#         b = sensor_cols[j]
#         rows.append({"지표1" : a, "지표2" : b, "상관계수" : cor_matrix.loc[a,b]})

# pair_table = pd.DataFrame(rows)
# pair_table["절댓값"] = pair_table["상관계수"].abs()

# 문제 1번
# print(df["밸브상태"].value_counts())

# 문제 2번
# print(df["result"].value_counts(normalize=True).round(3))

# 문제 3번
# cutted = pd.cut(df["온도"], bins=[0,40,50,200], labels=["낮음","보통","높음"], right=True)
# print(cutted.value_counts())
# print(cutted.isna().sum())
# cutted = pd.cut(df["온도"], bins=[0,20,30,40], label = ["낮음","보통","높음"], right=True)

# 문제 4번
# print(df.groupby("냉각기상태")["온도"].agg(["mean","max"]).round(2))

# 문제 5번
# print(df[["온도","진동","압력","냉각효율"]].corr().round(3))

# 문제 6번
# summary = df.groupby("냉각기상태").agg(평균온도=("온도","mean"), 온도표준편차=("온도","std"),
#                                   평균진동=("진동","mean"))
# print(summary.round(3))
# print(summary.loc["고장","평균온도"] - summary.loc["정상","평균온도"])

# 1 = df.groupby("냉각기상태")["온도"].agg(["mean","max"])
# 2 = df.groupby("냉각기상태").agg(평균온도 = ("온도","mean"), 평균진동 = ("진동","mean"))

# 문제 7번
# ct = pd.crosstab(df["냉각기상태"], df["운전부하"]) # 크로스탭은 사이클수 
# print(ct)
# mean_table = df.groupby(["냉각기상태","운전부하"])["온도"].mean().unstack() # 언스택은 어떤 인덱스를 열로 올릴지 결정
# print(mean_table.round(3))
# mean_table = df.groupby(["냉각기상태","운전부하"])["온도"].mean().unstsck()

# 문제 8번
# total = df["밸브상태"].value_counts()
# fail = pd.crosstab(df["밸브상태"], df["result"])
# normalize = fail["고장"] / total
# rate = normalize.sort_values(ascending=False)
# print(rate.index[0]) # 행의 첫번째 값

# 문제 9번
# marked = df.copy()

# temp_average = df.groupby("냉각기상태")["온도"].transform("mean")
# marked["그룹평균"] = temp_average
# marked["편차"] = marked["온도"] - marked["그룹평균"]

# print(marked[marked["편차"].abs() == marked["편차"].abs().max()][["냉각기상태","온도"]])
# print(marked.groupby("냉각기상태")["편차"].sum())

# 문제 10번
# temp_table = df.groupby(["밸브상태","운전부하"])["온도"].mean().unstack()
# print(temp_table)
# temp_table_1 = pd.pivot_table(df, index="밸브상태", columns="운전부하",
#                               values="온도", aggfunc="mean", margins=True,
#                               margins_name="전체")
# print(temp_table_1) # 결국 전체를 알기 위해 groupby.unstack이 아니라 pivot_table을 사용

# 문제 11번
# sensor_cols = qc.select_dtypes(include="number").columns.tolist()
# corr_matrix = qc[sensor_cols].corr()
# rows = []

# for i in range(len(sensor_cols)) :
#     for j in range(i+1, len(sensor_cols)) :
#         a = sensor_cols[i]
#         b = sensor_cols[j]
#         rows.append({"지표1" : a, "지표2" : b, "상관계수" : corr_matrix.loc[a,b]})

# pair_table = pd.DataFrame(rows)
# print(pair_table)
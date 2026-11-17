import numpy as np
import pandas as pd

df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
log = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8")

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

# df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", sep=",", encoding="utf-8")
# log = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", sep=",", encoding="utf-8")

# 문제 1번
# print(df.shape)
# print(int(df.isna().sum().sum())) # 행들을 전부 합침
# print(df.isna().sum(axis=1)>0) # 열들을 전부 합침

# 실습 4번
# print(df.shape)
# print(df.dropna().shape)
# print(df.dropna(thresh=20).shape)



# comparison_rows=[]

# for name, frame in version.items() :
#     comparison.append({"방식" : name, "행수" : len(frame),
#                        "손실율" : (1-len(frame)) / len(df),
#                        "불량수" : int(frame["불량여부"].sum())})

# comparison = pd.dataframe(comparison_rows)

# 실습 5번
# copied = df.copy()

# mask = copied["최대사출압"].isna()
# print(mask.sum())

# mean_val = copied["최대사출압"].mean()
# median_val = copied["최대사출압"].median()

# filled_mean = copied["최대사출압"].fillna(mean_val)
# filled_median = copied["최대사출압"].fillna(median_val)

# print(filled_mean.isna().sum())
# print(filled_median.isna().sum())

# print(filled_mean.loc[mask].head(3))
# print(filled_median.loc[mask].head(3))

# 실습 6번
# NA_RULES = {"배럴온도":[999],"스크루속도":[-999],"사출압력":[0]}

# df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv", na_values=NA_RULES, parse_dates=["시간"])

# unknown = df[df["설비"].isna()].copy()
# rest = df[df["설비"].notna()].sort_values(["설비","시간"]).reset_index(drop=True)

# g = rest.groupby("설비")
# filled = g["온도"].ffill(limit=1)


# 실습 7번
# df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv")

# print(df[df["스크루속도"].isna()].index.tolist())
# print(df.groupby("사출기")["스크루속도"].count()) # 유효한 행만 센다

# df["그룹평균"] = df.groupby("사출기")["스크루속도"].transform("mean")

# valid_cnt = df.groupby("사출기")["스크루속도"].transform("count")
# fill_mask = df["스크루속도"].isna() & (valid_cnt >= 3)

# df.loc[fill_mask,"스크루속도"] = df.loc[fill_mask,"그룹평균"]

# print(fill_mask[fill_mask].index.tolist())
# print(df["스크루속도"].isna().sum())

# 실습 7번
# df = pd.read_csv("data/15_사출성형_공정_28_261113_1.csv")

# print(df[df["스크루속도"].isna()].index.tolist())
# print(df.groupby("사출기")["스크루속도"].count())

# df["그룹평균"] = df.groupby("사출기")["스크루속도"].transform("mean")

# valid_cnt = df.groupby("사출기")["스크루속도"].transform("count")
# fill_mask = df["스크루속도"].isna() & (valid_cnt >= 3)

# df.loc[fill_mask,"스크루속도"] = df.loc[fill_mask,"그룹평균"]

# print(fill_mask[fill_mask].index.tolist())
# print(df["스크루속도"].isna().sum())

# 문제 1번
# print(df.shape)
# print(df.isna().sum().sum())
# print((df.isna().sum()>0).sum()) 

# 문제 2번
# count = df.isna().sum()
# print(count)
# mean = df.isna().mean()
# ratio =round(mean*100,2)
# print(ratio[ratio > 0])

# 문제 3번
# count = df.isna().sum(axis=1)

# print((count == 0).sum())
# print((count > 0).sum())
# print((count >= 5).sum())

# 문제 4번
# print(df.shape)
# print(df.dropna().shape)
# print(df.dropna(axis=1).shape)
# print(df.dropna(how="all").shape)
# print(df.dropna(thresh=20).shape)

# 문제 5번
# example = pd.Series([1, 2, 3, 4, 100, None])

# print(example.mean())
# print(example.median())

# a = example.fillna(example.median())
# print(a.tolist())
# b = example.fillna(example.mean())
# print(b.tolist())

# 문제 6번
# series_demo = pd.Series([None, 73.0, None, None, 75.0])
# a = series_demo.ffill()
# print(a)
# b = series_demo.bfill()
# print(b)
# c = series_demo.ffill(limit=1)
# print(c)

# 문제 7번
# text = pd.Series(['1호기', ' ', '', None], dtype='string')

# print(text.isna().sum())
# replaced = text.str.strip().replace(" ","pd.NA")
# print(replaced.isna().sum())

# 문제 8번
# log = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv")
# print(log.isna().sum().sum())
# log_1 = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", na_values={"배럴온도" : [999], "스크루속도" : [-999]})
# print(log_1)
# NA_RULES = {"배럴온도" : [999], "스크루속도" : [-999], "사출압력" : [0]}
# log_2 = pd.read_csv("data/15_사출성형_로그_28_261113_2.csv", na_values=NA_RULES)
# print(log_2)

# 문제 9번
# feature_cols = df.columns.tolist()
# isna_count = df[feature_cols].isna().mean() * 100
# isna_list = isna_count[isna_count > 40].index.tolist()
# result = df.drop(columns= isna_list)
# print(result.shape)
# print(result.columns.tolist())

# 문제 10번
# a = df
# b = df.dropna()
# c = df.dropna(thresh=20)
# rows = []

# cases = { "원본" : a, "기본 행 제거" : b, "thresh20" : c}

# for name, d in cases.items() :
#     rows.append({"방식" : name, "행수" : len(d), 
#                  "손실률" : 1 - len(d)/len(df),
#                   "불량 수" : d["불량여부"].sum(),
#                    "불량비율" : d["불량여부"].mean()})

# summart = pd.DataFrame(rows)
# print(summart)

# 문제 11번
# work =df.copy()

# mask = work[work["최대사출압"].isna()].index.tolist()

# mean_val = work["최대사출압"].mean()
# median_val = work["최대사출압"].median()

# work.loc[work["최대사출압"].isna(),"최대사출압"] = mean_val
# filled = work["최대사출압"].fillna(mean_val)
# print(filled)

# 문제 11번
# work = df.copy()

# mean_val = work["최대사출압"].mean()
# median_val = work["최대사출압"].median()

# filled = work["최대사출압"].fillna(mean_val)

# print(work["최대사출압"])
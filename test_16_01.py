import pandas as pd

# masked = df["temp"].mask(mask) # 이상치에 대해서 Nan을 매긴다
# print(masked.isna().sum())
# med = masked.median()
# fixed = masked.fillna(med)
# print(fixed.mean())

# print(df.duplicated())
# print(df[df.duplicated()])

# df_unique = df.drop_duplicates(keep="last")
# df_u = df.drop_duplicates(subset = ["machine_id","cycle"], keep = "last").reset_index(drop=True)

import pandas as pd
import numpy as np

F = "data/12_metro_compressor_22_261109_1.csv"
FS = "data/12_metro_compressor_semicolon_22_261109_2.csv"
FD = "data/12_metro_digital_22_261109_3.csv"

# 문제 1번
df_comp = pd.read_csv(F, sep=",", encoding="utf-8") # 한글을 읽기 때문에 encoding
# print(fd_comp.head(5))
# print(fd_comp.tail(3))
# print(fd_comp.index[-1]) # index는 위치번호를 반환

# 문제 2번
# print(df_comp.shape)
# print(df_comp.columns.tolist())
# print(len(df_comp.index))
# print(df_comp.dtypes)

# 문제 3번
np_comp = np.genfromtxt(F, delimiter=",", skip_header=1) # 문자열 처리 x, 따라서 pd가 필요
oil = df_comp["오일온도"].values
print(type(oil))
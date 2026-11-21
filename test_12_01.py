import pandas as pd
import numpy as np

F = "data/12_metro_compressor_22_261109_1.csv"
FS = "data/12_metro_compressor_semicolon_22_261109_2.csv"
FD = "data/12_metro_digital_22_261109_3.csv"

# 문제 1번
# df_comp = pd.read_csv(F, sep=",", encoding="utf-8") # 한글을 읽기 때문에 encoding
# print(fd_comp.head(5))
# print(fd_comp.tail(3))
# print(fd_comp.index[-1]) # index는 위치번호를 반환

# 문제 2번
# print(df_comp.shape)
# print(df_comp.columns.tolist())
# print(len(df_comp.index))
# print(df_comp.dtypes)

# 문제 3번
# np_comp = np.genfromtxt(F, delimiter=",", skip_header=1) # 문자열 처리 x, 따라서 pd가 필요
# oil = df_comp["오일온도"].values
# print(type(oil))

# 문제 1번
# temp = np.array([70.1, np.nan, 71.2, 70.8, np.nan])

# print(np.isnan(temp).mean())
# print(np.nanmean(temp))

# 문제 2번
# vib = np.array([1.8, 2.0, 2.1, 2.3, 2.4, 2.6, 2.7, 7.9])

# q1 = np.percentile(vib,25)
# q3 = np.percentile(vib,75)
# iqr = q3 - q1

# upper = q3 + 1.5 * iqr
# print(vib[vib > upper])

# 문제 3번
# x = np.array([10, 12, 11, 13, 12, 30])
# z = ( x - np.mean(x)) / np.std(x)
# print(z[np.abs(z) > 2])

# 문제 4번
# a = np.array([1, 2, 3, 4, 5]) 
# b = np.array([10, 8, 6, 4, 2])

# print(np.corrcoef(a,b)[0,1])

# 문제 5번
# data = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.mean(data, axis = 1))
# print(np.mean(data, axis = 0))

# 문제 6번
# vib = np.array([2.0, 2.2, 2.1, 2.0, 6.0, 6.2, 6.1])

# mean = np.mean(vib)
# minus = vib - mean
# cumsum = minus.cumsum()
# print(cumsum.argmin()) # 최솟값의 위치 인덱스

# 문제 7번
# ct = np.array([21, 22, 21, 23, 95, 24])
# result = np.abs(np.diff(ct))
# print(result.argmax()) # 가장 큰 값의 인덱스
# print(result[3])

# 문제 8번
# vib = np.array([2.1, 6.1, 2.0, 5.8, 3.3])
# a = np.argsort(vib) # 정렬을 하되 인덱스로 나타남
# print(a[-3:])

# 문제 9번
# pres = np.array([4.5, 9999.0, 4.6, -1.0, 5.1])
# a = np.clip(pres, 0, 10)
# print(round(a.mean(),3))

# 문제 10번
# vib = np.array([2.1, 3.5, 2.0, 6.2, 5.0, 3.0])

# a = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))
# print(a)

# c, d = np.unique(a, return_counts = True)
# print(c,d)

# 문제 11번
# am = np.array([2.0, 2.1, 2.2])
# pm = np.array([2.3, 2.4, 6.5])

# a = np.concatenate([am,pm])

# print(np.any(a > 5))
# print(np.all(a < 10))

# b = np.stack([am,pm])

# print(b)

# 문제 12번
# t = np.array([35.2, 35.4, np.nan, 35.3, 35.6,
#               35.5, 35.4, 35.7, 35.6, 58.1])

# print(np.isnan(t).sum() / len(t))
# print(round(np.nanmean(t),3))

# q1 = np.nanpercentile(t,25)
# q3 = np.nanpercentile(t,75)
# upper = q3 + 1.5 * (q3 - q1)

# print(t[t > upper])

# z = ( t - np.nanmean(t)) / np.nanstd(t)

# print(np.nanmax(z))

# 문제 12번
# data = np.array([[35., 36., 35., 58.],
#                  [47., 46., 48., 19.]])

# a = np.mean(data, axis=1, keepdims=True) # 차원을 유지
# b = np.std(data, axis=1, keepdims=True)

# z = (data - a) / b
# print(np.abs(z))

# c = np.sum(z, axis=0)
# print(np.argmax(c) + 1) # 가장 큰 값의 인덱스 arg~

# d = np.corrcoef(data[0,:], data[1,:])[0,1]
# print(d)

# 문제 14번
# shot = np.arange(1, 11)
# ct  = np.array([21, 22, 20, 36, 652, 23, 91, 1885, 24, 6170])
# cyl = np.array([214, 215, 108, 216, 265, 214, 217, 264, 215, 109])

# print(np.argmax(ct))
# print(ct[9])

# diff = np.abs(np.diff(ct))
# print(np.argmax(diff))

# print(np.sum((ct >= 50) | (cyl < 150)) / len(ct)) 

# print(np.argsort(ct)[::-1][:3])

# where = np.where(ct < 50, 0, np.where((ct > 50) & (ct < 1000), 1, 2))
# a, b = np.unique(where, return_counts=True)
# print(b / len(where))
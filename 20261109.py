import numpy as np

# 실습 4번
# data = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=(0,1))
# cycle = data[:,0]
# temp = data[:,1]

# a = np.mean(temp)
# b = np.std(temp)
# print(a,round(b,1))

# upper = a + 3*b
# print(round(upper,2))
# print(cycle[temp > upper])

# # 실습 5번
# data = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=(1,3))
# temp = data[:,0]
# effi = data[:,1]

# print(round(float(np.corrcoef(temp,effi)[0,1]),3))
# # 온도가 증가하면 거의 1:1 음의 비례관계로 효율이 떨어짐

# # 실습 6번
# temp = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=1)
# vib = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=2)
# effi = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=3)
# power = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=4)

# data = np.stack([temp, vib, effi, power])
# print(np.round(np.nanmean(data, axis=1),2))
# print(np.round(np.nanstd(data, axis=1),2))

# 실습 7번
# data = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=(0,1))
# cycle = data[:,0]
# temp = data[:,1]

# a = np.mean(temp)
# print(a)
# b = np.cumsum(temp - a)
# print(b)
# print(np.argmin(b))
# print(cycle[np.argmin(b)])

# # 실습 8번
# cycle = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=0)
# temp = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=1)
# effi = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=3)
# stats = np.genfromtxt("data/11_hydraulic_cooler_20_261105_2.csv", delimiter=",", skip_header=1, usecols=5)

# a = np.stack([temp, effi])
# def z_score (b) :
#     mean = np.nanmean(b, axis = 1, keepdims=True)
#     std  = np.nanstd(b, axis = 1, keepdims=True)
#     result = np.abs((b - mean) / std)
#     return result

# c = np.sum(z_score(a), axis=0 )
# print(cycle[np.argmax(c)], round(c[np.argmax(c)],2))
# d = np.argsort(c)
# print(cycle[d[-3:]])

import pandas as pd
# oil = pd.read_csv("data/12_metro_compressor_22_261109_1.csv")["오일온도"]
# print(oil)

# 실습 1번
# df_comp = pd.read_csv("data/12_metro_compressor_22_261109_1.csv")
# print(df_comp.head(5))
# print(df_comp.shape)
# print(df_comp.describe())

# 실습 2번
# df_comp = pd.read_csv("data/12_metro_compressor_22_261109_1.csv", sep=",", encoding="utf-8", usecols=["측정시각","오일온도","모터전류"], nrows = 20)
# print(df_comp)

# 실습 3번
# df_comp = pd.read_csv("data/12_metro_compressor_semicolon_22_261109_2.csv")
# df_comp_1 = pd.read_csv("data/12_metro_compressor_semicolon_22_261109_2.csv", sep=";", encoding="utf-8")
# print(df_comp)
# print(df_comp_1)

# 실습 4번
df_comp = pd.read_csv("data/12_metro_compressor_semicolon_22_261109_2.csv", sep=";", encoding="utf-8", usecols=["측정시각","오일온도","모터전류"], nrows=50)
print(df_comp)
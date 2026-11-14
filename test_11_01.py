import numpy as np

# 실습 1번 
# data = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=(0,1))
# time = data[:,0]
# cycle = data[:,1]
# print(np.argmax(cycle))
# print(time[np.argmax(cycle)])
# print(cycle[np.argmax(cycle)])

# # 실습 2번
# data = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=(0,1))
# time = data[:,0]
# cycle = data[:,1]
# print(np.diff(cycle))
# print(np.abs(np.diff(cycle)))
# a = np.abs(np.diff(cycle))
# print(np.argmax(a))
# b = np.argmax(a)
# print(cycle[b], cycle[b+1])))

# 실습 3번
# cyl = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=2)
# cyl[0] = 9999
# print(cyl)
# print(np.mean(cyl))
# fixed = np.clip(cyl, 100, 300)
# print(np.mean(fixed))

# 실습 4번
# cyl = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=1)
# a = np.where(cyl>1000, 2, np.where((cyl >= 50) & (cyl < 1000),1,0))
# kind, counts = np.unique(a, return_counts=True)
# print(kind)
# print(counts)

# 실습 5번
# time = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=1)
# pres = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=2)
# make = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=3)
# shap = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=4)

# a = np.stack([time, pres, make, shap])
# print(a.shape)
# b = a[:,-10:]
# print(b)
# print(b.shape)

# # 실습 6번
# data = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter = ",", skip_header = 1, usecols =  (0, 1, 2))

# time = data[:,0]
# cycle = data[:,1]
# pressure = data[:,2]

# a = np.argmax(cycle)
# print(a)
# b = cycle[a]
# print(b)

# c = np.abs(np.diff(cycle))
# d = np.argmax(c)
# print(d)

# e = (cycle > 50) | (pressure < 150) 
# print(e.sum() / len(e) * 100)

# f = np.argsort(cycle)
# print(f[-3:])

# 문제 1번
# temp = np.array([70.1, np.nan, 71.2, 70.8, np.nan])
# print(np.isnan(temp))
# print(np.isnan(temp).sum() / len(temp))
# print(np.mean(temp))
# print(np.nanmean(temp))

# 문제 2번
# vib = np.array([1.8, 2.0, 2.1, 2.3, 2.4, 2.6, 2.7, 7.9])
# q1 = np.percentile(vib,25)
# q3 = np.percentile(vib,75)
# iqr = q3 - q1 
# print(iqr)
# upper = q3 + 1.5*iqr
# print(vib[vib > upper])

# # 문제 3번
# x = np.array([10, 12, 11, 13, 12, 30])
# z = (x - np.mean(x)) / np.std(x)
# print(z[np.abs(z) > 2])
# print(x[x > np.mean(x) + 3*np.std(x)])

# # 문제 4번
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([10, 8, 6, 4, 2])
# print(np.corrcoef(a,b)[0,1]) # ***

# 문제 5번
# data = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.mean(data, axis=1))
# print(np.mean(data, axis=0))

# 문제 6번
# vib = np.array([2.0, 2.2, 2.1, 2.0, 6.0, 6.2, 6.1])
# a = vib - np.mean(vib)
# print(np.cumsum(a))
# b = np.cumsum(a)
# print(np.argmin(b)) # 4번째 값에서 갑자기 튄다.

# 문제 7번
# ct = np.array([21, 22, 21, 23, 95, 24])
# a = np.abs(np.diff(ct))
# print(np.argmax(a))
# print(a[3])

# 문제 8번
# vib = np.array([2.1, 6.1, 2.0, 5.8, 3.3])
# print(np.argsort(vib))
# print(np.argsort(vib)[::-1][:3]) # ***

# 문제 9번
# pres = np.array([4.5, 9999.0, 4.6, -1.0, 5.1])
# a = np.clip(pres, 0, 10)
# print(np.mean(pres))
# print(np.mean(a))

# 문제 10번
# vib = np.array([2.1, 3.5, 2.0, 6.2, 5.0, 3.0])
# a = np.where((vib >= 5), 2, np.where(vib >= 3, 1, 0))
# c, d = np.unique(a, return_counts=True) # ***
# print(c)
# print(d)

# 문제 11번
# am = np.array([2.0, 2.1, 2.2])
# pm = np.array([2.3, 2.4, 6.5])
# a = np.any(np.concatenate([am, pm]) > 5)
# print(a)
# b = np.all(np.concatenate([am, pm]) < 10)
# print(b)
# print(np.stack([am,pm]))

# 문제 12번
# t = np.array([35.2, 35.4, np.nan, 35.3, 35.6, 35.5, 35.4, 35.7, 35.6, 58.1])
# print(np.isnan(t).sum())
# print(np.isnan(t).sum() / len(t))
# print(np.nanmean(t))
# print(np.nanpercentile(t,[25,75]))
# q1, q3 = np.nanpercentile(t,[25,75])
# iqr = np.diff(np.nanpercentile(t,[25,75]))
# upper = q3 + 1.5*iqr
# print(upper)
# print(t[t > upper])
# z = (t - np.nanmean(t)) / np.nanstd(t)
# print(float(np.nanmax(z)))

# 문제 13번
# data = np.array([[35., 36., 35., 58.],
#                  [47., 46., 48., 19.]])
# m = np.mean(data, axis=1, keepdims=True)
# s = np.std(data, axis=1, keepdims=True)
# z = np.abs((data - m) / s)
# t = np.sum(z, axis=0)
# q = np.argmax(t) + 1
# e = np.corrcoef(data[0,:], data[1,:])[0,1]

# 문제 14번
shot = np.arange(1, 11)
ct = np.array([21, 22, 20, 36, 652, 23, 91, 1885, 24, 6170])
cyl = np.array([214, 215, 108, 216, 265, 214, 217, 264, 215, 109])

print(ct.argmax())
print(ct[ct.argmax()])

print(np.abs(np.diff(ct)).argmax())

print((ct >= 50) | (cyl < 150))
a = (ct >= 50) | (cyl < 150)
print(a.sum() / len(ct))

print(np.argsort(ct)[::-1][:3])

b = np.where((ct < 50), 0, np.where((ct > 50) & (ct < 1000),1 ,2))
kinds, counts = np.unique(b, return_counts=True)
print(counts / len(ct))
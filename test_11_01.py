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
# print(cycle[b], cycle[b+1])

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
time = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=1)
pres = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=2)
make = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=3)
shap = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter=",", skip_header=1, usecols=4)

a = np.stack([time, pres, make, shap])
print(a.shape)
b = a[:,-10:]
print(b)
print(b.shape)

# 실습 6번
data = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter = ",", skip_header = 1, usecols =  (0, 1, 2))

time = data[:,0]
cycle = data[:,1]
pressure = data[:,2]

a = np.argmax(cycle)
print(a)
b = cycle[a]
print(b)

c = np.abs(np.diff(cycle))
d = np.argmax(c)
print(d)

e = (cycle > 50) | (pressure < 150) 
print(e.sum() / len(e) * 100)

f = np.argsort(cycle)
print(f[-3:])
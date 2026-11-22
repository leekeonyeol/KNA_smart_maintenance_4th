import numpy as np

# # 문제 1번
# a = np.array([4603, 4967, 4987, 3632, 58, 1216])
# b = np.array([[4603, 2], [58, 5], [1216, 1]])

# print(a.ndim, b.ndim)
# print(a.shape, b.shape)
# print(a.size, b.size)
# print(a.dtype, b.dtype)

# # 문제 2번
# temp = np.arange(0,50,10)
# print(temp)
# temp = np.linspace(0,1,5)
# print(temp)
# temp = np.zeros(3)
# print(temp)
# temp = np.full(3,7)
# print(temp)

# # 문제 3번
# cur = np.array([18.69, 25.4, 30.99])
# print(cur.dtype)
# cur_int = cur.astype(int)
# print(cur_int)

# # 문제 4번
# temp = np.array([70, 72, 71, 95, 73, 68])
# data = np.array([[4603, 2], [58, 5], [1216, 1], [4967, 3]])

# print(temp[0], temp[-1])
# print(temp[1:4])
# print(temp[::2])
# print(data[:,0])
# print(data[1,1])

# # 문제 5번
# vals = np.array([70, 95, 71, 88, 73])
# a = vals > 85 # 한꺼번에 처리 
# print(a)
# b = vals[vals > 85]
# print(b)
# c = np.where(vals > 85, 1, 0)
# print(c)
# d = vals[(vals > 70) & (vals < 90)]
# print(d)

# # 문제 6번
# s = np.array([60, 85, 65, 95, 70])
# print(s.mean(), np.median(s), s.max(), s.min())
# print(round(s.std(),2))

# # 문제 7번
# rpm = np.array([4500, 3000, 1500, 4800, 600])
# a = rpm - rpm.min()
# b = rpm.max() - rpm.min()
# print(np.round(a/b, 2))

# # 문제 8번
# flat = np.array([30, 20, 4600, 31, 25, 4500, 29, 22, 1200, 30, 28, 4700])
# data = flat.reshape(4,3)

# print(data.mean(axis = 0)) # 배열의 목적은 ***분산된 값을 한번에 처리***
# a = data.mean(axis = 0)
# print(np.round(a,1))
# data_1 = data[:,2]
# data_2 = data_1 < 2000
# print(data_2.sum(), data_2.mean() * 100) # true의 총 개수

# 문제 9번
# vals = np.array([[4603, 40], [4967, 25], [4987, 20], [3632, 40], [58, 25],
#                   [1216, 40], [1217, 20], [1241, 40], [3143, 20]])
# a = vals[:,0]
# b = vals[:,1]

# data = a < 2000
# print(data.sum(), round((data.mean() * 100), 2))
# data_1 = b[data]
# print(data_1.mean())
# print(np.where(data, 1, 0))
# print(round(a[a > 2000].mean(),1))
# print(round(a.mean(), 1))

# 문제 10번
# ct = np.array([15800, 15750, 15820, 15790, 21207, 15810, 15770, 15830])

# print(ct.mean(), ct.std())
# a = ct - ct.mean()
# b = a > ct.std()
# print(b)
# print(ct[b], np.arange(1, ct.size + 1)[b]) # TRUE 해당하는 값만 추출
# print(round(ct[~b].mean(),1))
# print(np.median(ct))

# 문제 11번
# table = np.array([[72, 2.3], [95, 6.8], [70, 2.0], [71, 2.4]])
# base = np.array([70, 2.0])

# a = table - base
# print(np.round(a,1))
# print(a[:,0] > 5)
# b = a[:,0] > 5
# print(np.arange(1, 5)[b]) # TRUE값에 해당하는 인덱스(위치)
# print(np.round(table.mean(axis = 0),2))
# print(np.round(table.std(axis = 0),2))

# 문제 12번
# data = np.genfromtxt("data/10_mct_tool_18_261104.csv", delimiter=",", skip_header=1, usecols=4)

# print(data.shape)
# print(data.dtype)
# print(data.mean(), round(data.std(),1), data.max(), data.min())
# a = data < 2000
# print(a.sum())
# print(np.mean(data[a]))
# print(np.arange(1, data.size + 1)[a])
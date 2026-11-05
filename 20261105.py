#  실습 3번
import numpy as np
# a = np.array([[4603], [4967], [4987], [3632], [58], [1216], [1217], [1241], [3143]])
# b = a.max()
# c = a.min()
# print(a - c)
# d = b -c
# e = (a-c)/d
# print(np.round(e,2))

# # 실습 4번
# vals = np.array([[4603, 40], [4967,25], [4987,20], [3632,40], [58,25], [1216,40], [1217,20], [1241,40], [3143,20]])
 
# cond1 = vals[:,0] > 2000
# print(cond1)

# cond2 = (vals[:,0] > 2000) | (vals[:,1] > 25)
# print(cond2)

# print(cond1.sum()) # 만족하는 시점 개수
# print(cond2.sum())

# print((cond1.sum() / len(vals[:,0])) * 100)
# print((cond2.sum() / len(vals[:,0])) * 100)

# # 실습 5번
# data = np.array([2, 21, 3, 147, 5, 146, 91, 10, 11, 12])

# cond3 = data > 10
# print(cond3)

# print(len(data))
# print(cond3.sum())
# print((cond3.sum() / len(data)) * 100)

# # 실습 6번
# import csv 

# with open ("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f :
#     reader = csv.reader(f)
#     next(reader)
#     data = list(reader)

# a = np.array(data)
# b = a[:,3:5].astype(float) 
# print(np.round(b.mean(axis=0),1))
# print(np.round(b.std(axis=0),1))

# np.로만 되는 경우: 배열을 만들때 ***
# 배열.로만 쓰는 경우: 그 배열 자신에 대한 것 ***

# 실습 7번
# rpm = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter = ",", skiprows = 1, usecols = 4)
# print(np.round(rpm.mean(),1))
# print(np.round(rpm.std(),1))
# print(rpm.max(), rpm.min())

# # 실습 8번
# torque = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter = ",", skiprows = 1, usecols = 5 )
# print(torque[ torque > 10])
# print(round(np.mean(torque[ torque > 10]),1))

# # 실습 9번
# total = np.loadtxt("data/10_mct_tool_18_261104.csv", delimiter = ",", skiprows = 1, usecols=(4,5) )
# print(total.shape)
# print(total.dtype)
# a = total[:,0] < 2000
# a_1 = total[:,0]
# b = total[a]
# print(np.sum(b) / len(b))
# print(np.sum(a_1) / len(a_1))

# 실습 1번
data = np.genfromtxt("data/11_diecasting_series_20_261105_1.csv", delimiter = ",", skip_header = 1,usecols = (0,1))
shot = data[:,0]
cycle = data[:,1]

a = np.argmax(cycle) # 가장 큰 값의 위치
print(a) 
b = shot[a] # 가장 큰 값의 시점
print(b)
c = cycle[a] # 가장 큰 값을 도출
print(c)

# 실습 2번
d = np.diff(cycle)
print(d)
e = np.abs(d)
print(e)
f = np.argmax(e)
print(f)
print(cycle[f], cycle[f+1])



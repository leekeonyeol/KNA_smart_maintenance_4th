# 리스트
# 서로 다른 자료형 같이 존재 가능
# 계산이 느리고 반복문을 돌아야한다
# print( [v*2 for v in list] )

# 배열
# 계산이 빠르고 반복문을 돌 필요가 없다
# 서로 다른 자료형 같이 존재 불가능
 
# 튜플로 배열 만들기
# print(np.array((1, 2, 3)))

import numpy as np 

# # 실습 1번
# temp = np.array([20.5, 70.3, 83.4]) # 배열
# print(temp)
# temp_1 = temp*1.8 + 32 # 한 줄로 처리 가능
# print(temp_1) 

# # 실습 2번
# temp = np.linspace(0,70,8)
# print(temp)

# # 실습 3번
# temp = np.arange(0,40,5)
# print(temp)

# # 실습 4번
# temp =np.array([[1.2, 2.3, 4.5],[3.2, 3.4, 4.1]])
# print(temp.ndim)
# print(temp.shape)
# print(temp.size)

# # 실습 5번
# print(temp.dtype)
# temp_1 = temp.astype(int)
# print(temp_1)

# # 실습 6번 ,7번
# a = np.arange(12)
# print(a)
# b = a.reshape(3,4)
# print(b)
# c = b.flatten()
# print(c)

# 실습 1번
import csv
with open ("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f :
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

a = np.array(data)
print(a[0],a[39])
print(a[1:4])
print(a[::2])

# 실습 2번
print(a[:,4],a[:,5])
print(a[2])
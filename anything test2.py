# a = [12, 24, 999, 31]
# a.remove(999) # 값을 기준으로 빼기만 하는 메서드
# print(a)
# b = a.pop(1) # 빼준 값을 반환하는 메서드
# print(b)
# del a[0] # 위치를 기준으로 빼기만 하는 메서드 
# print(a)

# # append(붙일 값) 
# # insert(위치, 주입값)  받는 함수는 필요업다
# # extend(붙일 리스트) 

# # 누적 변수 패턴 (합계, 갯수, 패턴)
# total = 0
# for i in range(1,6):
#     total += i
# print("합계:",total)

# count= 0 #초기화
# for i in range(1,11) :
#     if i>5 :
#         count += 1
# print(count)

# # 평균
# temps = [25, 26, 24]
# for idx, t in enumerate(temps) :
#     print(idx +1, "번째:", t)

count = 1
while count <= 3:
    print(count)
    count = count + 1

# 문제 1번 04_02, 05_01
pres = float(input("압력:"))
if pres > 5.0 :
    print("경고")
else :
    print("정상")    

# 문제 2번




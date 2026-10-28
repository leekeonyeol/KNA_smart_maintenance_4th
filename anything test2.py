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

# count = 1
# while count <= 3:
#     print(count)
#     count = count + 1

# # 문제 1번 04_02, 05_01
# pres = float(input("압력:"))
# if pres > 5.0 :
#     print("경고")
# else :
#     print("정상")    

# # 문제 2번
# count = 0
# for i in range(1,6) :
#     count += i
# print(count)

# # 문제 3번
# scores = [85, 92, 58, 71, 40]
# for s in scores : # s를 scores 별로 반복해서 보겠다.
#     if s >=90 :
#         grade = "A"
#     elif s >=80 :
#         grade = "B"
#     elif s >=60 :
#         grade = "C"
#     else :
#         grade = "F"
#     print(f'{s}점: {grade}')

# # 문제 4번
# count = 0
# for i in range(1,31) :
#     if i%3 == 0 and i%5 != 0:
#         count += 1
# print(count)

# # 문제 5번
# for i in range(1,21) :
#     s = str(i)
#     if "3" in s or "6" in s or "9" in s : 
#         print("짝")
#     else :
#         print(s)

# 문제 6번
# words = ["apple", "kiwi", "banana", "fig"]
# result = []
# for i in words :
#     if len(i) >= 5 :
#         result.append(i.upper())
# print(result)
# print(len(result))

# answer = 7
# guess = 0
# while guess != answer :
#     guess = int(input("맞혀보세요 :"))
# print("축하합니다.")

# for i in range(1,11) :
#     if i == 5 :
#         break
#     print(i)


# for i in range(1,7) :
#     if i%2 == 0 :
#         continue
#     print(i)

# while True :
#     x = input("입력 :")
#     if x == "q" :
#         break
# print("입력:",x)

# 문제 1번 05_01 ~ 05_03
# for i in range(3,16,3) :
#     print(i)

# # 문제 2번
# data = 0
# for i in range(1,101) :
#     data += i
# print(data)

# # 문제 3번 ***
# count = 10
# while count >= 1 : #조건이 참인 동안 반복
#     print(count)
#     count -= 1

# # 문제 4번 
# for i in range(1,11) :
#     if i%3 == 0 :
#         continue
#     print(i)

# 문제 5번 0단계한번, 1단계매바퀴, 2단계조건부 ***
# i = 1
# while True :           기본적으로 계속 반복
#     print(i)
#     if i%7 == 0 : 
#         break 
#     i += 1

# # 문제 6번
# num = int(input("정수:"))
# total = 0
# count = 0
# for i in range(1,num+1) :
#     if i%2 == 0 :
#         total += i
#         count += 1
# print(f'합: {total}, 개수: {count}')

# # 문제 7번
# n = int(input("측정 횟수:"))
# b = 0
# c = 0
# for i in range(1,n+1) :
#     a = int(input("측정값"))
#     b += a
#     c += 1

# if n != 0 : 
#     print("평균:",b/c)
# else :
#     print("데이터 없음")

# 문제 8번 ***
# answer = 42 
# guess = 0
# count = 0
# while guess != answer : #조건이 참인 동안 반복
#     guess = int(input("입력하세요:")) 
#     count += 1
#     if guess > answer :
#         print("크다")
#     elif guess < answer :
#         print("작다")
# print("정답입니다!", count)

# # 문제 9번
# for i in range(1,6) :
#     print("*"*i)

# 문제 10번 ***
#found = False #플래그 변수
#n = int(input("횟수:"))
#for i in range(1,n+1) :
#    value = int(input("측정값:"))
#    if value > 80 :
#       found = True
#        break
#if found :    
#    print("발견")
#else :
#    print("없음")

# 문제 11번
#temps = [25, 32, 28, 35, 19, 41]
#data_1 = 0
#data_2 = 0
#data_3 = 0
#data_4 = 0
#for i in temps :
#    data_1 += i
#    data_4 += 1
#    if i > 30 :
#        data_2 += 1
#        data_3 += i
#print(data_2,data_3/data_2)
#print(data_1/data_4)
#print(max(temps))

# 문제 12번 ***
# total = 0
# count = 0
# while True : # 값을 그냥 계속 입력 받을 경우
#     x = input("입력(q종료):")
#     if x == "q" :
#         break
#     v = int(x)
#     if v < 0 :
#         continue
#     total += v 
#     count += 1
# print(total,count)

# 문제 13번 ***
data = 0
i = 0
while data <= 500 :
    i += 1
    data += i
print(data,i)

# 문제 14번 ***
found = False
for i in range(2,10) :
    for j in range(1,10) : # ***for 2개 연달아 사용가능
         v= i * j
         if v > 50 :
            found = True
            break
         print(i,"*",j,"=",i*j) 
    if found :
        break
if found :
    print("끝")

# 문제 15번
data = [72, 85, 90, 64, 88, 79, 95]
found = False
count = 0
for i in data :
    if i > 80 :
        count += 1
        if count >= 2:
            found = True
            break
    else :
        count = 0
if found :
    print("연속 이상 발견")
else :
    print("없음")

# 문제 16번
temps = [25, 32, 28, 35, 27]
for i in temps :
    if i > 30 :
        print(i , "고온 주의")

# 문제 17번
hours = [8, 3, 6, 11, 10, 4, 9]
for i in hours :
    if i >= 5 and i <= 10 :
        print(i)

# 문제 18번
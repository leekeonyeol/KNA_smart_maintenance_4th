# # 문제 1
# report = int(input("정수:"))
# count = 0
# count_1 = 0
# for i in range(1,report + 1) :
#     if i%2 == 0 :
#         count += i
#         count_1 += 1
# print("합:",count,"개수",count_1)

# # 문제 2
# report = int(input("측정 횟수:"))
# report_1 = []
# count_2 = 0

# for i in range(1, report + 1) :
#     count_1 = int(input("측정값:"))
#     report_1.append(count_1)
#     count_2 += 1

# if report != 0 :
#     print("평균", sum(report_1)/count_2)
# else :
#     print("데이터")

# # 문제 2
# report = int(input("측정 횟수:"))
# count_2 = 0

# for i in range(1, report + 1) :
#     j = int(input("측정값:"))
#     count_2 += j

# if report != 0 :
#     print("평균", count_2/report)
# else :
#     print("데이터 없음")

# # 문제 3
# answer = 42
# count = 0
# count_1 = 0
# while  count != answer :
#     count = int(input("숫자를 입력하세요:"))
#     count_1 = 1
#     if count > answer :
#         print("크다")
#     elif count < answer :
#         print("작다")
# print(count_1, "번 만에 정답!")

# # 문제 4
# report = int(input("횟수:"))
# found = False
# for i in range(1, report + 1) :
#     count = int(input("측정값:"))
#     if count > 80 :
#         found = True
#         print("발견")
#         break
#     else :
#         print("없음")

# # 문제 4
# report = int(input("횟수:"))
# found = False
# for i in range(1, report + 1) :
#     count = int(input("측정값:"))
#     if count > 80 :
#         found = True
#         break

# if found == True :
#     print("발견")
# else :
#     print("없음")

# # 문제 5
# count = 0
# count_1 = 0
# while True :
#     report = input("입력하세요:")
#     if report == "q" :
#         break
#     v = int(report)
#     if v < 0 :
#         continue
#     count += v
#     count_1 += 1
    
# print("양수의 합",count,"양수의 개수",count_1)

# 문제 6
found = False
for i in range(2,10) :
    for j in range(1,10) :
        report = i * j
        if report > 50 :
            found = True
            break
        print(i,"x",j,"=",report)
    if found :
        break
    print("----")


    







print('--실습1--')

# num = int(input("나이를 입력하세요 :"))
# if num >= 20:
#     print("성인")
# else :
#     print("미성년자")

# data = 70 
# if data >= 90 :
#     print("A")
# elif data >= 80 :
#     print("B")
# elif data >= 70 :
#     print("C")
# else :
#     print("D")

# temp = 85
# if temp > 80:
#     print("위험")
# elif temp >60 :
#     print("주의")
# else :
#     print("정상")

# a = input("아이디:")
# b = int(input("패스워드:"))
# if a == "lky" and b == 456 :
#     print("로그인 성공")
# else :
#     print("로그인 실패")

# tem = int(input("온도 :")) #input의 결과는 문자열이다.
# vib = float(input("진동 :"))
# ele = int(input("전류 :"))
# if tem>80 or vib>4.0 :
#     print("위험: 즉시 정지")
# else:
#     if ele>60 and tem>70 :
#         print("주의: 부하 점검")
#     elif vib>2.5 :
#         print("주의: 진동 관찰")
#     else :
#         print("정상") 

# print("--실습2--")
# n = int(input("숫자 :"))
# for i in range(1,n+1) :
#     print(i)
# for j in range(2,n,2) :
#     print(j)
# for k in range(n,0,-1) :
#     print(k) 

# num = int(input("대입 숫자 :"))
# count = 0
# for i in range(1,num+1) :
#     count += i # i는 for문 밖에서는 사용 x 따라서 함수 생성 필수
# print("합:", count)

# for i in range(1,10) :
#     for j in range(1,10) :
#          print(i ,"x", j, "=", i*j)
#     print("---")


# data_1 = int(input("측정 횟수:"))
# count = 0
# for i in range(1,data_1+1) :
#     data_2 = int(input("측정값:"))
#     if data_2 > 80 :
#         count += 1
# print("초과 개수:",count) 

# for는 제한 횟수동안 반복
# while은 참인 동안 반복

print("--실습3--")
ans = 7
count = int(input("숫자:"))
while count != ans : #답이 아니면 계속 반복해
    count = int(input("맞혀 보세요: "))
print("정답입니다!")

# % 나머지, // 몫





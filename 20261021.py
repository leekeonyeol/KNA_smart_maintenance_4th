# 자료형 
count = 3 # int 정수
temp = 25.5 # float 실수
name = "센서" # str 문자열

ok = True   # bool 불린형 - 참/거짓
no = False

# print(type(25))
# print(type("센서"))
# print(type(ok))

# print(3 + 5)
# print("3" + "5")
# print("안녕" + "하세요")

# score = 10
# score += 10 # like x = x + 10
# print(score)

# print("---실습1---")

# count = 3
# temp = 2.5
# name = "감사"
# is_ok = True

# print(type(count))
# print(type(temp))
# print(type(name))
# print(type(is_ok))

# # 100 = int
# # 100.0 = float
# # "100" = str
# print(type(100))
# print(type(100.0))
# print(type("100"))

# print(2 + 7)
# print("2" + "7")
# print("27" + "34")

# # 3 > 2
# print(3 > 2)
# print(5 == 5)
# print(type(3 > 2))

# count = 2
# print(type(count))
# count = 2.3
# print(type(count))
# count = "2.3"
# print(type(count))

# device_temp = 25.3
# check_count = 7
# device_name = "기쁨"
# is_normal = True
# print(type(device_temp))
# print(type(check_count))
# print(type(device_name))
# print(type(is_normal))

# print(20 / 4) # 나눗셈의 결과는 실수
# print(7 // 2) # 몫
# print(7 % 2) # 나머지
# print(2**3) # 거듭제곱

# print("----실습2----")
# a = 17
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(a ** b)
# print(a / b)

# a = 6
# b = 8
# c = 10
# print((a + b + c) / 3)
# print(a * b)
# print(a * b * c)

# print("----실습3----")
# print( 2 == 2)
# print( 2 != 3)
# print( 2 > 3)
# print( 2 < 3) 
# print( 3 >= 2)
# print( 3 <= 2)

# temp = 85 
# print( temp >= 60 and temp <= 90)
# pre = 5
# print( pre >= 3 and pre <= 7)

# box = 100
# box += 50
# box -= 30
# box += 5
# print(box)

# print(str((23 / 500) * 100) + "%")
# print(str((21 / 24) * 100) + "%")
# print( str(500 // 60) , "시간" , str(500 % 60) , "분")

# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식 : 변수 = input("안내문구:")
# name = input("이름:")
# age = input("나이:")
# print(name,"이고",int(age),"이야")

# birth_year = input("태어난 연도 :")
# print(birth_year, "태어났으니", 2026 - int(birth_year), "살이구나")

# print("----실습4----")
# country = input("거주 국가 :")
# city = input("거주 도시")
# print(country, "의", city, "에서 거주하시는군요!")

# a = input("수학 :")
# b = input("영어 :")
# print("총 점수", int(a) + int(b))

# temp = int(input("현재온도는 :"))
# print("100이하?", temp <= 100)

# a = int(input("국어 :"))
# b = int(input("영어 :"))
# c = int(input("영어 :"))
# print("평균은", a+b+c / 3, "점 입니다.")
# print("평균 80이상?", (a+b+c / 3) >= 80)

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검"""
print(notice)

# \n 줄바꿈, \t 탬(간격), 엔터 위의 키로 사용
print("이름\t상태")
print("첫째\n둘째줄")

notice ="""가동 점검표
1. 온도 확인
2. 압력 확인"""
print(notice)
print("가동 점검표 \n 1. 온도 확인 \n 2. 압력 확인")
print("가동 점검표 \t 1. 온도 확인 \t 2. 압력 확인")

print("PUMP_A" + "/정상" + "/2025-01-15")

operation_time = int(input("현재 시간은 :"))
if operation_time >= 1700 :
    print("정상")
print("설비 \n 상태 \n" + str(operation_time) +"\n" + str(3>=2))

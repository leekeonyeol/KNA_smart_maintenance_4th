# 실습 3
def hello() :
    print("안녕하세요")
hello()
hello()

# 실습 4
def greet_2() :
    print("-"*5)
    
def grret_1() :
    print("점검을 시작하세요")

greet_2()
grret_1()

# 실습 1
def check(name) :
    print(name + "점검 시작")

check("압축기")
check("펌프1")

# 실습 2 
def check(name,temp) :
    print(name + str(temp) + "도")

check("모터", 78)
check("펌프", 92)

# 실습 3
def check(pres, vib) :
    print(str(pres) + "충격" + str(vib) + "진동")

check(pres = 75, vib = 30)
check(vib = 20, pres = 80)

# 실습 4
def minus(a,b) :
    return a - b
print(minus(9,5))
print(minus(8,1))

# 실습 5
def sum_1(values) :
    return max(values), min(values), (max(values) + min(values)) / len(values)
data_1, data_2, data_3 = sum_1([25, 30, 78, 80])
print(data_1, data_2, data_3)

# def report(필수, 선택=기본값)
# 같은 값을 매번 적는 번거로움을 줄인다
#  필요할 때는 덮어써도된다
def report(name, value, unit="도") : #unit="도" 가 기본값
    print(f'{name} : {value}{unit}')

report("압축기1",75.3)
report("압축기1",75.3,"bar")

# 실습 1 
def report(num, limit = 80) : # num, limit은 매개변수
    if num > limit :
        print("경고")
    else :
        print("정상")
report(90)
report(90, 100) # 90, 100은 인자

# 실습 2 
def data() :
    temp = 20 # 지역 변수
    print(temp)
data()

# 실습 3
value_1 = [25, 34, 26]
def get_avg(values) :
    return sum(values) / len(values)

def data(num, limit = 80) :
    if num > limit :
        return "경고"
    else :
        return "주의"

avg = get_avg(value_1)
print("평균:", round(avg, 1))
print(data(avg))





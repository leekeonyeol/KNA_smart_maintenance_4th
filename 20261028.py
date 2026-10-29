logs = ["S01", "S02", "S01", "S03"]
unique = set(logs)
print(unique)
print(sorted(unique,reverse = True))

ids = {"S01", "S02", "S01"} # set은 순서가 없다 , 중복 제거의 편의성을 위해 사용
print(type(ids))
print(ids)

ids.add("S04") # 추가 
print(ids)
print("S04" in ids) # 포함 여부

if "S02" in ids :
    print("S02 정비 알림")

ids_1 = {"S01", "S02", "S01"}
ids_2 = {"S03", "S04", "S02"}
a = ids_1.union(ids_2) # 연합
print(a)
b = ids_1.intersection(ids_2) # 교집합 출력
print(b)
c = ids_1.difference(ids_2)
print(c)

# 실습 4.
id_1 = ["S01", "S02", "S03", "S02"]
a = set(id_1)
print(sorted(a))
print(len(a))

# 실습 5.
ids_1 = {"S01", "S02", "S03"}
ids_2 = {"S03", "S04", "S02"}
a = ids_1.union(ids_2)
b = ids_1.intersection(ids_2)
c = ids_1.difference(ids_2)
d = ids_2.difference(ids_1)
print(a,b,c,d)

# 실습6. 
day_1 = {"S01", "S02", "S03"}
day_2 = {"S03", "S04", "S02"}
a = day_1.difference(day_2)
b = day_1.intersection(day_2)
print(a,b)


sensors = {"모터온도": 78, "진동": 0.5} # 콜론(:) 있으면 딕셔너리
print(sensors) # 빈중괄호{}는 딕셔너리
print(type(sensors))

sensors = {"모터온도": 78, "진동": 0.5} # 콜론이 있으므로 딕셔너리
print(sensors["모터온도"])
print(sensors["진동"])
sensors["유량"] = 42
print(sensors)
del sensors["모터온도"]
print(sensors)
print(sensors.get("모터온도")) # 없는 값을 꺼내도 오류대신 none을 출력한다.
print("진동" in sensors)
if "유량" in sensors :
    print(sensors.get("유량"))

# 실습 1.
sensors = {"모터온도": 78, "진동": 0.5, "유량": 20}
print(sensors["모터온도"]) #키로 검색
sensors["압력"] = 20 #추가
print(sensors)
print(sensors.get("속도")) # 조회
print( "진동" in sensors) # 존재 여부

sensors = {"모터온도": 78, "압력": 95}
print(list(sensors.keys()))
print(list(sensors.values()))
avg = sum(sensors.values()) / len(sensors)
print(avg)

sensors = {"모터온도": 78, "압력": 95}
for name,value in sensors.items() : # 딕셔너리에서의 언팩킹
    print(name, "측정값", value)

# 실습 2
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42} 
sensors.update(new_data) # 값을 받을 필요 없다
print(sensors)
del sensors["유량"]
print(len(sensors))

#실습 3
sensors = {"모터온도": 80, "진동": 0.5, "유량": 42}
print(sum(sensors.values()) / len(sensors))
max_value = 0
for key,value in sensors.items() :
    if value > max_value :
        max_value = value
print(max_value)

values = {"모터온도": 95, "압력": 88}
limits = {"모터온도": 90, "압력": 90}
for name, value in values.items(): # 순회
    if value > limits[name]:
        print(name, "경고")

# 실습 4
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names,values)) 
print(sensors)
for name,value in sensors.items() :
    print(name, value)

# 실습 5
values = {"모터온도": 95, "압력": 88}
limits = {"모터온도": 90, "압력": 90}
for key,value in values.items() :
    if value > limits[key] :
        print(key,value)

# 실습 6
plant = {
"1번모터": {"온도": 80, "상태": "정상"},
"2번펌프": {"압력": 90, "상태": "경고"} 
}
print(plant["1번모터"]["온도"])
for key,value in plant.items() :
    if value["상태"] == "경고" : # value["상태"]는 상태에 해당하는 값을 꺼낸다
        print(key,"점검필요")

# 실습 7 
sensors = ["모터온도,78", "진동,0.5", "압력,95"]
sensors_1 = {}
for i in sensors :
    i.split(",")
    a = i.split(",")
    name, value = a
    sensors_1[name] = float(value) # *** 추가 메커니즘
print(sensors_1)

# 실습 8 
value = {"모터온도": 95, "압력": 88}
limit = {"모터온도": 90, "압력": 90}
avg_1 = sum(value.values())/len(value)
avg_2 = sum(limit.values())/len(limit)
print(avg_1)
print(avg_2)
overlimit = {}
for name,val in value.items() :
    if val > limit[name] :
        overlimit[name] = val 
print(sorted(overlimit.keys())) # *** 키만 추출

def greet() :
    print("점검을 시작합니다")
greet()

def add(a,b) :
    return a+b
print(add(3,5))



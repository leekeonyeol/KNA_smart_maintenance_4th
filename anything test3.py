# 문제 1번 
sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
sensors["유량"] = 42 
print(sensors)
sensors["모터온도"] = 80 
print(sensors)
del sensors["압력"] 
print(sensors)

# 문제 2번
sensors = {"모터온도": 78, "압력": 95}
print(sensors.get("유량",0)) # get은 조회
print(sensors.get("압력",0))
if "유량" not in sensors :  # in도 도회
    print("유량 센서 없음")

# 문제 3번
temps = {"1호기": 78, "2호기": 82, "3호기": 91, "4호기": 85}
print(sum(temps.values()) / len(temps))
max_value = 0
for name, value in temps.items() :
    if value > max_value :
        max_value = value
        max_name = name # ***
print(max_name, max_value)

# 문제 4번
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
new_data = {"모터온도": 82, "유량": 40}
sensors = dict(zip(names,values)) # zip으로 네임과 밸류를 합치다
print(sensors)
sensors.update(new_data) # 새로운 값을 수정 및 추가, sensors["방향"] = 25 로 추가도 가능
print(sensors, len(sensors))

# 문제 5번
values = {"모터온도": 95, "진동": 0.4, "압력": 88, "유량": 30}
limits = {"모터온도": 90, "진동": 0.5, "압력": 85, "유량": 50}
data = []
for key, value in values.items() :
    if value > limits[key] : # ***
        data.append(key) # append는 list 에서만 
print(data)

# 문제 6번
plant = {
"1번모터": {"온도": 78, "상태": "정상"},
"2번펌프": {"압력": 95, "상태": "경고"},
"3번팬": {"진동": 0.9, "상태": "경고"},
}
print(plant["2번펌프"]["압력"])
data = []
for key, value in plant.items() :
    if value["상태"] == "경고" :
        data.append(key)
print(data)

plant["1번모터"]["상태"] = "점검중"
print(plant)

# 문제 7번
rows = ["온도,78", "압력,95", "진동,0.5"]
limits = {"온도": 70, "압력": 90, "진동": 1.0}
rows_1 = {}
rows_2 = set()
for i in rows :
    a = i.split(",")
    name, value = a
    rows_1[name] = float(value)
print(rows_1)
b = sum(rows_1.values())/len(rows_1)
print(round(b,1))

for name_1,value_1 in rows_1.items() :
    if value_1 > limits[name_1] :
        rows_2.add(name_1)
print(sorted(rows_2))

# 문제 8번
history = {
"모터온도": [78, 79, 80, 85],
"압력": [90, 92, 95, 97],
}
for name, value in history.items() :
    data = sum(value) / len(value) 
    print(f'{name} : {data}')

if history["압력"][3] > 95 :
    print("압력 경고")

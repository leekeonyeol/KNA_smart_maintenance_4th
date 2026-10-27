print("--실습1--")
# found = False # 플래스 변수
# num = int(input("횟수:"))
# for i in range(num) :
#     data = int(input("측정값 :"))
#     if data > 80 :
#         found = True 
#         break

# if found == True :
#     print("발견")
# else :
#     print("없음")

# temps = [25, 32, 28, 35, 19]
# for i in temps :
#     if i >= 30 :
#         print("고온:", i)

time = [3, 4, 8, 10, 15]
for i in time :
     if i >= 5 and i <= 10 :
         print(i)

temps = [25, 32, 28, 35, 19]
sumd = 0
count = 0
for i in temps :
     if i > 30 :
         sumd += i
         count += 1
print(float(sumd/count))

temps = [25, 32, 28, 35, 19]
select = []
for i in temps :
     if i > 30 :
         select.append(i)
print(select,"/",len(select))

temps = [25, 32, 28, 35, 19]
select = []
for i in temps :
     data = i*1.8 + 32
     select.append(data)
print(select)

temps = [25, 32, 28, 35, 19]
data = 0
result = []
for i in temps :
    data += i
    if i > 30 :
        result.append(i)
print("전체 평균:", data/len(temps))
print(len(result))
print("고온 평균:",sum(result)/len(result))

print("--실습1--")
sensor = ("모터온도", 78)
print(sensor)
print(sensor[0])
print(sensor[1])
sen, val = sensor
print(sen)
print(val)

sensors = [("모터온도",80), ("펌프압력",100)]
for name,value in sensors : # 바로 언팩킹 가능
    if value > 90 :
            print(name,"경고")

data = [("a",78,(3,5)), ("b",80,(4,6)), ("c",90,(5,7))]
for name,value, (x,y) in data :
     if x <= 5 :
          print(x,y)
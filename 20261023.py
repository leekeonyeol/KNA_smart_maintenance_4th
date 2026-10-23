print("---실습1---")
text_1 = 'PUMP_A'
text_2 = 87
print(f'설비{text_1}, 온도{text_2}도')
# f-string은 숫자와 글자를 혼용하기위해서 쓰는 도구 

numb = (80 + 70 + 40)
print(f'평균 {int(numb/3)} 점입니다.')
# 소수점은 value:.2f로 소수점 둘째자리를 나타낸다  

data = 87.456
clean_1 = f'{data:.1f}'
clean_2 = f'{data:.2f}'
print(clean_1, "/", clean_2)

text = ' 5 , sensor_2 , WARNING , 0.78912 '
clean_1 = text.strip()
clean_2 = clean_1.split(',')
print(f'[{clean_2[1]}상태],{clean_2[2]},측정값{float(clean_2[3]):.2f}')

data = [30, 29, 25, 23, 24]
print(data)
print(len(data))
print(len(''))

data = [30, 28, 26, 23, 24]
print(data[0], data[2], data[-1])

data = [30, 50, 40, 23, 24, 60]
text_1 = data[0]
text_2 = data[5]
print(text_1 + text_2)
clean_1 = text_1 + text_2
print(clean_1/2)

data = [30, 50, 40, 23, 24, 60, 80, 45, 12, 15]
clean_1 = data[:3]
clean_2 = data[-3:]
print(clean_1,clean_2,len(clean_1))

data = [30, 50, 40, 23, 24, 60, 80, 45, 12, 15, 15, 78]
first = data[:6]
second = data[-6:]
print(first,second,len(first),len(second))

temp = [25, 85, 48, 28, 240]
first = 25 in temp
print(first)
temp[4] = 24
print(temp)
second = 240 in temp
print(second)
# index는 색인 slice는 부분색인 

text = []
text_1 = [1, 2, 3]
first = text.append(30)
print(text)
second = text.insert(0,28)
print(text)
third = text.extend(text_1)
print(text)

data = [25, 84, 48, 999, 15]
first = data.remove(999)
print(data)
second = data.pop(3)
print(second)
del data[0]
print(data)

temp = [25, 84, 48, 36, 15]
first = temp.sort()
print(temp)
second = temp.reverse()
print(temp)
third = temp.count(25)
print(third)
fourth = temp.index(15)
print(fourth)

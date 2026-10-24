# print("git 명령어")
# print("update 2026")

# def add(a,b) :
#      return a+b 

# result = add(3,5)
# print(result)

# def minus(a,b) :
#      return a-b

# result = minus(8,3)
# print(result)

# score = 85

# if score >= 80 :
#     print("A")

# elif score >= 70 :
#     print("B")

# else :print("C")

# age = 25
# if age >= 20 and age <= 30 :
#     print("20대")

# text = "안녕"
# for i in range(3) :
#     print(text)

# fruits = ["사과", "배", "귤"]
# for fruit in fruits :
#     print(fruit)

record = ' 2025.01.15 / pump a 03 / WARNING / 1,250 rpm '
date = record.strip().replace(".","/")
print(date)

equipment = date.replace(" ",'-').upper()
print(equipment)

# 문제1번
text = "it's noraml"
print("설비 점검 \n" + text)

text = '사과, 배, 감'
clean_1 = text.split(',')
print(clean_1)
clean_2 = '/'.join(clean_1)
print(clean_2)

text = ' Hong@Company.com '
clean_1 = text.strip().lower()
print(clean_1)
clean_2 = clean_1.find('@')
print(clean_1[:clean_2])

text = ' hong gil dong '
clean_1 = text.strip().title()
print(clean_1)
clean_2 = clean_1.split(' ')
clean_3 = '-'.join(clean_2)
print(clean_3)

text = '사과, 배, 감'
clean_1 = text.split(',')
clean_2 = '-'.join(clean_1)
print(clean_2)

text = ' Sensor Measurement 3 '
clean_1 = text.strip().lower().replace(' ',"_")
print(clean_1)

code = 'AM6'
name = 'gildong'
stock = 8
print(f'{code}인 {name}은 {stock}개가 남아있습니다')

a = '25'
b = 5
print(int(a)+b ,"/", a+str(b))

print('='*20 + '설비 상태 보고' + '='*20)

code = 'PUMP_A_03'
clean_1 = len(code),code[0],code[-1]
print(clean_1)

date = '20250115'
print(date[:4],date[4:6],date[6:],sep='/') 
# sep는 무조건 print안에서만 사용가능

word = 'SIGNAL'
first = word[::2]
second = word[::-1]
third = word[-3:]
print(first,second,third)

fn = 'sensor_log.csv'
first = fn.endswith('.csv')
print(first)
second = fn.find('.')
third = fn[:second]
print(third)

email = 'hong@company.com'
print(email[:email.find("@")],email[email.find("@")+1:])

# 문제 9번 03_04, 04_05
log = ' WARNING,NORMAL,WARNING,FAULT '
first = log.index("WARNING")
print(first)
second = log.count("WARNING")
print(second)
print("WARNING" in log)

# 문제 10번
a = 'Normal'
b = 'NORMAL'
print(a == b)
print(a.lower() == b.lower())

# 문제 11번
raw = '  FAULT  '
print(raw == 'fault')
raw_1 = raw.strip().lower()
print(raw_1 == 'fault')

# 문제 12번
text = '  가동중  '
text = text.strip()
print('[' + text + ']')

# 문제 13번
text = '***경고***'
text = text.strip('*')
print('[' + text + ']')
s = ' 대기 '
s = s.lstrip()
print('[' + s + ']')

# 문제 14번
phone = ' 010-1234-5678 '
phone = phone.strip().replace('-','')
print(phone, len(phone))

# 문제 15번
st = 'fault, FAULT, Fault'
st = st.lower().replace('fault','고장')
print(st)

# 문제 16번
row = '1, NORMAL ,25.3'
row = row.split(',')
first = row[1].strip().lower()
print(first)
second = float((row[2])) + 1
print(second)

# 문제 17번
n = 'sensor_01_temp'
n = n.split('_')
print(n)
first = '-'.join(n)
print(first)
second = ' '.join(n).title()
print(second)

# 문제 18번 
c = 'EQP-001-NORMAL'
c = c.split('-',1)
print(c)
second = c[0].lower()
print(second)

# 문제 19번
raw = ' Pump A 03 '
raw = raw.strip().upper().split(' ')
print(raw)
first = '_'.join(raw)
print(first.startswith('PUMP'))

# 문제 20번
line = '  15, eqp-001 , WARNING , 31.5\n'
first = line.strip().split(',')
print(first)
second = first[1].strip().upper()
print(second)
third = float(first[3].strip())
print(third)

# 문제 1번 03_02, 03_03 
temp = 25
print(f'온도 : {temp}')

# 문제 2번
code = 'PUMP_A'
status = '정상'
hours = 120
text = f'{code} / {status} / {hours}'
print(text) # f-string은 변수들을 변환 없이 받기위한 장치

# 문제 3번
date = '20250115'
a = date[0:4]
b = date[4:6]
c = date[6:]
print(f'{a}-{b}-{c}')

# 문제 4번
phone = '01012345678'
a = '010'
b = '1234'
c = '5678'
print(f'{a}-{b}-{c}')

# 문제 5번
log = 'WARNING,NORMAL,WARNING,FAULT'
a = len(log)
b = log.count("WARNING")
c = log.find("FAULT")
print(f'전체 길이: {a}, WARNING 횟수: {b}, FAULT 위치: {c}')

# 문제 6번
code = 'EQP-001'
status = '정상'
hours = 1500
date = '20250115'
date = date[0:4]+'-'+date[4:6]+'-'+date[6:]
print(f'설비: {code}\n상태: {status}\n가동: {hours}시간\n점검: {date}')

# 문제 7번
filename = 'cmapss_fd001.csv'
a = filename[:9]
b = filename.find("_")
c = filename[9:12]
d = "csv" in filename
print(f'파일명:{filename}, 이름:{a}, 언더바 위치:{b}, 번호:{c}, csv여부:{d}')

# 문제 1번


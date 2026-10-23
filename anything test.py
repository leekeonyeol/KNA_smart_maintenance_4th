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

# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 형식 : 문자열[번호]  (첫 글자 = 0번)

word = 'python'
print(word[0], word[2])
# 음수 인덱스 : 뒤에서부터 -1 ,-2 
print(word[-1], word[-3])

print("---실습1---")
word = 'SIGNAL'
print(word[0], word[2], word[5])
print(word[-1], word[-2])

word = 'SIGNAL'
print(word[0:3] + "/" + word[2:5])

word = 'temp_sensor'
print(word[:4])
print(word[5:])

word = 'sensor_01'
print(word[-2:])

word = 'SIGNAL'
print(word[::2])
print(word[::-1])

print("---실습2---")
number = '01012345678' #문자열!을 대입한다
numb = len(number)
print(numb)

word = '설비 고장 발생'
print('고장' in word, "/", '정상' in word) 

word = 'sensor-01-temp'
print(word.count('-'))

word = 'temp_2024'
ok = word.find('_')
print(ok)

word = 'sensor_log.csv'
ok_1 = word.startswith('sensor')
ok_2 = word.endswith('.csv')
print(ok_1, "/", ok_2)

label = 'warning'
go_1 = label =='warning'
go_2 = label =='WARNING'
print(go_1, "/", go_2)

# find와 index는 비슷한 함수
# find는 없으면 '-1' index는 없으면 오류

# in과 statswith는 비슷한 함수
# in은 어디든 포함 startswith는 맨 앞 endswith는 맨 뒤
print("---실습3---") 
#  메서드 예시) word.method()
word = "ready"
at = word.upper()
print(at)

word = 'WARNING'
at = word.lower()
print(at)

word = 'kim chul soo'
at = word.title()
print(at)

ok_1 = 'Fault'
ok_2 = 'FAULT'
at_1 = ok_1 == ok_2
at_2 = ok_1.lower() == ok_2.lower()
print(at_1, ">", at_2)
print('ABC'.isupper(), "/", 'abc'.islower(), "/", 'Abc'.islower())

text = 'Sensor_LOG.CSV'
ok_1 = text.lower()
result1 = ok_1.startswith('sensor')
result2 = ok_1.endswith('.csv')
print(result1, "/", result2)

text = " 가동중 "
text = text.strip() 
print('[' + text + ']')

# 한쪽 공백만 제거하기 
text = ' 대기 '
text1 = text.lstrip()
text2 = text.rstrip()
print('[' + text1 +']', "/", '[' + text2 + ']')

text = '***경고***'
text1 = text.strip('*')
print(text1)
# strip은 앞뒤 공백 제거 replace는 글자 사이의 공백도 제거

text = ' WARNING '
clean = text.strip().lower()
print(clean)

text = ' 경보 '
clean_2 = text.strip()
print("[" + text + "]")
print("[" + clean_2 + "]")

print("---실습4---") 
text = '설비 정상 가동'
clean = text.replace('정상','점검')
print(clean)

text = 'PUMP A 03'
clean = text.split()
print(clean)

text = 'a,b,c,d'
clean = text.split(',')
print(clean)
clean_1 = text.split(',',1)
print(clean_1)

text = ['2025','01','15']
clean = '-'.join(text) # join은 예외적으로 구분자가 앞에 온다
print(clean)

print('2025','1','15',sep='-')
print('2025','1','15',sep=',')

date = '2025/01/15'
clean_1 = date.split('/')
clean_2 = '-'.join(clean_1)
print(clean_2)

text = '1, NORMAL ,25.3'
clean_1 = text.split(',')
print(clean_1)
clean_2 = clean_1[1]
print(clean_2)
clean_3 = clean_2.strip().lower()
print(clean_3)


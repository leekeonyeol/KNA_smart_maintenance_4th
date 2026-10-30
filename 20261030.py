# 모듈 / 패키지 / 라이브러리
# 모듈: 기능을 모아둔 .py 파일 하나
# 패키지: 모듈을 모아둔 폴더 
# 라이브러리: 위에 사항들을 통칭

# import math # math 모듈을 불러온다
# result = math.sqrt(16) # math 모듈에 있는 sqrt 기능
# print(result)
# result_1 = math.sqrt(25)
# print(result_1)

# from math import sqrt
# print(sqrt(25))
# print(sqrt(16))

# import math as m
# report = m.sqrt(16)
# print(report)
# report_1 = m.sqrt(25)
# print(report_1)

# # 실습 2
# import random 
# report = random.randint(1,20)
# print(report)

# import math
# report_1 = math.sqrt(report)
# print(round(report_1,1))

# os.getcwd() 현재 작업 디렉토리를 문자열로 반환
# os.listdir(경로) 폴더 안 파일을 리스트로 반환


# # 실습 3
# import os 
# report = os.getcwd()
# print(report) # 현재 작업 폴더

# report_1 = os.listdir("data")
# for i in report_1 :
#      if i.endswith(".csv"):
#           print(i)

# # 실습 4 
# import os
# report = os.path.join("data","08_press.csv") # 경로 생성
# report_1 = os.path.exists(report) # 유무 확인
# if report_1 == True :
#      print("있음")
# else :
#      print("없음")

# # 실습 5
# import os  
# import datetime as dn

# report = os.listdir("data")
# report_1 = len(report)
# report_2 = dn.datetime.now()
# print(f'파일{report_1}개, 점검 시각{report_2}')

# # 실습 6
# import os
# count = []
# report = os.listdir("data")
# for i in report :
#      if i.endswith(".csv") :
#           count.append(i)
# print(count)

# for j in count :
#      path = os.path.join("data",j)
#      print(path)
# print(os.path.exists(path)) 경로 설정이 제대로 되었나 확인용 

FILE = "data/08_press_13_261029_3.csv" # 상수
f = open(FILE,'r',encoding='utf-8')
text = f.read() # 한 덩어리 문자열
print(text)
f.close() # 파일을 열면 닫아줘야함

f = open(FILE,'r',encoding='utf-8')
text = f.readline() #  한 줄 문자열
print(text)
f.close()

f = open(FILE,'r',encoding='utf-8')
text = f.readlines() # 한 줄 리스트
print(text)
f.close()

# 실습 2
with open("data/text.txt", "w", encoding = "utf-8") as f : # with open은 자동 닫김
    f.write("쓰기 테스트")

with open("data/text.txt", "r", encoding= "utf-8") as f :
    text = f.read()
    print(text)

# 실습 3 
with open("data/text.txt", "a", encoding= "utf-8") as f :
    f.write("\n두번째 쓰기 테스트")

with open("data/text.txt", "r", encoding="utf-8") as f :
    text = f.read()
    print(text)

# 실습 4
import csv
with open(FILE, "r", encoding = "utf-8") as f :
    reader = csv.reader(f) #  각 행은 list, 각 값은 문자열
    for i in reader :
        print(i)

# 실습 5 
import csv
with open(FILE,"a",encoding = "utf-8",newline='') as f : 
    writer = csv.writer(f)
    writer.writerow(["PRESS-01", "2022-10-30 01:00:00.019", "0.117", "-0.1764", "192.3387", "0"])


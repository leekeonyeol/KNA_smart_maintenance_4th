# # 문제 1
# import math
# report = math.sqrt(16)
# report_1 = math.ceil(4.2)
# print(report, report_1)

# # 문제 2 
# from math import sqrt 
# report = sqrt(25)
# print(report)

# # 문제 3 
# import datetime as dt
# report = dt.datetime.now()
# print(report)

# # 문제 4
# import os # operating system
# report = os.getcwd() # 현재 작업 디렉토리
# print(report)

# # 문제 5
# import os 
# report = os.path.join("data","08_press.csv") # only 합치는 기능, 생성 x
# print(report)
# report_1 = os.path.exists(report)
# print(report_1)

# # 문제 6
# with open("data/08_press_13_261029_3.csv","r",encoding="utf-8") as f :
#     report = f.readlines()

# print(len(report)) # 행의 수
# print(report[0].strip()) # 첫번째 행 

# # 문제 7
# import csv # 현장 데이터의 대부분의 구조 = csv

# count = 0
# with open ("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f :
#     report = csv.reader(f) # 각 행은 리스트로, 모든 값은 문자열로 반환
#     next(report)
#     for i in report :
#         count += 1
# print(count)

# # 문제 8
# import csv

# currents = []
# with open ("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f :
#     report = csv.reader(f)
#     next(report)
#     for i in report :
#         currents.append(float(i[4]))

# print(max(currents))

# # 문제 9
# import csv

# with open ("data/08_press_13_261029_3.csv", "a", encoding="utf-8", newline="") as f :
#     report = csv.writer(f) # 리스트를 행으로 써준다.
#     report.writerow(["PRESS-01", "2022-11-01 01:00:10.019", "0.117", "-0.18964", "192.3387", "0"])

# # 문제 10

# with open ("data/text.txt", "w", encoding="utf-8", newline="") as f :
#     f.write("점검 시작\n")

# with open ("data/text.txt", "a", encoding="utf-8", newline="") as f :
#     f.write("점검 종료\n")

# with open ("data/text.txt", "r", encoding="utf-8") as f :
#     report = f.readlines()

# print(report)

# # 문제 11번
# import os
# csv_files = []
# report = os.listdir("data") # 파일 목록을 리스트 형태로 반환
# for i in report :
#     if i.endswith(".csv") :
#         csv_files.append(i)

# for name in csv_files :
#     report_1 = os.path.join("data",name)

# print(report_1)

# # 문제 12번
# import random 
# import math
# lists = []

# for i in range(1,6) :
#     lists.append(random.randint(1,100))

# for v in lists :
#     report = round((math.sqrt(v)),2)
#     print(v, report)

# # 문제 13번
# import os
# import csv
# report = os.path.join("data","08_press_13_261029_3.csv")

# if os.path.exists(report) :
#     with open(report, "r", encoding="utf-8") as f :
#         report_1 = csv.reader(f) # 각 행을 리스트, 문자열 형태로 반환
#         next(report_1)
#         rows = list(report_1) # 그것을 리스트 형태로 받음
#     print(len(rows))
# else :
#     print("파일 없음 : 경로")

# # 문제 14번
# import csv
# count =[]

# with open ("data/08_press_13_261029_3.csv", "r", encoding= "utf-8") as f :
#     report = csv.reader(f)
#     header = next(report) # 첫 줄을 꺼내서 저장
#     for i in report :
#         if int(i[5]) == 1:
#             count.append(i)

# import csv
# with open ("data/08_press_abnormal.csv", "w", encoding= "utf-8", newline="") as f :
#     report_1 = csv.writer(f)
#     report_1.writerow(header)
#     for i in count :
#         report_1.writerow(i)

# # 문제 15번
# import csv
# limit = 90
# count = []
# with open ("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f :
#     report = csv.reader(f)
#     header = next(report)
#     for i in report :
#         if float(i[4]) >= limit :
#             count.append(i)

# with open ("data/over.csv", "w", encoding="utf-8",newline="" ) as f :
#     report_1 = csv.writer(f)
#     report_1.writerow(header)
#     for j in count :
#         report_1.writerow(j)


        



        




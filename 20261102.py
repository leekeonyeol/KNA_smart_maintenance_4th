# # 실습 6
# import csv 
# limit = 90
# data = []
# with open ( "data/08_press_13_261029_3.csv", "r",encoding="utf-8") as f :
#     report = csv.reader(f)
#     next(report)
#     for i in report :
#         if float(i[4]) > limit :
#             data.append(i)
# print(data)

# import csv 
# with open ( "data/over.csv", "w", encoding="utf-8",newline="") as f :
#     writer = csv.writer(f)
#     for i in data :
#         writer.writerow(i)


# 실습 

# # 실습 2
# try :
#     num = int((input("온도:")))
#     print(num)
# except ValueError :
#     print("숫자를 입력하세요")

# print("프로그램은 계속 진행됩니다.")

# # 실습 3
# try :
#     num = int(input("측정값:"))
#     print( 100/num )
# except ValueError :
#     print("숫자가 아닙니다.")
# except ZeroDivisionError :
#     print("0으로 나눌 수 없습니다.")

# print("프로그램은 계속 진행됩니다.")

# else 예외가 하나도 안나왔을때
# finally 실패여부와 상관없이 무조건 마지막 실행

# text = "62.5"
# try :
#     temp = float(text)
# except ValueError :
#     print(" 변환 실패 ")
# else :
#     print("변환 성공", temp)
# finally :
#     print("종료")

# # 실습 4
# f = None # 이차 에러 방지
# try :
#     f = open("data/09_ict_inspection_dirty_15_261102_12.csv","r",encoding="utf-8")
#     text = f.read()
# except FileNotFoundError :
#     print("오류 발생")
# else :
#     print(text, "성공")
# finally :
#     if f is not None :
#         f.close()
#     print("실행됨")

# 실습 2번
try :
    with open ("data/09_ict_inspection_dirty_15_261102_2.csv", "r", encoding="utf-8") as f :
        rows = f.readlines()[1:] # 한줄의 리스트로 반영
except FileNotFoundError :
    rows = []

total = 0.0
skipped = 0
for i in rows :
    try :
        total += float(i.split(",")[3]) # 측정값 (3열)
    except (IndexError) :
        skipped += 1
        continue

print(round(total,1))
print(skipped)

# 실습 4번
import os 

count = 0
count_1 = 0
data = os.listdir("data")

for i in data :
    path = os.path.join("data",i)
    try :
        with open (path,"r",encoding="utf-8") as f :
               count += 1
    except FileNotFoundError :
        count_1 += 1
        continue
print("파일 개수", count ,"미존재 파일 개수", count_1)







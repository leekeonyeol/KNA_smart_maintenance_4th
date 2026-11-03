# # 실습 5번
# def check_value ( text , lo=0.0 , hi=5000.0) :
#     v = float(text)
#     if not (lo <= v <= hi) :
#         raise ValueError ("정상 범위 밖")
#     return v

# for i in ["128.5", "결측", "-999"] :
#     try :
#         print(check_value(i), "통과")
#     except ValueError as e:
#         print("제외", e)

# 실습 1번
import csv 

DATA_PATH = "data/09_ict_inspection_dirty_15_261102_2.csv"

def read_csv_data(path) :
    with open (path, "r", encoding="utf-8") as f :
        text = csv.reader(f)
        header = next(text)
        rows = list(text)
    return header, rows

try :
    header, rows = read_csv_data(DATA_PATH) 
except FileNotFoundError :
    header, rows = [], []

print(header, len(rows))



    





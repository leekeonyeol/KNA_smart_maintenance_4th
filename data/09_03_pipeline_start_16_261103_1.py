"""ICT 검사 CSV 처리 파이프라인 — 교육생 실습 시작 코드.

1단계부터 6단계까지 완성할 때마다 RUN_TO_STEP을 하나씩 올리세요.
PPT의 실습 1~6과 함수가 대응합니다. 추가 패키지는 필요하지 않습니다.
"""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_PATH = "data/09_ict_inspection_dirty_15_261102_2.csv"
REPORT_PATH = BASE / "09_report.txt"
RUN_TO_STEP = 5  # 실습 1 완성 후 2, ... 6으로 변경


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


def group_by_part(rows):
    by_part = {}
    dropped = 0

    for row in rows :
        try :
            key = row[1]
        except IndexError :
            dropped += 1
            continue

        if key not in by_part :
            by_part[key] = []
        by_part[key].append(row)
    return by_part, dropped


def calc_stats(rows , column=2):
    values = []
    count_1 = 0
    for row in rows :
        try :
            data = float(row[column])
        except (ValueError,IndexError) :
            continue
        values.append(data)
        count_1 += data

    if not values :
        return None
        
    return {"count":len(values), "mean": count_1 / len(values),
            "max": max(values),"min": min(values)}


def filter_valid_rows(rows, lo=0.0, hi=5000.0):
    valid = []
    rejected = []
    
    for n, row in enumerate(rows, start=2) :
        try :
            check_id =row[0]
            data = float(row[2])
            if not ( lo <= data <= hi) :
                raise ValueError (" 정상 범위 밖 ")
            valid.append(row)
        except IndexError :
            rejected.append((n, check_id ,"측정값 열 부족"))
            continue
        except ValueError as e:
            rejected.append((n, check_id ,str(e)))
            continue
        
    
    return valid, rejected    
    
    
def save_report(path, total_rows, valid_rows, rejected, stats):
    lines = []
    lines.append(f"전체 행: {total_rows}")
    lines.append(f"유효 행: {len(valid_rows)}")
    lines.append(f"제외 행: {len(rejected)}")

    if stats is not None :
        lines.append(f"평균: {stats['mean']:.2f}")
        lines.append(f"최대: {stats['max']}")
        lines.append(f"최소: {stats['min']}")

    with open (path, "w", encoding="utf-8",newline="") as f :
        f.write("\n".join(lines))



def verify_part_counts(valid_rows):
    """[실습 6] 유효 행을 부품별로 다시 묶고 합계가 전체와 같은지 확인."""
    # TODO: group_by_part(valid_rows)를 재사용하고
    # 각 부품에 calc_stats(part_rows, 2)를 적용해 건수를 합산하세요.
    raise NotImplementedError("실습 6: 부품별 검증 함수를 완성하세요")


def main():
    header, rows = read_csv_data(DATA_PATH)
    print(f"[1단계] 헤더 {len(header)}개 / 데이터 {len(rows)}행")
    if RUN_TO_STEP == 1:
        return

    by_part, dropped = group_by_part(rows)
    print(f"[2단계] 부품 {len(by_part)}종 / 부품명 누락 {dropped}행")
    if RUN_TO_STEP == 2:
        return

    before = calc_stats(rows, 2)
    print(f"[3단계] 범위 검증 전 통계: {before}")
    if RUN_TO_STEP == 3:
        return

    valid, rejected = filter_valid_rows(rows)
    after = calc_stats(valid, 2)
    print(f"[4단계] 유효 {len(valid)}건 / 제외 {len(rejected)}건")
    for item in rejected:
        print("    제외:", item)
    if RUN_TO_STEP == 4:
        return

    save_report(REPORT_PATH, len(rows), valid, rejected, after)
    print(f"[5단계] 리포트 생성: {REPORT_PATH.name}")
    if RUN_TO_STEP == 5:
        return

    verify_part_counts(valid)


if __name__ == "__main__":
    main()

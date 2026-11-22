# import random

# answer = random.randint(1,100)
# count = 0

# while True :
#     try :
#         guess = int(input("숫자 입력:"))
#     except ValueError :
#         print("숫자를 입력하세요.")
#         continue

#     count += 1

#     if guess > answer :
#         print("숫자가 너무 커요.")
#     elif guess < answer :
#         print("숫자가 너무 작아요.")
#     else :
#         print(f"정답! {count}번만에 맞추셨어요.")
#         break

import random

choices = ["가위", "바위", "보"]
win = 0
lose = 0
draw = 0

while True :
    user = input("가위/바위/보 (종료: q):").strip()

    if user == "q" :
        break
    elif user not in choices :
        print("가위 바위 보 중에서 내세요.")
        continue

    computer = random.choice(choices)
    print(f"컴퓨터 : {computer}")

    if user == computer :
        draw += 1
        print("비겼습니다.")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        win += 1
        print("이겼습니다.")
    else :
        lose += 1
        print("졌습니다")

print(f"결과: {win}승 {lose}패 {draw}무")






    
    
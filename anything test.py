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
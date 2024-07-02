# 문제 1
name1 = input("이름을 입력하세요: ")
age1 = input("나이를 입력하세요: ")
email1 = input("이메일을 입력하세요: ")
phone1 = input("연락처를 입력하세요: ")

name2 = input("이름을 입력하세요: ")
age2 = input("나이를 입력하세요: ")
email2 = input("이메일을 입력하세요: ")
phone2 = input("연락처를 입력하세요: ")

dic1 = {name1 [age1, email1, phone1]}
print(dic1)
dic2 = {name2 [age2, email2, phone2]}
print(dic2)

# 문제 2
exchange = {'달러': 1320, '엔화': 800, '위안': 182}
chul = [13, 200, 13]

print(exchange['달러'] * chul[0] + exchange['엔화'] * chul[1])
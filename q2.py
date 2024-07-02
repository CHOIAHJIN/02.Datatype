# 문제 2
exchange = {'달러': 1320, '엔화': 950, '위안': 182}
chul = [13, 200, 13]

total = exchange['달러'] * chul[0] + exchange['엔화'] * chul[1] + exchange['위안'] * chul[2]

print('철수가 가지고 있는 돈은', total, '원 입니다.')
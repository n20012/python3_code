user_birth = input('あなたの誕生日をスラッシュ(/)区切りで入力してください。　例：1992/7/19 \n → ').split('/')
week = {0:'土曜日', 1:'日曜日', 2:'月曜日', 3:'火曜日', 4:'水曜日', 5:'木曜日', 6:'金曜日'}
# j = user_birth[0:2]
# print(j)
# print(user_birth)

j = int(user_birth[0][0:2])
k = int(user_birth[0][2:])
m = int(user_birth[1])
q = int(user_birth[2])
# print(j)
# print(k)
# print(m)
# print(q)

#h = (j + Fraction((m + 1) * 26, 10) + 92 + Fraction(92, 4) + Fraction(19, 4) - 2
# = (19 

h = (q + ((m + 1) * 26 // 10) + k + (k // 4) + (j // 4) - 2 * j) % 7

print(str(week[h]) + 'です。')
# print(week[h])

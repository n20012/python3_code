import datetime
today = datetime.date.today()
 # print(today.year)
num = int(input('１〜９まで好きな数字を入力してください。\n→ '))
birthday = int(input('誕生した西暦を入力してください。　例：2020　\n→ '))
birthday_later = input('今年の誕生日は過ぎましたか？:yes or no \n→ ')

ans = (num * 2 + 5) * 50 + int(today.year)
#print(ans)


if birthday_later == 'yes':
    anser = str(ans - 250 - birthday)
    print(str(ans - 250 - birthday))
    print('あなたが選んだ数字は' + anser[0] + 'で、\nあなたの年齢は' + anser[1:2 + 1] + 'ですね？(๑• ̀д•́ )✧+°ﾄﾞﾔｯ')
elif birthday_later == 'no':
    anser = str(ans - 251 - birthday)
    print(str(ans - 251 - birthday))
    print('あなたが選んだ数字は' + anser[0] + 'で、\nあなたの年齢は' + anser[1:2 + 1] + 'ですね？(๑• ̀д•́ )✧+°ﾄﾞﾔｯ')
else:
    None



#if birthday_later == 'yes':
#    anser = str(ans - 250 - birthday)
#    print('あなたが選んだ数字は' + anser[0] + 'で、\nあなたの年齢は' + anser[1:2 + 1] + 'ですね？(๑• ̀д•́ )✧+°ﾄﾞﾔｯ')
# elif birthday_later == 'no':
#     anser = str(ans - 251 - birthday)
#     print('あなたが選んだ数字は' + anser[0] + 'で、\nあなたの年齢は' + anser[1:2 + 1] + 'ですね？(๑• ̀д•́ )✧+°ﾄﾞﾔｯ')
# else:
#     None

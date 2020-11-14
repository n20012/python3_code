user_have_money = int(input('所持金を入力してください。　例：29953 \n =>'))

onedays_usedmoney = {'lunch':500, 'drinks':300, 'smokings':500, 'gas':500}

 # onedays_usedmoney_total
 # print(sum(onedays_usedmoney.values()))
    # 1800

onedays_usedmoney_total = sum(onedays_usedmoney.values())

if user_have_money < onedays_usedmoney_total:
    print("You can't live")
else:
    print("You have " + str(user_have_money // onedays_usedmoney_total) + "days worth of money")

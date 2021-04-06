print("Сейчас мы Вас обсчитаем, то есть рассчитаем\n\n")
total_bil = input ("На какую сумму вы тут нажрали?\n")
if float(total_bil) >= 200:
  print ("С паршивой овцы хоть шерсти клок")
else:
  print ("Кто сюда пустил этих нищебродов???")
percent_tip = input ("Какой процент чаевых вы не зажидите нашем заведению?\n 5, 10 или 50?\n")
if float(percent_tip) == 10:
  print ("Видимо я совсем мало плюнул в ваш чай")
if float(percent_tip) == 5:
  print ("Вася, занеси этих оборванцев в черный список заведения")
if float(percent_tip) == 50:
  print ("В убогом теле таится щедрая душа")
if float(percent_tip) != 5 or float(percent_tip) != 10 or float(percent_tip) != 50:
  print ("Даже выбрать из трех вариантов не можете, вы что с Кавказа? Но так и быть применим ваше значение")
overal_human = input ("И сколько вас здесь чавкало?\n")
bil_from_human = round ((float(total_bil) + float(total_bil)*float (percent_tip)/100)/float(overal_human), 2)
if bil_from_human > 50:
    print (f"И толпа из {overal_human} человек нажрала всего на {total_bil} рублей? О боги!" "\n \n" f"С каждого из вас по {bil_from_human} руб. и больше не появляйтесь в нашем заведении")
else:
    print("У вас минимальный чек с человека, 50 руб. Можем оформить в кредит в микрозаймах.")

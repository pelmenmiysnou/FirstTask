import math


a = float(input("введите первое делимое: \n"))
b = float(input("пожалуйста, введите делитель: \n"))
if (b != 0):
    print(a/b)
else:
    print("div on 0!!!!")


a = float(input("на какую сумму вы закупились? \n"))
if (a > 20):
  b = a * (1 - 1 * (35/100))
  print(f'ваша скидка: {round(a * 35/100, 2)}, к оплате: {round(b, 2)}')
else:
  print(f'Скидки нет, к оплате: {a}')


month = int(input("пожалуйста, введите номер месяца: \n"))
if month < 1 or month > 12:
  print("неверный номер!")
else:
  if month > 2 and month <= 5:
    print("Весна")
    if month == 3:
      print('Март')
    elif month == 4:
      print('Апрель')
    elif month == 5:
      print('Май')
  elif month > 5 and month <= 8:
    print("Лето")
    if month == 6:
      print('Июнь')
    elif month == 7:
      print('Июль')
    elif month == 8:
      print('Август')
  elif month > 8 and month <= 11:
    print("Осень")
    if month == 9:
      print('Сентябрь')
    elif month == 10:
      print('Октябрь')
    elif month == 11:
      print('Ноябрь')
  elif month == 1 or month == 2 or month == 12:
    print("Зима")
    if month == 1:
      print('Январь')
    elif month == 2:
      print('Февраль')
    elif month == 12:
      print('Декабрь')

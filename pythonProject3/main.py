import calendar
from datetime import datetime, date, time
print('Добро пожаловать в программу "Календарь".Чтобы запустить приложение, напишите "Запуск"')
txt=input()
while txt.lower()=="запуск":
    print("Вы вошли в систему. Вам доступны такие функции, как: 1) расписание на месяц, год; 2) конкретная дата; 3) Сегодняшний день. Чтобы выйти из программы,напишите 'Выход'.")
    text=input().lower()
    if text == 'расписание на месяц':
        c = calendar.LocaleTextCalendar(locale="Russian_Russia")
        theyear = int(input('Введите год:'))
        themonth = int(input('Введите месяц:'))
        print(c.prmonth(theyear, themonth))
    if text == 'расписание на год':
        c = calendar.LocaleTextCalendar(locale="Russian_Russia")
        theyear = int(input('Введите год:'))
        print(c.formatyear(theyear))
    if text == 'конкретная дата':
        c = calendar.LocaleTextCalendar(locale="Russian_Russia")
        year = int(input('Введите год:'))
        month = int(input('Введите месяц:'))
        day = int(input('Введите день:'))
        if calendar.weekday(year, month, day) ==0:
            print('Понедельник')
        elif calendar.weekday(year, month, day)==1:
            print('Вторник')
        elif calendar.weekday(year, month, day)==2:
            print('Среда')
        elif calendar.weekday(year, month, day)==3:
            print('Четверг')
        elif calendar.weekday(year, month, day)==4:
            print('Пятница')
        elif calendar.weekday(year, month, day)==5:
            print('Суббота')
        else:
            print('Воскресенье')
    if text=='сегодняшний день':
        a = datetime.now()
        print(a.date())
    if text == 'выход':
        print('Спасибо за использование нашей программы)))')
        break
import datetime

# Определить кварталы
# Проверить имя[1] - Газпром ли это?
# Если Да:
# Посмотреть Дату[2] и соотнести Кварталом
# Скопировать Поступление[3] или Отчисление[4]
# Если Нет:
# Перейти к следующей строке

quartes = {
    '1 квартал 2015' : [ datetime.date(2015,1,1), datetime.date(2015,3,31)],
    '2 квартал 2015' : [ datetime.date(2015,4,1), datetime.date(2015,6,30)],
    '3 квартал 2015' : [ datetime.date(2015,7,1), datetime.date(2015,9,30)],
    '4 квартал 2015' : [ datetime.date(2015,10,1), datetime.date(2015,12,31)],
    '1 квартал 2016' : [ datetime.date(2016,1,1), datetime.date(2016,3,31)],
    '2 квартал 2016' : [ datetime.date(2016,4,1), datetime.date(2016,6,30)],
    '3 квартал 2016' : [ datetime.date(2016,7,1), datetime.date(2016,9,30)],
    '4 квартал 2016' : [ datetime.date(2016,10,1), datetime.date(2016,12,31)],
    '1 квартал 2017' : [ datetime.date(2017,1,1), datetime.date(2017,3,31)],
    '2 квартал 2017' : [ datetime.date(2017,4,1), datetime.date(2017,6,30)],
    '3 квартал 2017' : [ datetime.date(2017,7,1), datetime.date(2017,9,30)],
    '4 квартал 2017' : [ datetime.date(2017,10,1), datetime.date(2017,12,31)],
}

result = {
    '1 квартал 2015' : [ 0, 0 ],
    '2 квартал 2015' : [ 0, 0 ],
    '3 квартал 2015' : [ 0, 0 ],
    '4 квартал 2015' : [ 0, 0 ],
    '1 квартал 2016' : [ 0, 0 ],
    '2 квартал 2016' : [ 0, 0 ],
    '3 квартал 2016' : [ 0, 0 ],
    '4 квартал 2016' : [ 0, 0 ],
    '1 квартал 2017' : [ 0, 0 ],
    '2 квартал 2017' : [ 0, 0 ],
    '3 квартал 2017' : [ 0, 0 ],
    '4 квартал 2017' : [ 0, 0 ],

}

# Открываем файл и читаем строчки в нем
fileOpen = open('Gazprom.csv', 'r')
linesFile = fileOpen.readlines()
# print(linesFile)


# для каждой строчки
for line in linesFile:
    values = line.split(';') # разделяем строку по запятым, соответственно по формату
    # print(values)
    name = values[0] # первая колонка - название компании
    # print(name.lower())

    # является ли имя газпром
    if 'газпром' in name.lower(): # lower - переводит в нижний регистр
        datefull = values[1] # вторая колонка - Дата
        income = values[2] # третья колонка - Поступления
        payment = values[3].replace('\n', '') # четвертая колонка - Отчисления + Удаляем знак \n начало новой строки
        # print(payment)
        # print(datefull)

        # дата в виде 01/01/0011:
        # первый способ
        dateSplit = datefull.split('/') # разделяем по слешу 01/01/0011 --> 01 01 0011
        date = datetime.date(int(dateSplit[2]), int(dateSplit[1]), int(dateSplit[0]))
        #print(date)
        # второй способ
        date = datetime.datetime.strptime(datefull, '%d/%m/%Y').date() # Использование Текстового Формата


        # находим к какому кварталу принадлежит ([ключ][значение])
        for qs in quartes:
            if date > quartes[qs] [0] and date <= quartes[qs] [1]:
        # если дата между началом и концом квартала
                # Добавляем сумму
                result[qs] [0] = result[qs] [0] + int(income)
                # Убираем (-) абсолютное значение
                result[qs][1] = result[qs][1] + abs(int(payment))

        # print(result)


#1 Сделать сумму по поступлениям
#2 Сделать сумму по отчислениям, предварительно убрать минус
#3 Вычесть сумму отчислений от сумму поступлений за выбранный квартал для каждого квартала

for quarter in result:
    netCashFlow = result[quarter][0] - result[quarter][1] # вычитаем отчисления из поступлений
    netCashFlowTxt = "{:,}".format(netCashFlow) # форматируем число в формат ХХХ,ХХХ,ХХХХ
    print(quarter + " : " + netCashFlowTxt + '\n')

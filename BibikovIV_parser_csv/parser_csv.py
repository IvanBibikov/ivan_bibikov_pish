# Формат входных данных YEAR;MONTH;DAY;HOUR;MINUTE;TEMPERATURE
# Требования к обработке данных
## Необходимо вывести статистику по каждому месяцу, с учетом исходных данных:
# - среднемесячная температура
# - минимальная температура в текущем месяце
# - максимальная температура в текущем месяце
## Также необходимо вывести статистику за год:
# - среднегодовая температура
# - минимальная температура
# - максимальная температура
import argparse # Импортируем модуль argparse
parser = argparse.ArgumentParser() # Создаём объект parser, который будет отвечать за аргументы командной строки
parser.add_argument("-f", "--file", type=str, help="Введите имя файла *.csv с данными") # Создаём именованный аргумент для имени файла
parser.add_argument("-y", "--year", type=str, help='Введите год в формате "ГГГГ"') # Создаём именованный аргумент для параметра ГОД
parser.add_argument("-m", "--month", type=str, help='Введите месяц от 1 до 12 или от 01 до 12 в зависимости от набора данных') # Создаём именованный аргумент для параметра МЕСЯЦ
args = parser.parse_args() # Создаём объект args. Он будет содержать все принятые агрументы
if args.file == None and args.year == None and args.month == None: # если все аргументы пустые
    parser.print_help() # выводим help
else:
    file_name = args.file
    year_in = args.year
    month_in = args.month
#file_name = input('Введите имя файла: ', ) # Ввод имени файла для обработки
#year_in = input ('Введите год в формате "ГГГГ" -> ', ) 
#month_in = input ('Введите месяц от 1 до 12 или от 01 до 12 в зависимости от набора данных -> ', )
    def make_year_data_set (f_name, year): # функция создания набора данных за выбранный год из файла
        year_data_set = [] # пустой набор данных за год
        try:
            with open (f_name, 'r') as file:
                for line in file: # для каждой строки в файле
                    row = line.strip().split(';') # .strip() - метод строки убирающий лишнии символы  .split() - метод строки разделяющий строку на под-строки и размещающий результат в список                                               
                    for ch in row[-1]: # для каждого символа данных о температуре
                        if ch == '-' or ch.isnumeric(): # проверяем, что в данных о температуре только символ "-" или цифры от 0 до 9
                            temp_data_ok = 1 # если условие выполняется, ставим флаг данные Ok 
                        else:
                            temp_data_ok = 0 # иначе, данные NotOk
                    if temp_data_ok == 0:
                        print (row, 'В строке отсутствуют данные о температуре')
                    if row[0].strip() == year: # проверяем, что год в строке соответствует выбранному году 
                        year_in_data_Ok = 1   # если условие выполняется, ставим флаг "год совпадает" 
                    else:
                        year_in_data_Ok = 0 # иначе, снимаем флаг "год совпадает"
                    if temp_data_ok == 1 and year_in_data_Ok == 1: # если данные о температуре Ok и год совпадает с выбранным
                        year_data_set.append(row) # добавляем строку из файла в набор данных
        except:
            print ('!!!Файл с именем', f_name,'не найден!!!')   
        return year_data_set # набор данных в формате списка строк [[YEAR, MONTH, DAY, HOUR, MINUTE, TEMPERATURE], [],...]
    year_data_set = make_year_data_set (file_name, year_in)
    def calc_year_temp (data_set, year): # функция собработки данных о температуре из набора данных за год
        import math
        i = 0
        year_temp_list = [] # пустой набор температур за год
        try:
            for string in data_set: # для каждой строки в наборе данных  
                row = data_set[i] # выбираем i-й элемент набора данных
                i = i + 1
                year_temp_list.append(int(row[-1])) # добавляем в список значение температуры
            #if not any (year_temp_list): # если список пустой (в статистике нет данных за выбранный год или все данные о температуре за выбранный год не корректны)
                #output_string = f"В {year} : \nМинимальная температура: н/д \nМаксимальная температура: н/д \nСредняя температура: н/д"
            #else:
            min_temp = min (year_temp_list) # выбираем минимальное значение температуры из набора данных
            max_temp = max (year_temp_list) # выбираем максимальное значение температуры из набора данных
            avr_temp = round (sum (year_temp_list)/len (year_temp_list), 2) # рассчитываем среднее значение температуры из набора данных (с округлением до 2-х знаков после запятой)
            output_string = f"В {year} : \nМинимальная температура: {min_temp} \nМаксимальная температура: {max_temp} \nСредняя температура: {avr_temp}"
            return print (output_string)
        except:
            output_string = f"В наборе нет данных о температуре за {year} год: \nМинимальная температура: н/д \nМаксимальная температура: н/д \nСредняя температура: н/д"
            return print (output_string)
    calc_year_temp (year_data_set, year_in)
    def calc_month_temp (data_set, year, month): # функция собработки данных о температуре за выбранный месяц из набора данных за год
        import math
        i = 0
        month_temp_list = [] # пустой набор температур за месяц
        try:
            for string in data_set: # для каждой строки в наборе данных  
                row = data_set[i] # выбираем i-й элемент набора данных
                i = i + 1
                if row[1].strip () == month: # проверяем, что месяц в строке соответствует выбранному месяцу .strip() - метод строки убирающий лишнии символы         
                    month_temp_list.append(int(row[-1])) # добавляем в список значение температуры           
            #if not any (month_temp_list):  # если список пустой (в статистике нет данных за выбранный месяц или все данные о температуре за выбранный месяц не корректны)      
            #output_string = f"В {month} месяце {year}: \nМинимальная температура: н/д \nМаксимальная температура: н/д \nСредняя температура: н/д"
            #else:
            min_temp = min (month_temp_list) # выбираем минимальное значение температуры из набора данных
            max_temp = max (month_temp_list) # выбираем максимальное значение температуры из набора данных
            avr_temp = round (sum (month_temp_list)/len (month_temp_list), 2) # рассчитываем среднее значение температуры из набора данных (с округлением до 2-х знаков после запятой)
            output_string = f"В {month} месяце {year}: \nМинимальная температура: {min_temp} \nМаксимальная температура: {max_temp} \nСредняя температура: {avr_temp}"
            return print (output_string)
        except:
            output_string = f"В наборе нет данных о температуре за {month} месяц {year} года: \nМинимальная температура: н/д \nМаксимальная температура: н/д \nСредняя температура: н/д"
            return print (output_string)
    calc_month_temp (year_data_set, year_in, month_in)
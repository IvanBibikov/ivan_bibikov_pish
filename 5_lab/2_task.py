# Задание 2: Извлечение email-адресов
# Дана строка, содержащая текст с email-адресами:
# text = "Контакты: ivanov@example.com, petrow@work.net, sid@mail.ru"
# Напишите программу, которая:
# Извлечет все email-адреса из строки.
# Сохранит их в список и выведет результат.
text = "Контакты: ivanov@example.com, petrow@work.net, sid@mail.ru"
def string_split (string): # функция парсинга строки
    temp_list = string.split (':') # преобразуем строку в список строк по разделителю ':'
    for string in temp_list: # для каждой строки в списке  
        email_list = string.split (',') # преобразуем строку в список по разделителю ',', помещаем результаты в список
    print ("Список email: ", email_list)
    return 
string_split (text)
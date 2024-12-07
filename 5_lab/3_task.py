# Задание 3: Подсчет количества слов
# Дана строка, содержащая предложение:
# sentence = "Python is a powerful and easy-to-learn programming language."
# Напишите программу, которая:
# Разделит предложение на отдельные слова.
# Подсчитает, сколько слов в предложении.
sentence = "Python is a powerful and easy-to-learn programming language." # исходная строка
def w_numb_counter (string): # функция подсчёта количества слов в строке 
    word_list = string.split () # преобразуем строку в список
    print (word_list)
    print ("Слов в предложении:", len (word_list)) # подсчитываем кол-во элементов в списке
    return
w_numb_counter (sentence)
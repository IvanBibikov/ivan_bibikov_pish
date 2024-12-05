# Задача 1: Уникальные элементы
# Условие: Дана строка, содержащая несколько слов.
# Найдите все уникальные слова в строке и выведите их в алфавитном порядке.
# sentence = "apple banana apple orange banana kiwi"
# Вывод: ['apple', 'banana', 'kiwi', 'orange']
sentence = "apple banana apple orange banana kiwi" # исходная строка
print ("Исходная строка", sentence)
def sort_list_from_string (string): # функция поиска уникальных слов в строке и упорядочения в алфавитном порядке
    my_set = set (string.split (' ')) # преобразуем строку в множество
    unsort_list = list (my_set) # преобразуем множество в список
    sort_list = sorted (unsort_list) # сортируем список
    return print ("Отсортированный список", sort_list) # выводим отсортированный список
sort_list_from_string (sentence)
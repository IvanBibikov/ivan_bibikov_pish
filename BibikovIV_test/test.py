# Считать массив из 10 элементов и выполнить циклический сдвиг ВПРАВО на 1.
# Входные данные
# 4 -5 3 10 -4 -6 8 -10 1 0
# Результат работы
# 0 4 -5 3 10 -4 -6 8 -10 1
input_str = input ('Введите массив из 10 элементов разделив их пробелами-> ') # исходные данные
shift = 1 # заданный сдвиг массива
array = input_str.split (' ') # преобразуем строку в список строк по разделителю ' ' (пробел)
def shift_array (list, step): # функция циклического сдвига массива list на заданное кол-во позиций step
    for i in range (step): # в диапазоне от i до заданного значения сдвига
        list.insert (0, list.pop()) # сдвигаем список направо (извлекаем элемент с конца списка и вставляем в начало списка)
print ("Исходный массив: ", array) # выводим исходный массив
print ("Сдвиг: ", shift) # выводим заданный сдвиг массива
shift_array (array, shift) # возвращаем результат функции сдвига массива. В качестве аргументов исходный массив и заданный сдвиг
print ("Массив со сдвигом вправо на 1 позицию: ", array) # выводим массив со сдвигом
# 1. Циклический сдвиг массива
# Дан список чисел. Требуется выполнить циклический сдвиг на заданное число позиций.
# Элементы, смещаемые за пределы массива, должны "переходить" в начало.
# Вход array = [1, 2, 3, 4, 5]
# Выход [4, 5, 1, 2, 3]
array = [1, 2, 3, 4, 5] # исходный список
shift = 2 # заданный сдвиг списка
def shift_list (list, step): # функция циклического сдвига списка list на заданное кол-во позиций step
    if step < 0: # если задан сдвиг на отрицательное кол-во позиций
        step = abs (step) # берём значение сдвига по модулю
        for i in range (step): # в диапазоне от i до заданного значения сдвига
            list.append (list.pop (0)) # сдвигаем список налево (извлекаем первый элемент списка и добавлем его в конец) 
    else: # если задан сдвиг на положительное кол-во позиций или 0
        for i in range (step): # в диапазоне от i до заданного значения сдвига
            list.insert (0, list.pop()) # сдвигаем список направо (извлекаем элемент с конца списка и вставляем в начало списка)
print ("Исходный список", array) # выводим исходный список
print ("Сдвиг", shift) # выводим заданный сдвиг списка
shift_list (array, shift) # возвращаем результат функции сдвига списка. В качестве аргументов исходный список и заданный сдвиг
print ("Список со сдвигом", array) # выводим список со сдвигом
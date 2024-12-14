# Задание 2: Фильтрация чётных чисел
# Описание: Дан список целых чисел. Нужно отфильтровать из списка только чётные числа.
# Используйте функцию filter() и лямбда-выражение для выбора чётных чисел.
# numbers = [10, 15, 20, 25, 30]
# Ожидаемый результат: [10, 20, 30]
numbers = [10, 15, 20, 25, 30] # исходный список
print ("Исходный список", numbers)
evens = list(filter(lambda x: x % 2 == 0, numbers)) # выбираем из исходного списка чётные элементы (проверем, что результат деления без остатка на 2 равен 0) 
print ("Список чётных чисел", evens)
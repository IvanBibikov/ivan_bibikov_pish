# Задача 4: Словарь квадратов
# Условие: Дано целое число n. 
# Создайте словарь, где ключами будут числа от 1 до n, а значениями — их квадраты.
# n = 5
# Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5 # исходное число
def squares (n): # функция создания словаря квадратов числа
     squares_dict = {} # объявляем словарь квадратов числа
     for i in range (n): # в диапазоне от i до n
          squares_dict [i+1] = (i+1)**2 # заполняем словарь квадратами чисел от 1 до n
     return print ("Словарь квадратов",squares_dict)
squares (n)
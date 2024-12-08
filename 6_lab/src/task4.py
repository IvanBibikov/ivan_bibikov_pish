# 4. Составить функцию, которая определяет сумму цифр в числе
a = abs(int(input("Введите целое число : "), base=10)) # переводим строку в целое число
def n_of_d(a): # функция определение кол-ва разрядов в ведённом числе
    numofdigit = 1
    div = int (a/10)
    while div > 0:
        div = int (div/10)
        numofdigit = numofdigit + 1
    return numofdigit 
print ("Количество разрядов в числе :", n_of_d(a))
print ("Цифры числа в порядке возрастания слева направо:")
print ("Разряд  Цифра  Сумма")
num_of_dig = n_of_d(a) # возщвращаем из функции кол-во разрядов в ведённом числе
def sum_of_digit (a, num_of_dig): # функция определение суммы всех цифр в ведённом числе
    summ = 0
    i = 1
    while num_of_dig  > 0: # пока не пройдём все разряды от старшего к младшему
        digit = int ((a) / 10**(num_of_dig - 1)) # значение цифры в текущем разряде
        summ = summ + digit
        print (i, "     ", digit, "     ", summ)  
        a = a - digit * 10 ** (num_of_dig-1) # отбрасываем в ведённом числе старший разряд
        num_of_dig = num_of_dig - 1
        i = i + 1
    return summ
print ("Сумма цифр", sum_of_digit(a, num_of_dig)) # возвращаем из функции сумму цифр в ведённом числе
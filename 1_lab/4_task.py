#Ввести целое число и определить, верно ли, что все его цифры расположены в порядке возрастания (слева направо)
a = abs(int(input("Введите целое число : "), base=10)) # переводим строку в целое число
numofdigit = 1 # кол-во разрядов в введённом числе
leftdigit = 0 # значение цифры слева от текущего разряда
# digit - значение цифры в текущем разряде
i = 1
div = int (a/10)
while div > 0: # определение кол-ва разрядов в ведённом числе
    numofdigit = numofdigit + 1
    div = int (div/10)
print ("Количество разрядов в числе :", numofdigit)
print ("Цифры числа в порядке возрастания слева направо:")
while numofdigit > 0: # цикл проверки что цифра в левом разряде меньше или равна цифре в правом разряде
    digit = int ((a) / 10**(numofdigit-1))
    if leftdigit <= digit: # пока цифра в левом разряде меньше или равна цифре в правом разряде выводим на каждом шаге цикла номер разряда и цифру в этом разряде
        print ("Разряд", i, ":", digit)
        leftdigit = digit
        a = a - digit * 10 ** (numofdigit-1)
        numofdigit = numofdigit - 1
        i = i + 1
    else: # Иначе, выводин номер разряда, в котором цифра больше чем в разряде слева
        numofdigit = 0
        print ("Разряд", i, ":","Нет")
# 2. Составить функцию, которая опеределяте наибольший общий делитель двух чисел nod(a, b)
a = int (input("Введите число a: "))
b = int (input("Введите число b: "))
def nod(a, b):
    while a != 0 and b !=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
print (nod (a, b))
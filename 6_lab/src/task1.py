# 1. Описать функцию вычисления:
# f(x)=x^2 if [-2 <= x < 2]
# f(x)=x^2+4x+5 if [x >= 2]
# f(x)=4 if [x < -2]
x = float (input("Введите число x: "))
def function_1(x):
    return x**2
def function_2(x):
    return x**2 + 4*x + 5
def result (function_1, function_2):
   if x >= -2 and x < 2:
       return function_1(x)
   else:
       if x >= 2:
            return function_2(x)
   if x < -2:
    return 4
print (result (function_1, function_2))
# Задание 12 из ЕГЭ-2025 профиль [https://math-ege.sdamgia.ru/test?id=77409203&ysclid=mgqhp19pfb346776915]
# Найдите наименьшее значение функции y=9x-9ln(x+11)+7 на отрезке [-10,5;0] 
import numpy as np
import math
def f(x):
    "Исходная функция y=9x-9ln(x+11)+7"
    return 9*x-9*math.log(x+11)+7
def f_derivative(x):
    "Производная функции"
    return 3*x*2-6*x
def f_second_derivate(x):
    "Вторая производная функции"
    return 6*x-6

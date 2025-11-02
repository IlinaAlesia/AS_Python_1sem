# 4 задание Ильина
import math
n = int(input("Натуральное число n: "))
sum = 0
print("Вычисление суммы:")
for x in range(1, n+1):
    y= 1/math.sin(x)
    sum += y
    print ("1/sin(" + str(x) + ")= " + str(round(y,6)))
print("\nИтоговая сумма: {}".format(round(sum,6)))


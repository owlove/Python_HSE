print("Задание № 1")
from math import log

while True:
    try:
        x = float(input("Пожалуйста, введите вещественное число Х: "))
        if x != 0:
            break
    except:
        print("Вы допустили ошибку при вводе вещественного числа")

while True:
    try:
        lnNum = int(input("Пожалуйста, введите количество натуральных логарифмов: "))
        if lnNum != 0:
            break
    except:
        print("Вы допустили ошибку при вводе количества натуральных логарифмов")

for i in range(lnNum):
    try:
        x = log(x)
    except:
        print("Ой-ой, что-то пошло не так")
print("S = ", x)



print("Задание № 2")
num_list = []
n_count = 0

while True:
    try:
        n = int(input("Пожалуйста, введите количество элементов последовательности: "))
        break
    except:
        print("Вы допустили ошибку при вводе целого числа")


while True and n_count != n:
    try:
        elem = int(input("Пожалуйста, введите целое число последовательности: "))
        num_list.append(elem)
        n_count += 1
    except:
        print("Вы допустили ошибку при вводе целого числа")

print("Получившаяся последовательность: ", num_list)

sum_buf = 0 # временный счетчик для 3х элементов
sum = 0 # количество подходящих последовательностей
el = 0

while el < len(num_list) - 1:
    if (num_list[el + 1] > num_list[el]) and sum_buf == 1:
        sum += 1
        sum_buf += 1
    elif (num_list[el + 1] > num_list[el]) :
        sum_buf += 1
    elif (num_list[el + 1] < num_list[el]):
        sum_buf = 0
    el += 1

print("Количество цепочек из 3х и более возрастающих чисел = ", sum)

# 5, 7, 3, -5, 7, 8, 11, 3, 9







# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math


def intNum(number):
    while not number.isdigit():
        print('Вы ввели не то что я просил!')
        number = input('Введите целое положительное число: ')
    return int(number)

def findMultArray(number):
    array = [0] * number
    i = 1
    while i <= number:
        array[i-1] = math.prod(range(1,i+1,1))
        i += 1
    return array

print(findMultArray(intNum(input('Введите число: '))))
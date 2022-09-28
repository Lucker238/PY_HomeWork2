#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# C:\Users\maxim.s.EWGH\Desktop\Geekbrains\Python\HW2\file.txt

import random

def inpt(N):
    check = True
    while check:
        if N.isdigit():
            check = False
        else:
            print('N должно быть числом')
            N = input('Введите N: ')
    return int(N)

def makeList(N):
    array = []
    for i in range(N):
        array.append(random.randint(-N,N))
    return array

def findProd(array):
    file = open(r'C:\Users\maxim.s.EWGH\Desktop\Geekbrains\Python\HW2\file.txt', 'r')
    result = 1
    try:
        for index in file:
            result *= arr[int(index)-1]
            print(f'На позиции {int(index)} находится элемент {arr[int(index)-1]}')
        return result
    except (IndexError):
        return f'Индекс {int(index)} в file.txt больше чем длина списка. Операция прервана!'


arr = makeList(inpt('Введите N:'))
print(arr)
print(findProd(arr))



#5. Реализуйте алгоритм перемешивания списка.

import random

def createList():
    N = input('Введите длину списка: ')
    check = True
    array = []
    while check:
        if N.isdigit():
            for i in range(1, int(N)+1):
                array.append(i)
            check = False
        else:
            print('Вы ввели что то не то')
            N = input('Введите длину списка: ')
    return array

list = createList()
print(list)
random.shuffle(list)
print(list)
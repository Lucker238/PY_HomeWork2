# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def intNumber(smth):
    check = True
    number = 0
    while check:
        try:
            number = float(smth)
            check = False
        except ValueError:
            print('Вы ввели не число!')
            smth = input('Введите число: ')
    return number


def numbersSum(number):
    sum = 0
    for i in str(number):
        if i.isdigit():
            sum += int(i)
    return sum

print(numbersSum(intNumber(input('Введите число: '))))
# Задача 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

from os import system

system ('cls')

import Base

number= Base.check_number_more(0,'Введите число: ', 'Вы ввели не правильное число, введите его заново: ')

number = int(number)

def binary_numbers (number, out:str='0'):
    out = str(number%2)+out
    if number == 1:
        return out[:-1]
    else:
        return binary_numbers (number//2,out)
    
    
print (f'{number} -> {binary_numbers(number)}')

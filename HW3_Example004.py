# Задача 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

from os import system

system ('cls')

def binary_numbers (number, out:str='0'):
    out = out+str(number%2) 
    if number == 1:
        return out[:0:-1]
    else:
        return binary_numbers (number//2,out)
    
    
a=binary_numbers(46)
print (a)

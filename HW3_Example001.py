## Задача №1
# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from operator import index
from os import system
system ('cls')
import Base

reng_= Base.check_number_more(0,'Введите размер массива: ', 'Вы ввели не правильное число, введите его заново: ')



list_= Base.random_list_number(int(reng_),1,20)


def sum_not_even (list_:list):
    sum_=0
    new_list =[]
    for number in list_:
        if list_.index(number)%2==1:
            new_list.append(number)
            sum_+=number
    return sum_, new_list

sum_number, new_list = sum_not_even(list_)

print ( f'{list_} -> на нечётных позициях элементы {new_list}  ответ: {sum_number}')
# Задача 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from os import system
system ('cls')

my_list = [4.01, 5.1, 8.2444, 6.98]



def list_diff (my_list:list):
    def isolating_fractional(number):
        number=str(number)
        return float('0'+number[number.find('.'):])

    new_list = []

    for number in my_list:
        new_list.append(isolating_fractional(number))

    return round((max (new_list)-min (new_list)),12)


print(f'{my_list} => {list_diff (my_list)}')
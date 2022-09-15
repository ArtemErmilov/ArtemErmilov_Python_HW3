# Задча 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


from os import system
system ('cls')
import Base

reng_= Base.check_number_more(1,'Введите размер массива: ', 'Вы ввели не правильное число, введите его заново: ')


my_list= Base.random_list_number(int(reng_),1,5)


def mul_list (my_list:list):
    new_list=[]
    for i in range(0,len(my_list)//2+len(my_list)%2):
        new_list.append(my_list[i]*my_list[-(i+1)])
    return new_list

print (f'{my_list} => {mul_list (my_list)}')

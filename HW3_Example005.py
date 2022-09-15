# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи

from os import system
system ('cls')
import Base


number = Base.check_number_more(1,'Введите число больше 1: ', 'Вы ввели не правильно число, введите его заново и больше 1: ')

def fibonacy (n):
    list1=[]
    for i in range(0,n+1):
        if i ==0:
            list1.append(0)
        if i==1 or i ==2:
            list1.append(1)
        elif i>2: 
            list1.append(list1[(i-1)]+list1[(i-2)])

    list2 =[]
    for i in range(1,n+1):
       list2.append((-1)**(i+1)*list1[i])
       
    list2.reverse()
    return list2+list1

print (f'Для K={number} список Негафибоначчи будет выглядеть так: {fibonacy(int(number))}')




from random import randint, random


def check_number ( text_in:str, text_breac:str): 
    '''
    Проверка, является ли введённые данные числом. 
    Если нет то повторяется запрос заново.
    text_in - техт запроса в консоли
    text_breac - техт вторичного запроса, при неправильном вводе числа
    '''
    number_in = input(text_in)
    number = number_in.replace('-','0')
    number = number.replace('.','0')

    while number.isdigit() == False or number_in.count('-')>1 or (number_in.count('-')==1 and number_in[0]!='-') or number_in.count('.')>1:
        number_in = input(text_breac)
        number = number_in.replace('-','0')
        number = number.replace('.','0')
    
    return number


def check_number_more ( num:float, text_in:str, text_breac:str): 
    '''
    Проверка, является ли введённые данные числом. И это число больше num
    Если нет то повторяется запрос заново.
    text_in - техт запроса в консоли
    text_breac - техт вторичного запроса, при неправильном вводе числа
    '''
    number_in = input(text_in)
    number = number_in.replace('-','0')
    number = number.replace('.','0')

    while number.isdigit() == False or number_in.count('-')>1 or (number_in.count('-')==1 and number_in[0]!='-') or number_in.count('.')>1 or float(number_in)<num:
        number_in = input(text_breac)
        number = number_in.replace('-','0')
        number = number.replace('.','0')
    
    return number


def random_list_number ( rendg_:int,min_:int, max_:int):
    '''
    Заполнение списка случайными числами
    rendg_ - длина списка
    min_ - минимальное значение случайной величины
    max_ - максимальное значение случайной величины

    '''
    list_my = []

    for i in range(0,rendg_):
        list_my.append(randint(min_,max_))
    
    return list_my
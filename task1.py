# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

MIN_NUMBER = -1000
MAX_NUMBER = 1000
COUNT_STR = 10
user_file_name = 'user_file.txt'

def random_dual(count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        while count > 0:
            number1 = random.randint(MIN_NUMBER, MAX_NUMBER) 
            number2 = random.uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{number1} | {round(number2,2)}\n')
            count -= 1 
  
random_dual(COUNT_STR, user_file_name)    
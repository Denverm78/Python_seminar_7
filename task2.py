# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random

NUMBER_NAME = 10

def create_name():
    LIST1 = ['А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
    LIST2 = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
    MIN = 4
    MAX = 7
    name = ''
    for i in range(random.randint(MIN-2, MAX-2)):
        num_list = random.randint(1,2)
        if num_list == 1:
            name += random.choice(LIST1)
            if len(name) == MAX:
                break
            name += random.choice(LIST2)
        else:
            name += random.choice(LIST2)
            if len(name) == MAX:
                break
            name += random.choice(LIST1)
    return name
    
def gen_name(number):
    with open('name_list.txt', 'a', encoding='utf-8') as f:
        for _ in range(number):
            f.write(f'{create_name().capitalize()}\n')
            
gen_name(NUMBER_NAME)
# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import random
import os

def create_files(dict_extan, min_name=6, max_name=30, min_size=256, max_size=4096):
    for key in dict_extan:
        for _ in range(dict_extan[key]):
            LIST1 = 'EYUIOA'
            LIST2 = 'QWRTPSDFGHJKLZXCVBNM'
            MIN = 6
            MAX = 30
            name = ''
                                
            for i in range(random.randint(MIN/2, MAX/2)):
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
            cwd = os.getcwd()
            name = cwd + '\\' + 'date2' + '\\' + name.lower() + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                date = bytes(random.randint(0, 255) for i in range(random.randint(min_size, max_size)))
                new_f.write(str(date))
        

user_dict = {'txt':5, 'doc':3}
create_files(user_dict)
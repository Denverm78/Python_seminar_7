# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
import os
from pathlib import Path

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
            name = name.lower() + '.' + key
            if Path(name).is_file():
                continue
            # cwd = os.getcwd()
            # name = cwd + '\\' + 'date2' + '\\' + name.lower() + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                date = bytes(random.randint(0, 255) for i in range(random.randint(min_size, max_size)))
                new_f.write(str(date))
        
def dir(user_path):
    if isinstance(user_path, str): # Проверяем является ли user_path строкой
        work_path = Path(user_path)
    else:
        work_path = user_path
    if not work_path.is_dir():
        work_path.mkdir(parents=True)
    os.chdir(work_path) # Меняем рабочю папку на work_path
    create_files(user_dict)



if __name__ == '__main__': 
    user_dict = {'txt':5, 'doc':3}
    dir('date3')
    # dir('c:\\1\\2')
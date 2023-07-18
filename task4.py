# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random
import os

def create_files(extension='', min_name=6, max_name=30, min_size=256, max_size=4096, number_files=42):
    for _ in range(number_files):
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
        name = cwd + '\\' + 'date' + '\\' + name.lower() + '.' + extension
        print(name)
        with open(name, 'w', encoding='utf-8') as new_f:
            date = bytes(random.randint(0, 255) for i in range(random.randint(min_size, max_size)))
            new_f.write(str(date))
        

create_files('dwg')

# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def gen_file():
    with (
        open('name_list.txt', 'r', encoding='utf-8') as name,
        open('user_file.txt', 'r', encoding='utf-8') as mult,
        open('result.txt', 'w', encoding='utf-8') as res
    ):
        while user_file := mult.readline():
            a, b = user_file.split(' | ')
            mult_f = int(a) * float(b)
            if mult_f < 0:
                name_f = name.readline().lower()
                res.write(f'{name_f[:-1], abs(mult_f)} \n')
            else:
                name_f = name.readline().upper()
                res.write(f'{name_f[:-1], int(mult_f)} \n')

gen_file()
                
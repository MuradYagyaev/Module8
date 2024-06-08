# Модуль №8. Исключения. Try и Except

def add_everything_up(a, b):
    try:
        return round(a + b, 3)
        # return f'{a + b:7.3f}'
    except TypeError:
        return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456,7))



# Модуль №8. Исключения. Создание исключений.

class MyException1(Exception):
    def __init__(self, message, extra_info=None):
        self.message = message
        self.extra_info = extra_info

class MyException2(Exception):
    def __init__(self, message, extra_info=None):
        self.message = message
        self.extra_info = extra_info


def f1(age, name):
    if age < 18:
        raise MyException1('Вам нет 18 лет, доступ ограничен', {'Name': name, 'Age': age})
    elif name == 'Anonymous':
        raise MyException2('Для продолжения необходимо представиться')
    else:
        print(f'Приветствуем вас {name} на нашем закрытом чате')

def f2(age, name='Anonymous'):
    try:
        f1(age, name)
    except MyException1 as m1:
        print(f'Ошибка входа: {m1.message}, дополнительная инфа: {m1.extra_info}')
        raise
    except MyException2 as m2:
        print(f'Ошибка входа: {m2.message}')
        raise
    else:
        print('Приятного времяпрепровождения')


try:
    f2(27, 'Иван')
except (MyException1, MyException2):
    print('Ошибка передана на уровень ниже, и обработана')
print('Программа продожает работать')

try:
    f2(28)
except (MyException1, MyException2):
    print('Ошибка передана на уровень ниже, и обработана')
print('Программа продожает работать')

try:
    f2(12, 'Ваня')
except (MyException1, MyException2):
    print('Ошибка передана на уровень ниже, и обработана')
print('Программа продожает работать')

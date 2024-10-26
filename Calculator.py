import math
import time


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'Ошибка: На ноль делить нельзя!'
    return a / b


def integer_divide(a, b):
    if b == 0:
        return 'Ошибка: На ноль делить нельзя!'
    return a // b


def taking_the_remainder(a, b):
    if b == 0:
        return 'Ошибка: На ноль делить нельзя!'
    return a % b


def stepen(a, b):
    return a**b


def root(a):
    a = float(a)
    if a < 0:
        return 'Ошибка: Число под корнем является отрицательным!'
    elif a == 0:
        return 0
    return a ** 0.5


def system_number(a, base):
    try:
        return int(str(a), base)
    except ValueError:
        return 'Ошибка: Неверно введёные данные!'


def number_analyzator(number):
    number = int(number)
    final_analyze = dict()
    z = [int(i) for i in str(abs(number))]
    zcount = len(z)
    chastota = {i: z.count(i) for i in set(z)}
    if number % 2 == 0:
        chetnoe = 'Да'
    else:
        chetnoe = 'Нет'
    summa = sum(int(i) for i in str(number))
    flag = True
    deliteli = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            deliteli.append(i)
            if i != number // i:
                deliteli.append(number // i)
    deliteli.sort()
    kvadrat = None
    for i in range(1, int(math.sqrt(number)) + 1):
        if i * i == number:
            kvadrat = i
            break
    number = int(number)
    cub = None
    for i in range(1, int(number ** (1 / 3)) + 2):
        if i * i * i == number:
            cub = i
            break
    final_analyze = {
        "Количество разрядов": zcount,
        "Частота цифр": chastota,
        "Четное": chetnoe,
        "Сумма цифр": summa,
        "Простое": "Да" if flag else 'Нет',
        "Делители": deliteli if not flag else [],
        "Полный квадрат": kvadrat,
        "Полный куб": cub
    }
    return final_analyze


def main():
    print('Привет. Это калькулятор.')
    time.sleep(0.5)
    print('Он умеет выполнять различные операции и анализы чисел.')
    time.sleep(0.5)
    print('Список операций, которые есть в калькуляторе:')
    time.sleep(1.2)
    print('1. Сложение (+)')
    time.sleep(0.08)
    print('2. Вычитание (-)')
    time.sleep(0.08)
    print('3. Умножение (*)')
    time.sleep(0.08)
    print('4. Деление (/)')
    time.sleep(0.08)
    print('5. Целочисленное деление (//)')
    time.sleep(0.08)
    print('6. Взятие остатка (%)')
    time.sleep(0.08)
    print('7. Возведение в степень (**)')
    time.sleep(0.08)
    print('8. Квадратный корень (sqr)')
    time.sleep(0.08)
    print('9. Перевод из любой системы счисления в десятичную (systems)')
    time.sleep(0.08)
    print('10. Анализ числа (analyze)')
    time.sleep(1)

    while True:
        try:
            goida = input("Введите операцию которую хотите воспроизвести:"
                          "+, -, *, /, //, %, **, sqr, systems, analyze").strip().lower()
            if goida in ["+", "-", "*", "/", "//", "%", "**"]:
                zov = float(input('Введите первое число: '))
                svo = float(input('Введите второе число: '))
                if goida == '+':
                    result = add(zov, svo)
                elif goida == '-':
                    result = subtract(zov, svo)
                elif goida == '*':
                    result = multiply(zov, svo)
                elif goida == '/':
                    result = divide(zov, svo)
                elif goida == '//':
                    result = integer_divide(zov, svo)
                elif goida == '%':
                    result = taking_the_remainder(zov, svo)
                elif goida == '**':
                    result = stepen(zov, svo)
                print(f'Результат: {result}')
            elif goida == 'sqr':
                number = input('Введите число: ')
                result = root(number)
                print(f'Результат: {result}')
            elif goida == 'systems':
                a = input('Введите число: ')
                base = int(input("Введите систему в которой дано это число: "))
                result = system_number(a, base)
                print(f'Результат: {result}')
            elif goida == 'analyze':
                number = input('Введите число: ')
                final_analyze = number_analyzator(number)
                print("Анализ числа:")
                for key, value in final_analyze.items():
                    print(f"{key}: {value}")
            else:
                print('Данные введены некорректно')
        except ValueError:
            print('Ошибка при выполнении программы! Данные введены неверно!')

        repeator = input('Хотите воспользоваться калькулятором снова? Если да напишите "да": ').strip().lower()
        if repeator != 'да':
            print('До свидания!')
            break


if __name__ == "__main__":
    main()

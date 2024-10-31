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


def trigonometry(mode, operation, putin):
    def radians_to_degrees(radians):
        return math.degrees(radians)

    def degrees_to_radians(degrees):
        return math.radians(degrees)

    if mode == 'degrees':
        putin = degrees_to_radians(putin)

    if operation == 'sin':
        result = math.sin(putin)
    elif operation == 'cos':
        result = math.cos(putin)
    elif operation == 'tan':
        result = math.tan(putin)
    elif operation == 'asin':
        result = math.asin(putin)
        if mode == 'degrees':
            result = radians_to_degrees(result)
    elif operation == 'acos':
        result = math.acos(putin)
        if mode == 'degrees':
            result = radians_to_degrees(result)
    elif operation == 'atan':
        result = math.atan(putin)
        if mode == 'degrees':
            result = radians_to_degrees(result)
    else:
        raise ValueError("Неверная операция")

    return round(result, 15)


def slow_print(text, char_delay=0.008, line_delay=0.85):
    for line in text:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)


def main():
    intro_text = [
        'Привет. Это калькулятор.',
        'Он умеет выполнять различные операции и анализы чисел.',
        'Список операций, которые есть в калькуляторе:',
        '1. Сложение (+)',
        '2. Вычитание (-)',
        '3. Умножение (*)',
        '4. Деление (/)',
        '5. Целочисленное деление (//)',
        '6. Взятие остатка (%)',
        '7. Возведение в степень (**)',
        '8. Квадратный корень (sqr)',
        '9. Перевод из любой системы счисления в десятичную (systems)',
        '10. Анализ числа (analyze)',
        '11) Тригонометрические функции (trigon)'
    ]

    slow_print(intro_text)

    while True:
        try:
            operation_prompt = [
                "Введите операцию которую хотите воспроизвести:"
                "+, -, *, /, //, %, **, sqr, systems, analyze, trigon, !help"
            ]
            slow_print(operation_prompt)
            goida = input().strip().lower()
            
            if goida == '!help':
                help_text = [
                    "Помощь по использованию калькулятора:",
                    "1) Сложение: вводится число a, затем число b, после выводится сумма a + b.",
                    "2) Вычитание: вводится число a, затем число b, после выводится разность a - b.",
                    "3) Умножение: вводится число a, затем число b, после выводится произведение a * b.",
                    "4) Деление: вводится число a, затем число b, после выводится частное a / b.",
                    "5) Целочисленное деление: вводится число a, затем число b, после выводится"
                    "целая часть от деления a // b.",
                    "6) Взятие остатка: вводится число a, затем число b, после выводится остаток от деления a % b.",
                    "7) Возведение в степень: вводится число a, затем число b, после выводится результат a ** b.",
                    "8) Квадратный корень: вводится число a, после выводится квадратный корень из a.",
                    "9) Перевод из любой системы счисления в десятичную: вводится число a и его основание"
                    "системы счисления, после выводится число в десятичной системе.",
                    "10) Анализ числа: вводится число a, после выводится анализ числа, включая количество разрядов,"
                    "частоту цифр, четность, сумму цифр, простоту, делители, полный квадрат и полный куб.",
                    "11) Тригонометрические функции: выбирается режим (radians/degrees),"
                    "затем операция (sin, cos, tan, asin, acos, atan) и число, после выводится результат."
                ]
                slow_print(help_text)
                continue

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
            elif goida == 'trigon':
                trigon_text = [
                    'Доступные тригонометрические функции:',
                    '1) Sinus (sin)',
                    '2) Cosinus (cos)',
                    '3) Tangens (tan)',
                    '4) ArcSinus (asin)',
                    '5) ArcCosinus (acos)',
                    '6) ArcTangens (atan)'
                ]
                slow_print(trigon_text)
                while True:
                    mode = input('Выберите режим подсчёта: radians/degrees')
                    if mode not in ['radians', 'degrees']:
                        print("Неверный режим. Попробуйте снова.")
                        continue
                    time.sleep(0.5)
                    operation = input("Введите операцию: ").strip().lower()
                    if operation not in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']:
                        print("Неверная операция. Попробуйте снова.")
                        continue
                    try:
                        putin = float(input(f"Введите число ({mode}): "))
                    except ValueError:
                        print("Неверный ввод. Пожалуйста, введите число.")
                        continue
                    if operation == 'sin':
                        result = trigonometry(mode, operation, putin)
                    elif operation == 'cos':
                        result = trigonometry(mode, operation, putin)
                    elif operation == 'tan':
                        result = trigonometry(mode, operation, putin)
                    elif operation == 'asin':
                        result = trigonometry(mode, operation, putin)
                    elif operation == 'acos':
                        result = trigonometry(mode, operation, putin)
                    elif operation == 'atan':
                        result = trigonometry(mode, operation, putin)
                    print(f"Результат: {result}")
                    break
            else:
                print('Данные введены некорректно')
        except ValueError:
            error_text = ["Ошибка при выполнении программы! Данные введены неверно!"]
            slow_print(error_text)

        repeator = ["Хотите воспользоваться калькулятором снова? Если да напишите 'да':"]
        slow_print(repeator)
        repeator = input().strip().lower()
        if repeator != 'да':
            print('До свидания!')
            break


if __name__ == "__main__":
    main()

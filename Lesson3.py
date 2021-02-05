import string


def division(number1, number2):
    """Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
    try:
        return float(number1)/float(number2)
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    except ValueError:
        print("Ошибка в вводе переменных")


def user_info_print(name="", surname="", year=0, city="", email="", phone=""):
    """Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
    рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой."""
    print(name, surname, year, city, email, phone)


def sum_of_max_two(number1, number2, number3):
    """
    Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
    аргументов.
    """
    try:
        numbers = [number1, number2, number3]
        first_number = max(numbers)
        numbers.remove(first_number)
        return first_number + max(numbers)
    except TypeError:
        print("Ошибка в вводе переменных")


def number_in_power(number, power):
    """Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
    возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
    необходимо обойтись без встроенной функции возведения числа в степень."""
    try:
        number = int(number)
        power = int(power)
        if number < 0 or power > 0:
            raise TypeError
        return 1 / (number ** abs(power))
    except TypeError:
        print("Ошибка в вводе переменных")


def number_in_power_2(number, power):
    try:
        number = int(number)
        power = int(power)
        result = 1.0
        if number < 0 or power > 0:
            raise TypeError
        for _ in range(abs(power)):
            result *= number
        return 1 / result
    except TypeError:
        print("Ошибка в вводе переменных")


def sum_with_special_symbol():
    """Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
    сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
    введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
    выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
    сумму этих чисел к полученной ранее сумме и после этого завершить программу."""
    flag = True
    result = 0
    while flag:
        numbers = input("Введите числа через пробел. Для выхода из программы нажмите q").split()
        for number in numbers:
            try:
                result += float(number)
            except ValueError:
                if number == 'q':
                    flag = False
                    break
        print(f"Сумма чисел равна {result}")


def int_func(word):
    """Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
    прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
    состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
    заглавной буквы. Необходимо использовать написанную ранее функцию int_func()."""
    # или string.capwords(word)
    return word[0].upper() + word[1:]


def first_letter_to_upper(words):
    return " ".join([int_func(word) for word in words.split()])


# print(division(input("Введите первое число для деления: "), input("Введите второе число для деления: ")))
# user_info_print(name='Джон', surname='Сноу', year=1998, city='Винтерфелл', email='kinginthenorth@gmail.com',
#                  phone='281-302')
# print(sum_of_max_two(1.0, 2, 3))
# print(number_in_power(input("Введите положительное число: "), input("Введите отрицательную степень: ")))
# sum_with_special_symbol()
# print(first_letter_to_upper("dfs gsd dsak d dsf"))

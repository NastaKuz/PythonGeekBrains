"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    if second == 0:
        raise MyZeroDivisionError("Нельзя делить на 0")
    print(f"Результат деления: {first/second}")
except ValueError:
    print("Неверный формат данных")
except MyZeroDivisionError as err:
    print(err)


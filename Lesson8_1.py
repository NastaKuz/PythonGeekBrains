"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, date_string):
        self.day, self.month, self.year = Date.string_to_date(date_string)

    def __str__(self):
        return f"День: {self.day}, Месяц: {self.month}, Год: {self.year} "

    @staticmethod
    def date_validate(check_day, check_month, check_year):
        if check_year > 0:
            if check_month in range(1, 13):
                if check_day in range(1, 32):
                    return True
                else:
                    return False

    @classmethod
    def string_to_date(cls, date_string):
        try:
            day, month, year = map(int, (date_string.split("-")))
            if Date.date_validate(day, month, year):
                return day, month, year
            else:
                raise ValueError
        except ValueError:
            print("Неверный формат данных")
            return 0, 0, 0


date_str = "31-12-2021"
dat = Date(date_str)
print(dat)

"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    def __init__(self, user_name, user_surname, user_position, user_income):
        self.name = user_name
        self.surname = user_surname
        self.position = user_position
        self._income = {"wage": user_income[0], "bonus": user_income[1]}


class Position(Worker):
    def __init__(self, user_name, user_surname, user_position, user_income):
        super(Position, self).__init__(user_name, user_surname, user_position, user_income)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print("Доход с учетом премии: ", sum(self._income.values()))


pos = Position("Иван", "Иванов", "Слесарь", (10000, 2000))
pos.get_full_name()
pos.get_total_income()
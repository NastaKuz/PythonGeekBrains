""" Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра. """


class Stationery:
    def __init__(self, u_title):
        self.title = u_title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Рисуем маркером {self.title}")


stat = Stationery("Перо")
stat.draw()

pen = Pen("Berlingo")
pen.draw()

pencil = Pencil("KOH-I-NOOR")
pencil.draw()

handle = Handle("Edding")
handle.draw()


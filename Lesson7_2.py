"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """
from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):
    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 77:
            self.__size = 77
        elif size < 38:
            self.__size = 38
        else:
            self.__size = size

    def calculate_fabric(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 188:
            self.__height = 188
        elif height < 158:
            self.__height = 158
        else:
            self.__height = height

    def calculate_fabric(self):
        return 2 * self.height + 0.3


costume = Costume(154)
coat = Coat(50)
print("Рост для костюма:")
print(costume.height)
print("Расчет ткани для костюма:")
print(costume.calculate_fabric())
print("Размер для пальто:")
print(coat.size)
print("Расчет ткани для пальто:")
print(coat.calculate_fabric())

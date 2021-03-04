"""«Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь. Реализуйте механизм валидации вводимых пользователем
данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""
import inspect


class Warehouse:
    def __init__(self):
        self.catalog = {}

    def add_tech(self, tech):
        if tech.id in self.catalog.keys():
            print(f"Техника с номером {tech.id} уже есть на складе, заменяю  значение")
        self.catalog[tech.id] = tech.tech_dict()

    def redirect_unit(self, id):
        self.catalog.pop(id)


class OrgTech:
    def __init__(self, id, name, amount, price):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, number):
        try:
            number = int(number)
            if number > 0:
                self.__amount = number
            else:
                raise ValueError
        except ValueError:
            print("Неверное количество техники")
            self.__amount = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, number):
        try:
            number = int(number)
            if number > 0:
                self.__price = number
            else:
                raise ValueError
        except ValueError:
            print("Неверная цена техники")
            self.__price = 0

    def __str__(self):
        return f"{self.name.capitalize()}. Количество техники: {self.amount} Цена: {self.price} Номер: {self.id}"

    def tech_dict(self):
        dict = {}
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    dict[i[0]] = i[1]
        return dict


class Printer(OrgTech):
    def __init__(self, id, name, amount, price, type, color):
        super(Printer, self).__init__(id, name, amount, price)
        self.color = color
        self.type = type

    def __str__(self):
        return f"{self.name.capitalize()}. Номер: {self.id} Количество принтеров: {self.amount} Цена: {self.price}"\
               f" Тип: {self.type} Цвет: {self.color}"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, check_color):
        if check_color == 0:
            self.__color = "чб"
        elif check_color == 1:
            self.__color = "цветной"
        else:
            print("Неверный ввод цвета принтера")
            self.__color = None


class Scanner(OrgTech):
    def __init__(self, id, name, amount, price, sides, color):
        super(Scanner, self).__init__(id, name, amount, price)
        self.color = color
        self.sides = sides

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, check_color):
        if check_color == 0:
            self.__color = "чб"
        elif check_color == 1:
            self.__color = "цветной"
        else:
            print("Неверный ввод цвета сканера")
            self.__color = None

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, check_sides):
        if check_sides == 1:
            self.__sides = "односторонний"
        elif check_sides == 2:
            self.__sides = "двусторонний"
        else:
            print("Неверный ввод количества сторон сканера")
            self.__sides = None

    def __str__(self):
        return f"{self.name.capitalize()}. Номер: {self.id} Количество сканеров: {self.amount} Цена: {self.price}" \
               f" Цвет: {self.color} Тип устройства подачи: {self.sides}"


class Copier(OrgTech):
    def __init__(self, id, name, amount, price, speed):
        super(Copier, self).__init__(id, name, amount, price)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, check_speed):
        try:
            check_speed = int(check_speed)
            if check_speed > 0:
                self.__speed = check_speed
            else:
                raise ValueError
        except ValueError:
            print("Неверная скорость ксерокса")
            self.__speed = 0

    def __str__(self):
        return f"{self.name.capitalize()}. Номер: {self.id} Количество ксероксов: {self.amount} Цена: {self.price}" \
               f" Скорость: {self.speed}"


cop = Copier(1, "copy", 45, 67700, -67)
print(cop)
scan = Scanner(2, "scan", 3, 56000, 1, 0)
print(scan)
pr = Printer(3, "print", 6, 4500, "лазерный", 0)
print(pr)
ware = Warehouse()
ware.add_tech(cop)
ware.add_tech(pr)
ware.add_tech(scan)
print(ware.catalog)
ware.redirect_unit(1)
print(ware.catalog)

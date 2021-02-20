"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    def __init__(self, u_speed, u_color, u_name, u_is_police):
        self.speed = u_speed
        self.color = u_color
        self.name = u_name
        self.is_police = u_is_police

    def car_info(self):
        print(f"{self.color.capitalize()} {self.name}")

    def go(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины:", self.speed)


class TownCar(Car):
    limit = 60

    def __init__(self, u_speed, u_color, u_name):
        super(TownCar, self).__init__(u_speed, u_color, u_name, False)

    def show_speed(self):
        if self.speed > self.limit:
            print(f"Превышение скорости! Лимит {self.limit}, ваша скорость {self.speed}")
        else:
            Car.show_speed(self)


class WorkCar(Car):
    limit = 40

    def __init__(self, u_speed, u_color, u_name):
        super(WorkCar, self).__init__(u_speed, u_color, u_name, False)

    def show_speed(self):
        if self.speed > self.limit:
            print(f"Превышение скорости! Лимит {self.limit}, ваша скорость {self.speed}")
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, u_speed, u_color, u_name):
        super(SportCar, self).__init__(u_speed, u_color, u_name, False)


class PoliceCar(Car):
    def __init__(self, u_speed, u_color, u_name):
        super(PoliceCar, self).__init__(u_speed, u_color, u_name, True)


w_car = WorkCar(35, 'красная', 'Audi')
w_car.car_info()
w_car.show_speed()
w_car.go()
w_car.turn("направо")
w_car.stop()

p_car = PoliceCar(13, 'синяя', 'BMW')
p_car.car_info()
p_car.show_speed()
p_car.go()
p_car.turn("налево")

s_car = SportCar(234, 'зеленая', 'Ferrari')
s_car.car_info()
s_car.show_speed()
s_car.go()

t_car = TownCar(72, 'белая', 'Toyota')
t_car.car_info()
t_car.show_speed()

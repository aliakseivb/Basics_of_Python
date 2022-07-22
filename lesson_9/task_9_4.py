# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, is_police(булево). speed - текущая скорость машины.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала,
# остановилась, повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

# Реализуйте класс Car (машина)
class Car:

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is going out'

    def stop(self):
        return f'{self.name} is stopping now'

    def turn(self, direction):
        self.direction = direction
        return f'{self.name} is turning {self.direction}'

    # добавьте в базовый класс метод show_speed
    def show_speed(self):
        return f'{self.name} is going with speed {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} - police car'
        else:
            return f'{self.name} - not police car'


# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    # для классов TownCar и WorkCar переопределите метод show_speed.
    def show_speed(self):
        if self.speed >= 60:
            return f'Your current speed is {self.speed}, limit - 60. Slow down!!!'
        else:
            return f'Your current speed {self.speed}'

# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    # для классов TownCar и WorkCar переопределите метод show_speed.
    def show_speed(self):
        if self.speed >= 40:
            return f'Your current speed is {self.speed}, limit - 40. Slow down!!!'
        else:
            return f'Your current speed {self.speed}'

# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



# Создайте экземпляры классов, передайте значения атрибутов.
c1 = SportCar(120, 'Red', 'Ferari', False)
c2 = TownCar(29, 'Black', 'Reno', False)
c3 = WorkCar(65, 'Green', 'Mercedes', False)
c4 = PoliceCar(90, 'Blue', 'Opel', True)
print(c1.show_speed())
print(c2.show_speed())
print(c3.show_speed())
print(c4.show_speed())
print(c1.police())
print(c4.police())
print(f'When {c4.go()} then {c2.stop()}')
print(f'{c3.turn("left")}')

class Transport:
    horse_force = 735.49875 / 16  # атрибут класса, он же будет доступен в методах экземпляра

    def __init__(self, power_engine, mass, transport_type,
                 name='underfinder', color='break',
                 body='hachback', transmission='auto'):  # метод init - конструктор-иницализатор
        self.power_engine = power_engine * self.horse_force  # или Car.horse_force  # получает параметры уникальные для данного экземпляра
        self.__mass = mass  # обьявление атрибута экземпляра (обязательно self)
        # a = 1                                                   # локальная переменная, после выполнения функции исчезнет
        self.velocity = 0
        self.tire_friction = 0.7
        self.gas_acceler = self.power_engine / self.__mass
        self.break_acceler = -9.81 / self.tire_friction
        self.type = transport_type

        self.name = name
        self.color = color
        self.body = body
        self.transmisson = transmission

    def gas_pedal(self, duration):  # создание функции-метода класса Car
        print(f'Вы жали на педаль газа {duration} сек')
        rez = ''
        for time in range(duration):
            velocity = self.velocity + time * self.gas_acceler
            rez += f'{velocity:.0f} '  # .0f убирает лишние знаки после запятой
        self.velocity = velocity
        return rez

    def break_pedal(self, duration=None):  # создание функции-метода класса Car
        print(f'Вы жали на педаль тормоза {duration} сек')
        rez = ''
        time = 0
        while True:
            time += 1
            velocity = self.velocity + time * self.break_acceler
            if velocity <= 0:
                self.velocity = 0
                rez += f'[stop]'
                break
            if duration is not None and time >= duration:
                break
            rez += f'{velocity:.0f} '
            self.velocity = velocity
        return rez

    def speedometer(self):  # создание функции-метода класса Car
        return self.velocity


# class Car(Transport): pass  # class Car - наследует класс Transport, pass если ничего не переопределяем в нем
class Car(Transport):
    def __init__(self, power_engine, mass):
        super().__init__(power_engine, mass, 'car')  # явно вызвать метод __init__ класса-предка

class Truck(Transport):
    def __init__(self, power_engine, mass, velocity_limit=None):
        self.__velocity_limit = velocity_limit
        super().__init__(power_engine, mass, 'truck')

    def gas_pedal(self, duration):  # создание функции-метода класса Car
        print(f'Вы жали на педаль газа {duration} сек')
        rez = ''
        for time in range(duration):
            velocity = self.velocity + time * self.gas_acceler
            if self.__velocity_limit is not None and velocity >= self.__velocity_limit:
                rez += f'{self.__velocity_limit} [limit]'
                break
            else:
                rez += f'{velocity:.0f} '  # .0f убирает лишние знаки после запятой
        self.velocity = velocity
        return rez


c1 = Car(320, 2600)  # создание экземпляра класса Car с опред параметрами, определенными в конструкторе init
c2 = Car(450, 3300)  # создание экземпляра класса Car

t1 = Truck(500, 7000)
t2 = Truck(500, 7000, 30)
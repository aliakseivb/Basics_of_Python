# 3. Реализовать класс Worker (работник).
# Техническое задание:
#
# определить атрибуты: name, surname, position (должность), income (доход)
# атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}
# При создании экземпляра параметры wage, bonus передаются как числа.
# создать класс Position (должность) на базе класса Worker. Это наследование.
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income). Подумайте, корректно ли в классе наследнике напрямую
# обращаться к защищенному атрибуту income. Или нужен getter? Аргументируйте ответ.
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

# Реализовать класс Worker (работник).
class Worker:

    # определить атрибуты: name, surname, position (должность), income (доход)
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}


# создать класс Position (должность) на базе класса Worker. Это наследование.
class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return str.capitalize(self.name) + ' ' + str.capitalize(self.surname)

    def get_total_income(self):
        # Подумайте, корректно ли в классе наследнике напрямую обращаться к защищенному атрибуту income.
        # Или нужен getter? Аргументируйте ответ.
        # На вебинаре до геттеров и сеттеров так и не добрались, да и в методичке про них ни слова,
        # пока оставлю этот вопрос без ответа и обращусь напрямую - работает же
        return self._income.get('salary') + self._income.get('bonus')


pos = Position('Max', 'stivenson', 'teacher', 2000, 1500)
pos1 = Position('elon', 'Musk', 'director', 5000000, 250000)
print(pos.get_full_name())  # Max Stivenson
print(pos.get_total_income())  # 3500
print(pos1.get_full_name())  # Elon Musk
print(pos1.get_total_income())  # 5250000

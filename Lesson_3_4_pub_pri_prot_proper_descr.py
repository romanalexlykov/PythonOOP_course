#  Задание 1. Объявите класс Calendar для хранения даты: день, меясц, год. Определите свойства для записи и считывания
#  этой информации из этого класса. (Дополнение: используя __slots__ разрешите использовать только строго определенные
#  локальные свойства в экземплярах класса).
from _datetime import datetime


class Calendar:
    """Класс, для хранения даты: день, месяц, год"""
    __slots__ = ['__day', '__month', '__year']

    def __init__(self, day=0, month=0, year=0):
        for elem in [day, month, year]:
            if Calendar.__checkValue(elem):
                self.__day = day
                self.__month = month
                self.__year = year
            else:
                print('Некорректные координаты при инициализации экземпляра')
                raise AttributeError

    def __checkValue(x):
        return isinstance(x, int)

    def setDate(self, day, month, year):
        if Calendar.__checkValue(day) and Calendar.__checkValue(month) and Calendar.__checkValue(year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            print('Некорректные координаты')

    def getDate(self):
        return self.__day, self.__month, self.__year


# my_date = Calendar(12, 5, 2021)
my_date = Calendar(4, 5, 6)
print(my_date.getDate())


#  Задание 2. Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. Создайте дескрипторы
#  для записи и считывания этих значений в классе (атрибуты с данными координат должны быть приватными).


class PointLocation:
    """Дескриптор для работы с коррдинатами точек - добавления, получения, удаления"""

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Rectangle:
    """Класс, храняший координаты верхней левой и правой нижней точек прямоугольника"""
    coord1 = PointLocation()
    coord2 = PointLocation()

    def __init__(self, x1y1=(0, 0), x2y2=(0, 0)):
        self.coord1 = x1y1
        self.coord2 = x2y2


ABCD = Rectangle((3, 5), (5, 6))
print(ABCD.coord1, ABCD.coord2)  # выдает (3, 5) (5, 6)
ABCD.coord1 = (5, 10)
print(ABCD.coord1, ABCD.coord2)  # выдает (5, 10) (5, 6)
ABCD2 = Rectangle((100, 100), (110, 90))
print(ABCD.coord1, ABCD.coord2)  # выдает (5, 10) (5, 6)
print(ABCD2.coord1, ABCD2.coord2)  # выдает (100, 100) (110, 90)

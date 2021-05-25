#  Задача 1. Напишите класс Point3D для хранения координат в техмерном простарнстве (x, y, z). Реализуйте перегрузку
#  операторов сложения, вычитания, умножения, деления для этого класса. Также сделайте возможность сравннеия
#  координат между собой и запись/чтение значений через ключи 'x', 'y', 'z'

class PointLocation:
    """Дескриптор для работы с каждой коррдинатой точки - добавления, получения"""

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point3D:

    coord = PointLocation()

    def __init__(self, pcoord=(0, 0, 0)):
        self.coord = pcoord

    def __add__(self, other):
        return Point3D((self.coord[0] + other.coord[0], self.coord[1] + other.coord[1], self.coord[2] + other.coord[2]))

    def __getitem__(self, item):
        if item == 'x':
            return self.coord[0]
        if item == 'y':
            return self.coord[1]
        if item == 'z':
            return self.coord[2]

A = Point3D((1, 10, 100))
B = Point3D((2, 20, 200))

C = A + B

print(C.coord)
print(A['x'])



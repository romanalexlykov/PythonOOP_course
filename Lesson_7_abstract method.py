# Заданиее 1. Создайте базовый класс "Стол" и дочерние: "Прямоугольные столы" и "Круглые столы".. Через конструктор
# базового класса передавайте размер повехности стола: для прямоугольного - ширина и длина, для круглого - радиус. В
# дочерних классах реализуйте метод вычисления площади поверхности стола

from math import pi

class Tables:
    def __init__(self, width=None, length=None, radius=None):
        self.__width = width
        self.__length = length
        self.__radius = radius


class RectTables(Tables):
    def setParameters(self, width, length):
        self.__width = width
        self.__length = length

    def calcRectS(self):
        s = self.__width * self.__length
        return s


class RoundTables(Tables):
    def setParameters(self, radius):
        self.__radius = radius

    def calcRoundS(self):
        s = (pi * (self.__radius ** 2))
        return s


sq = RectTables()
sq.setParameters(5, 6)
print(sq.calcRectS())
sr = RoundTables()
sr.setParameters(5)
print(sr.calcRoundS())

# Задание 2. Создайте класс Animal (животное) и разные производные от него подклассы: Fox, Bird, Cat, Dog и т.п.
# Реализуйте у них общий метод say(), который бы возвращал звук, издаваемый этим животным. Создайте кортеж из
# нескольких экземпляров этих классов, переберите их в цикле и выведите в консоль их звуки (вызовите метод say())


class Animal:
    def __init__(self, voice):
        self._voice = voice


class Fox(Animal):
    def say(self):
        print(self._voice)


class Bird(Animal):
    def say(self):
        print(self._voice)


class Cat(Animal):
    def say(self):
        print(self._voice)


class Dog(Animal):
    def say(self):
        print(self._voice)


animals = (Fox('Khe'), Bird('Few'), Cat('Meaw'), Dog('Wow'))

for animal in animals:
    animal.say()


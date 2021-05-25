# Задание 1. Создайте суперкласс "Персональные компьютеры" и на его основе подклассы: "Настольные ПК" и "Ноутбуки". В
# базовом классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные
# свойства: для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль; для
# ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль

class Computer:
    def __init__(self, ram: int = 2, rom: int = 128, model: str = 'Intel', cpu: int = 2400):
        self._ram = ram
        self._rom = rom
        self._model = model
        self.cpu = cpu

class Desktop(Computer):
    def __init__(self, ram, rom, model, cpu, monitor: str, keyboard: str, mouse: str, size: str):
        super().__init__(ram, rom, model, cpu)
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
        self._size = size

    def getParameters(self):
        return f"Параметры Desktop-компа: ram {self._ram}, rom {self._rom}, model {self._model}, cpu {self.cpu}, " \
               f"monitor {self._monitor}, keyboard {self._keyboard}, mouse {self._mouse}, size {self._size}"

class Laptop(Computer):
    def __init__(self, ram, rom, model, cpu, size: str, diag: str):
        super().__init__(ram, rom, model, cpu)
        self._size = size
        self._diag = diag

    def getParameters(self):
        return f'Параметры Desktop-компа: ram {self._ram}, rom {self._rom}, model {self._model}, cpu {self.cpu}, ' \
               f'size {self._size}, diag {self._diag}'

dt1 = Desktop(4, 512, 'AMD', 3600, 'Sony', 'BT', 'Optic', '10*25')

print(dt1.getParameters())



# Задание 2. Повторите это задание для суперкласса "Человек" и подклассов "Мужчина" и "Женщина". Подумайте,
# какие общие характеристики можно выделить в супекласс и какие частные свойства указать в подклассах


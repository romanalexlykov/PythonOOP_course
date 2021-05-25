#  Задание. Создайте дочерний класс Motherboard (материнская плата), которая наследуется от классов: CPU (процессор),
#  GPU (графический процессор), Memory (память). В свою очередь CPU наследуется от классов AMD и Intel,
#  а GPU от классов Nvidia и GeForce.

class Memory:
    def __init__(self):
        super().__init__()


class AMD:
    def __init__(self):
        super().__init__()


class Intel:
    def __init__(self):
        super().__init__()


class Nvidia:
    def __init__(self):
        super().__init__()


class GeForce:
    def __init__(self):
        super().__init__()


class CPU(AMD, Intel):
    def __init__(self):
        super().__init__()


class GPU(Nvidia,GeForce):
    def __init__(self):
        super().__init__()


class Motherboard(CPU, GPU, Memory):
    def __init__(self):
        super().__init__()


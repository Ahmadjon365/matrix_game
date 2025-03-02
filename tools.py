from father_class import OTA

class ANJOM(OTA):
    def __init__(self, name, power, x, y):
        super().__init__(x, y)
        self.name = name
        self.power = power

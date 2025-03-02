import random
from father_class import OTA

class DUSHMAN(OTA):
    def __init__(self, x, y, power):
        super().__init__(x, y)
        self.power = power

    def move_randomly(self, zone):
        while True:
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(zone) - 1 and 0 <= ny < len(zone[0]) - 1 and zone[nx][ny] == '*':
                self.x, self.y = nx, ny
                break


class PLAYER(OTA):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.power = 100
        self.items = []

    def pick_item(self, item):
        self.power += item.power
        self.items.append(item.name)
        print(f"Siz {item.name} oldingiz! Kuchingiz: {self.power}")

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
    
    def move_towards_player(self, player_x, player_y, zone, enemies):
        dx = 1 if player_x > self.x else -1 if player_x < self.x else 0
        dy = 1 if player_y > self.y else -1 if player_y < self.y else 0

        new_x, new_y = self.x + dx, self.y + dy

        if 0 <= new_x < len(zone) and 0 <= new_y < len(zone[0]):
            occupied = any(e.x == new_x and e.y == new_y for e in enemies)
            if zone[new_x][new_y] in ('*', 'P') and not occupied:
                self.x, self.y = new_x, new_y



class PLAYER(OTA):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.power = 100
        self.items = []

    def pick_item(self, item):
        self.power += item.power
        self.items.append(item.name)
        print(f"Siz {item.name} oldingiz! Kuchingiz: {self.power}")

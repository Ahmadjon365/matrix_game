import random
from tools import ANJOM
from players import PLAYER, DUSHMAN

class Game:
    def __init__(self):
        self.zone = [['*' for _ in range(15)] for _ in range(10)]
        self.OYINCHI = 'P'
        self.XAZINA = 'T'
        self.moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1),
                      'wa': (-1, -1), 'wd': (-1, 1), 'sa': (1, -1), 'sd': (1, 1)}

        self.PLAYER = PLAYER(*self.place_in_corner("bottom-left"))
        self.t_x, self.t_y = self.place_in_corner("top-right")
        self.zone[self.PLAYER.x][self.PLAYER.y] = self.OYINCHI
        self.zone[self.t_x][self.t_y] = self.XAZINA

        self.items = {}
        for name, power in [("Qilich", 10), ("Pistalet", 20), ("Avtomat", 30)]:
            ix, iy = self.place_randomly()
            self.items[(ix, iy)] = ANJOM(name, power, ix, iy)
            self.zone[ix][iy] = 'I'

        ex, ey = self.place_randomly()
        self.enemy = DUSHMAN(ex, ey, size=5, power=30)
        self.zone[self.enemy.x][self.enemy.y] = 'E'

    def place_in_corner(self, corner):
        return {
            "top-left": (0, 0),
            "top-right": (0, len(self.zone[0]) - 1),
            "bottom-left": (len(self.zone) - 1, 0),  # Fixed here
            "bottom-right": (len(self.zone) - 1, len(self.zone[0]) - 1)  # Fixed here
        }[corner]

    def place_randomly(self):
        while True:
            x, y = random.randint(0, len(self.zone) - 1), random.randint(0, len(self.zone[0]) - 1)
            if self.zone[x][y] == '*':
                return x, y

    def print_zone(self):
        for row in self.zone:
            print(' '.join(row))
        print()

    def play(self):
        self.print_zone()
        while True:
            move = input("Harakat (w/s/a/d): ")
            if move in self.moves:
                dx, dy = self.moves[move]
                nx, ny = self.PLAYER.x + dx, self.PLAYER.y + dy

                if 0 <= nx < len(self.zone[0]) and 0 <= ny < len(self.zone):
                    self.zone[self.PLAYER.x][self.PLAYER.y] = '*'
                    self.PLAYER.move_player(dx, dy, self.zone)

                    if (self.PLAYER.x, self.PLAYER.y) in self.items:
                        item = self.items.pop((self.PLAYER.x, self.PLAYER.y))
                        self.PLAYER.pick_item(item)
                    elif (self.PLAYER.x, self.PLAYER.y) == (self.t_x, self.t_y):
                        print("Tabriklaymiz! Xazinani topdingiz! 🎉")
                        break
                    elif (self.PLAYER.x, self.PLAYER.y) == (self.enemy.x, self.enemy.y):
                        if self.PLAYER.power >= self.enemy.power:
                            print("Dushmanni yengdingiz! ✅")
                            self.PLAYER.power -= self.enemy.power
                            print(f"Sizda {self.PLAYER.power} kuch qoldi!")
                            self.zone[self.enemy.x][self.enemy.y] = '*'
                            self.enemy = None  # Dushman o'yindan chiqariladi
                        else:
                            print("Dushmanga yutqazdingiz! ❌")
                            break

                    self.zone[self.PLAYER.x][self.PLAYER.y] = self.OYINCHI

                if self.enemy is not None:
                    self.zone[self.enemy.x][self.enemy.y] = '*'
                    self.enemy.move_randomly(self.zone)
                    self.zone[self.enemy.x][self.enemy.y] = 'E'

            self.print_zone()


if __name__ == "__main__":
    game = Game()
    game.play()

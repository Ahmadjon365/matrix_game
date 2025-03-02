class OTA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_anomy(self, dx, dy, zone):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(zone) and 0 <= ny < len(zone[0]) and zone[nx][ny] == '*':
            self.x, self.y = nx, ny

    def move_player(self, dx, dy, zone):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(zone) and 0 <= ny < len(zone[0]) and zone[nx][ny] in {'*', 'I', 'T', 'E'}:
            self.x, self.y = nx, ny

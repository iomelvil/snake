from snake import Snake
class Board:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = board = [[' ' for _ in range(width)] for _ in range(height)]

    def render(self):
        print('-' * (self.width +2))
        for row in self.grid:
            print('|' + ''.join(row) + '|')
        print('-' * (self.width + 2))

    def clear(self):
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def place_snake(self,snake):
        for i, (x,y) in enumerate(snake.body):
            if 0 <=y < self.height and 0 <=x < self.width:
                self.grid[y][x] = '@' if i ==0 else 'S'

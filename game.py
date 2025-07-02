from board import Board
from snake import Snake
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.snake = Snake(initial_position=(10,10))
        self.state = 'start'
        self.tick = 0

    def start(self):
        print("start game")
        self.state = 'playing'

    def update(self):
        self.snake.move()
        self.tick += 1

    def render(self):
        self.board.clear()
        self.board.place_snake(self.snake)
        self.board.render()

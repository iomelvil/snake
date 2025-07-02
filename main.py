# Main run file for first test commit
import time
from game import Game

def main():
    game = Game()

    while game.state != 'game_over':
        if game.state == 'start':
            game.start()
        elif game.state == 'playing':
            game.update()
            game.render()
            time.sleep(0.5)


if __name__ == "__main__":
    main()
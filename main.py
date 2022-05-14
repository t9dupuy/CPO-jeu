from enum import Enum
from src.game import Game
from src.menu import Menu
from src.parameter import Param
from src.menu_fin import draw

import pygame
pygame.init()


class State(Enum):
    MAIN_MENU = 1
    PARAM = 2
    GAME = 3
    END_MENU = 4


def main():
    state = State.MAIN_MENU

    menu = Menu()
    para = Param()

    pygame.display.set_caption("Jeu")
    screen = pygame.display.set_mode((1080, 720))

    while True:
        match state:
            case State.MAIN_MENU:
                state = menu.run(screen)
            case State.PARAM:
                state = para.draw()
            case State.GAME:
                game = Game()
                state = game.run(screen)
            case State.END_MENU:
                state = draw([4, 5, 3])
            case _:
                break

    pygame.quit()


if __name__ == "__main__":
    main()

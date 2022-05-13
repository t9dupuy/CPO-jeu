from enum import Enum
from src.game import Game
from src.menu import Menu
from src.parameter import Param
from src.menu_fin import draw, basket_to_score

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
    game = Game()

    pygame.display.set_caption("Jeu")
    screen = pygame.display.set_mode((1080, 720))

    while True:
        match state:
            case State.MAIN_MENU:
                state = menu.run(screen)
            case State.PARAM:
                state = para.draw()
            case State.GAME:
                state = game.run(screen)
            case State.END_MENU:
                score = basket_to_score(game.player.basket)
                state = draw(score)
            case _:
                break

    pygame.quit()


if __name__ == "__main__":
    main()

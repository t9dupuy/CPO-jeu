from src.game import Game
from enum import Enum


class State(Enum):
    menu = "Menu"
    param = "Parameters"
    game = "Game"
    end = "End"


state = State["game"]


def main():
    game = Game()

    match state.value:
        case "Menu":
            print("In menu")
        case "Parameters":
            print("In parameters")
        case "Game":
            game.run()
        case "End":
            print("In end menu")


if __name__ == "__main__":
    main()

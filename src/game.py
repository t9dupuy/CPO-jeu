import pygame
from src.player import Player
from src.Product import *


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Game(metaclass=Singleton):

    def __init__(self):
        pygame.init()

        self.player: Player = Player()
        self.map: pygame.image = pygame.image.load("resources/tiles/png/v1.png")

        self.fonts = {'pixels32': pygame.font.Font("resources/fonts/pixels.ttf", 32)}

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.player.facing = 'back'
            self.player.pos_rel[1] -= 10
        if keys[pygame.K_DOWN]:
            self.player.facing = 'front'
            self.player.pos_rel[1] += 10
        if keys[pygame.K_LEFT]:
            self.player.facing = 'left'
            self.player.pos_rel[0] -= 10
        if keys[pygame.K_RIGHT]:
            self.player.facing = 'right'
            self.player.pos_rel[0] += 10

    def run(self):
        clk = pygame.time.Clock()

        pygame.display.set_caption("Jeu")
        screen = pygame.display.set_mode((1080, 720))

        running = True
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input(keys=pygame.key.get_pressed())

            screen.fill((58, 58, 80))

            screen.blit(self.map, (0, 0))
            self.player.draw(screen)

            #Display product
            Instance_Products(screen)

            pygame.display.update()

            clk.tick(60)

        pygame.quit()

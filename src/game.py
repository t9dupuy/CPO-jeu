import pygame
from src.player import Player


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
        self.map_pos_rel = [0, 0]

        self.borders = [100, 620, 100, 980]

        self.fonts = {'pixels32': pygame.font.Font("resources/fonts/pixels.ttf", 32)}

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()

    def move_up(self):
        self.player.facing = 'back'

        hitbox = [-2, 20, 70, 100]
        # [offset_x, offset_y, width, height] of the outside rectangle

        new_y = self.player.pos_rel[1] - 10

        if new_y + hitbox[1] < self.borders[0]:
            self.map_pos_rel[1] += 10
        else:
            self.player.pos_rel[1] = new_y

    def move_down(self):
        self.player.facing = 'front'

        hitbox = [-5, 30, 65, 160]
        # [offset_x, offset_y, width, height] of the outside rectangle

        new_y = self.player.pos_rel[1] + 10

        if new_y + hitbox[1] + hitbox[3] > self.borders[1]:
            self.map_pos_rel[1] -= 10
        else:
            self.player.pos_rel[1] = new_y

    def move_left(self):
        self.player.facing = 'left'

        hitbox = [-80, 40, 135, 95]
        # [offset_x, offset_y, width, height] of the outside rectangle

        new_x = self.player.pos_rel[0] - 10

        if new_x + hitbox[0] < self.borders[2]:
            self.map_pos_rel[0] += 10
        else:
            self.player.pos_rel[0] = new_x

    def move_right(self):
        self.player.facing = 'right'

        hitbox = [5, 40, 135, 95]
        # [offset_x, offset_y, width, height] of the outside rectangle

        new_x = self.player.pos_rel[0] + 10

        if new_x + hitbox[0] + hitbox[2] > self.borders[3]:
            self.map_pos_rel[0] -= 10
        else:
            self.player.pos_rel[0] = new_x

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

            screen.blit(self.map, self.map_pos_rel)
            self.player.draw(screen)

            pygame.display.update()

            clk.tick(60)

        pygame.quit()

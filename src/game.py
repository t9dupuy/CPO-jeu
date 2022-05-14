import pygame
from PIL import Image
from src.player import Player
from src.product import *
from src.productwindow import Sheet
from math import sqrt
from numpy import argmin


class Game:
    """
    Game class containing all basic information about the game state and parameters
    """
    def __init__(self):
        # Background image of the map
        self.map: pygame.image = pygame.image.load("resources/tiles/png/v2.png")
        self.map_pos_rel = [-1500, -1300]

        # Player instance
        self.player: Player = Player()

        # Products
        self.products = instance_products(self.map_pos_rel)

        # Collision layer image (as 2 dimensions array of pixels). Used for collision detection
        self.collision_layer = Image.open("resources/tiles/png/collision.png").load()

        # Invisible borders used to move the map instead of player.
        self.borders = [300, 520, 200, 880]

        # Dictionary of fonts
        self.fonts = {'pixels32': pygame.font.Font("resources/fonts/pixels.ttf", 32)}

        self.prod_info = Sheet()
        self.looking_at_product = (False, None)

    def handle_input(self, keys):
        """
        Function to handle all keyboard inputs through pygame's 'key.get_pressed()' method.
        :param keys: list of all pressed keys (acquired through 'pygame.key.get_pressed()' method).
        """
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()

    def move_map(self, new_pos: list[float, 2]):
        self.map_pos_rel = new_pos
        for product in self.products:
            product.update(self.map_pos_rel)

    def move_up(self):
        """
        Rather self-explanatory. Also runs the collision checker for the player.
        """
        self.player.facing = 'back'
        self.player.walking = True

        hitbox = [8, 20, 50, 100]
        # [offset_x, offset_y, width, height]

        new_y = self.player.pos_rel[1] - 10

        if not self.check_collisions([self.player.pos_rel[0], new_y], hitbox):
            if new_y + hitbox[1] < self.borders[0]:
                self.move_map([self.map_pos_rel[0], self.map_pos_rel[1] + 10])
            else:
                self.player.pos_rel[1] = new_y

    def move_down(self):
        """
        Rather self-explanatory. Also runs the collision checker for the player.
        """
        self.player.facing = 'front'
        self.player.walking = True

        hitbox = [5, 100, 45, 80]

        new_y = self.player.pos_rel[1] + 10

        if not self.check_collisions([self.player.pos_rel[0], new_y], hitbox):
            if new_y + hitbox[1] + hitbox[3] > self.borders[1]:
                self.move_map([self.map_pos_rel[0], self.map_pos_rel[1] - 10])
            else:
                self.player.pos_rel[1] = new_y

    def move_left(self):
        """
        Rather self-explanatory. Also runs the collision checker for the player.
        """
        self.player.facing = 'left'
        self.player.walking = True

        hitbox = [-80, 70, 70, 50]

        new_x = self.player.pos_rel[0] - 10

        if not self.check_collisions([new_x, self.player.pos_rel[1]], hitbox):
            if new_x + hitbox[0] < self.borders[2]:
                self.move_map([self.map_pos_rel[0] + 10, self.map_pos_rel[1]])
            else:
                self.player.pos_rel[0] = new_x

    def move_right(self):
        """
        Rather self-explanatory. Also runs the collision checker for the player.
        """
        self.player.facing = 'right'
        self.player.walking = True

        hitbox = [70, 70, 70, 50]

        new_x = self.player.pos_rel[0] + 10

        if not self.check_collisions([new_x, self.player.pos_rel[1]], hitbox):
            if new_x + hitbox[0] + hitbox[2] > self.borders[3]:
                self.move_map([self.map_pos_rel[0] - 10, self.map_pos_rel[1]])
            else:
                self.player.pos_rel[0] = new_x

    def check_collisions(self, new_pos: list[float, 2], hitbox: list[float, 4]) -> bool:
        """
        Collision checker for the player.

        Generate points on the player's hitbox rectangle and checks for each point
        if the corresponding pixel on the collision layer is black (if so, a collision is detected).
        :param new_pos: Player's next position
        :param hitbox: Player's hitbox
        :return: True if a collision is detected
        """
        num_points = 3

        points = []

        for n in range(num_points):
            points.append((new_pos[0] + hitbox[0] + n * (hitbox[2]/num_points),
                           new_pos[1] + hitbox[1]))
        for n in range(num_points):
            points.append((new_pos[0] + hitbox[0] + hitbox[2],
                           new_pos[1] + hitbox[1] + n * (hitbox[3]/num_points)))
        for n in range(num_points):
            points.append((new_pos[0] + hitbox[0] + hitbox[2] - n * (hitbox[2]/num_points),
                           new_pos[1] + hitbox[1] + hitbox[3]))
        for n in range(num_points):
            points.append((new_pos[0] + hitbox[0],
                           new_pos[1] + hitbox[1] + hitbox[3] - n * (hitbox[3]/num_points)))

        for point in points:
            if self.collision_layer[point[0] - self.map_pos_rel[0], point[1] - self.map_pos_rel[1]] == (0, 0, 0, 255):
                return True

        return False

    def pickClosestProduct(self):
        dist = [sqrt((self.player.pos_rel[0] - product.pos_rel[0])**2 + (self.player.pos_rel[1] - product.pos_rel[1])**2) for product in self.products]
        if dist:
            return argmin(dist)
        return -1

    def checkPlayerArrival(self):
        if self.collision_layer[self.player.pos_rel[0] - self.map_pos_rel[0] + 30, self.player.pos_rel[1] - self.map_pos_rel[1] + 100] == (110, 200, 250, 255):
            return True
        return False

    def run(self, screen):
        from __main__ import State

        clk = pygame.time.Clock()

        ret = 0

        running = True
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.looking_at_product[0]:
                        i = self.pickClosestProduct()
                        if i != -1:
                            self.looking_at_product = (True, i)

            if self.checkPlayerArrival():
                return State.END_MENU

            self.player.walking = False

            self.handle_input(keys=pygame.key.get_pressed())

            screen.fill((58, 58, 80))

            screen.blit(self.map, self.map_pos_rel)
            self.player.draw(screen)

            # Display product
            for product in self.products:
                product.draw(screen)

            if self.looking_at_product[0]:
                ret = self.prod_info.draw_productinfo(screen, self.products[self.looking_at_product[1]])
                if ret == -1:
                    self.looking_at_product = (False, None)
                elif ret == 1:
                    self.player.basket.append(self.products.pop(self.looking_at_product[1]))
                    self.looking_at_product = (False, None)


            pygame.display.update()

            clk.tick(60)

        return None

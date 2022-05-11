# Product classes
import pygame
from math import cos, pi


class Product:
    t = 0

    def __init__(self, name, sante, environemental, budget, pos_fix, pos_rel, sprite):
        self.name = name
        self.sante = sante
        self.environemental = environemental
        self.budget = budget
        self.pos_fix = pos_fix
        self.pos_rel = pos_rel
        self.sprite = sprite

    def update(self, map_pos_rel):
        for i in range(2):
            self.pos_rel[i] = self.pos_fix[i] + map_pos_rel[i]

    def draw(self, screen: pygame.display):
        """
        Draw the product
        :param screen: 'pygame.display' screen to render on.
        """
        # define product size on screen
        screen.blit(self.sprite, [self.pos_rel[0], self.pos_rel[1] - 10 * (cos(Product.t) + 1)])
        Product.t = (Product.t + 0.01) % (2 * pi)


def instance_products(map_pos_rel):  # Intenciation des Produits
    products = [Product("cod", 4, 4, 3, [560, 350], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (64, 64))),
                Product("oo", 4, 4, 3, [270, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/salmon.png"), (64, 64))),
                Product("oo", 4, 4, 3, [1550, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/beef.png"), (64, 64))),
                Product("oo", 4, 4, 3, [1650, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/chicken.png"), (64, 64)))]

    for product in products:
        product.update(map_pos_rel)

    return products

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


def instance_products(map_pos_rel):  # Produits
    products = [Product("Cod", 4, 4, 3, [560, 350], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (64, 64))),
                Product("Salmon", 3, 3, 1, [270, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/salmon.png"), (64, 64))),
                Product("Beef", 3, 2, 3, [1550, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/beef.png"), (64, 64))),
                Product("Chicken", 4, 3, 4, [1650, 420], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/chicken.png"), (64, 64))),
                Product("Apple", 3, 4, 4, [780, 1240], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/apple.png"), (64, 64))),
                Product("Beetroot", 5, 4, 4, [200, 1380], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/beetroot.png"), (64, 64))),
                Product("Bread", 3, 5, 4, [2060, 400], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/bread.png"), (64, 64))),
                Product("Cake", 2, 3, 2, [2520, 400], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/cake.png"), (64, 64))),
                Product("Carrot", 4, 4, 4, [200, 860], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/carrot.png"), (64, 64))),
                Product("Cookie", 2, 3, 3, [2250, 400], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/cookie.png"), (64, 64))),
                Product("Egg", 3, 3, 3, [1060, 1400], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/egg.png"), (64, 64))),
                Product("Endive", 5, 4, 3, [200, 580], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/endive.png"), (64, 64))),
                Product("Groseille", 4, 3, 1, [620, 1240], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/groseille.png"), (64, 64))),
                Product("Melon", 3, 4, 4, [1450, 720], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/melon_slice.png"), (64, 64))),
                Product("Mutton", 3, 3, 3, [1700, 700], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/mutton.png"), (64, 64))),
                Product("Pork", 4, 2, 3, [1700, 800], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/porkchop.png"), (64, 64))),
                Product("Potato", 4, 4, 5, [1060, 1300], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/potato.png"), (64, 64))),
                Product("Pie", 4, 3, 2, [1450, 850], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/pumpkin_pie.png"), (64, 64))),
                Product("Rabbit", 3, 3, 2, [1700, 900], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/rabbit.png"), (64, 64))),
                Product("Salad", 4, 2, 4, [400, 650], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/salad.png"), (64, 64))),
                Product("Sugar", 1, 3, 3, [1700, 1300], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/sugar.png"), (64, 64)))]

    for product in products:
        product.update(map_pos_rel)

    return products

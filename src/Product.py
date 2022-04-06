# Product classes
import pygame


class Product:
    def __init__(self, sante, environementale, budget, pos_fix, pos_rel, sprite):
        self.sante = sante
        self.environementale = environementale
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
        screen.blit(self.sprite, self.pos_rel)


def instance_products(map_pos_rel):  # Intenciation des Produits
    products = [Product(4, 4, 3, [500, 400], [0, 0], pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (64, 64))),]

    for product in products:
        product.update(map_pos_rel)

    return products

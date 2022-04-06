# Product classes
import pygame


class Product:
    def __init__(self, sante, environementale, budget, pos_rel, path_sprit):
        self.sante = sante
        self.environementale = environementale
        self.budget = budget
        self.pos_rel = pos_rel
        self.path_sprit = path_sprit

    def draw(self, screen: pygame.display):
        """
        Draw the product
        :param screen: 'pygame.display' screen to render on.
        """
        # define product size on screen
        self.path_sprit = pygame.transform.scale(self.path_sprit, (64, 64))
        screen.blit(self.path_sprit, (self.pos_rel[0], self.pos_rel[1]))

def Instance_Products(screen): #Intenciation des Produits
    #Test
    product = Product(4, 4, 3, [1.0, 1.0], pygame.image.load("resources/products/16x16/cod.png"))
    product.draw(screen)





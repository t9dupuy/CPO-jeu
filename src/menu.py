import pygame

class Menu():

    def __init__(self):
        pygame.init()

        self.background = pygame.image.load('resources/wallpaper/market.jpg')

    def run(self):

        pygame.display.set_caption("Menu")
        screen = pygame.display.set_mode((1080, 720))

        running = True
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.blit(self.background, (0, 0))

            pygame.display.flip()


        pygame.quit()
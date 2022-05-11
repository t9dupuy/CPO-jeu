from typing import List

import pygame
from src.product import *
from src.menu import *


class ProductWindow():

    def __init__(self):
        pygame.init()

    def run(self):

        width = 1080
        length = 720

        background = pygame.image.load("resources/wallpaper/market.jpg")

        pygame.display.set_caption("Window")
        screen = pygame.display.set_mode((width, length))

        product = Product("Cod", 4, 4, 3, [500, 400], [280, 170], pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (64, 64)))


        running = True
        while running:



            screen.blit(background, (0, 0))

            Sheet.draw_background(background, screen)

            Sheet.draw_productinfo(background, screen, product)



            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Sheet.staticButton.checkForInput(mouse_pos):
                        pygame.quit()

            pygame.display.flip()


        pygame.quit()

class Sheet:

    pygame.init()

    staticRect = pygame.Rect(250,150, 300, 500)
    staticFont =  pygame.font.Font("resources/fonts/Dunkin.otf", 50)
    staticTextToShow = ["Nutri : ", "Envir : ", "Price : "]
    staticTextPos = (380, 300)
    staticTextRender, staticTextRect = [], []


    staticLinesStart = pygame.Vector2(275,staticTextPos[1]+50)
    staticLinesEnd = pygame.Vector2(525, staticTextPos[1]+50)


    for elem in range(len(staticTextToShow)):
        staticTextRender.append(staticFont.render(staticTextToShow[elem], True, "Black"))
        staticTextRect.append(staticTextRender[elem].get_rect(center=(staticTextPos[0], staticTextPos[1] + elem*100)))

    staticButton = Button(color=(205, 92, 92), size=(200, 90), radius=10,
                             pos=(390, 620),
                             text_input="ADD", font_type="resources/fonts/Dunkin.otf", base_color="White",
                             hovering_color="Grey")




    @staticmethod
    def draw_background(self, screen):

        pygame.draw.rect(screen, 'White', Sheet.staticRect, 0, 20)

        for elem in range(len(Sheet.staticTextRender)):
            screen.blit(Sheet.staticTextRender[elem], Sheet.staticTextRect[elem])

        for elem in range(3) :
            pygame.draw.line(screen, 'Black',(Sheet.staticLinesStart.x, Sheet.staticLinesStart.y + 100*elem) , (Sheet.staticLinesEnd.x, Sheet.staticLinesEnd.y + 100*elem), width=5)


    def draw_productinfo(self, screen, product):


        sourceName = Sheet.staticFont.render(product.name, True, "Black")
        destName = sourceName.get_rect(center=(450, 200))

        scores = [product.sante, product.environemental, product.budget]
        scoresRender, scoresRect = [], []

        for elem in range(len(scores)):
            scoresRender.append(Sheet.staticFont.render(str(scores[elem]), True, "Black"))
            scoresRect.append(scoresRender[elem].get_rect(center=(Sheet.staticTextPos[0] + 120, Sheet.staticTextPos[1] + elem * 100)))


        for elem in range(len(scoresRender)):
            screen.blit(scoresRender[elem], scoresRect[elem])

        screen.blit(sourceName, destName)
        product.draw(screen)

        mouse_pos = pygame.mouse.get_pos()
        Sheet.staticButton.changeColor(mouse_pos)
        Sheet.staticButton.update(screen)

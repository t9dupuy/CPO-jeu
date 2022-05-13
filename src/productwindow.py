
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

        product = Product("Cod", 4, 4, 3, [500, 400], [280, 170],
                          pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (64, 64)))


        running = True
        while running:

            mouse_pos = pygame.mouse.get_pos()


            screen.blit(background, (0, 0))

            Sheet.draw_background(background, screen)

            Sheet().draw_productinfo(screen, product)

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Sheet.staticButtons[0].checkForInput(mouse_pos):
                        pygame.quit()
                    elif Sheet.staticButtons[1].checkForInput(mouse_pos):
                        pygame.quit()

            pygame.display.flip()


        pygame.quit()

class Sheet:

    pygame.init()

    staticRect = pygame.Rect(1080/2-300/2, 720/2-500/2, 300, 500)
    staticFont =  pygame.font.Font("resources/fonts/Dunkin.otf", 50)
    staticBigFont = pygame.font.Font("resources/fonts/Dunkin.otf", 70)
    staticTextToShow = ["Nutri : ", "Envir : ", "Price : "]
    staticTextPos = (staticRect.left+130, staticRect.top+180)
    staticTextRender, staticTextRect = [], []


    staticLinesStart = pygame.Vector2(staticRect.left+10,staticTextPos[1]+50)
    staticLinesEnd = pygame.Vector2(staticRect.right-10, staticTextPos[1]+50)


    for elem in range(len(staticTextToShow)):
        staticTextRender.append(staticFont.render(staticTextToShow[elem], True, "Black"))
        staticTextRect.append(staticTextRender[elem].get_rect(center=(staticTextPos[0], staticTextPos[1] + elem*100)))

    staticButtons = (Button(color=(205, 92, 92), size=(200, 90), radius=10,
                             pos=((staticRect.left+staticRect.width/2), staticRect.bottom),
                             text_input="ADD", font_type="resources/fonts/Dunkin.otf", base_color="White",
                             hovering_color="Grey"), Button(color=(205, 92, 92), size=(35, 35), radius=10,
                          pos=((staticRect.right), staticRect.top),
                          text_input="X", font_type="resources/fonts/Dunkin.otf", base_color="White",
                          hovering_color="Grey"))




    @staticmethod
    def draw_background(self, screen):

        pygame.draw.rect(screen, 'White', Sheet.staticRect, 0, 20)

        for elem in range(len(Sheet.staticTextRender)):
            screen.blit(Sheet.staticTextRender[elem], Sheet.staticTextRect[elem])

        for elem in range(3) :
            pygame.draw.line(screen, 'Black',(Sheet.staticLinesStart.x, Sheet.staticLinesStart.y + 100*elem) , (Sheet.staticLinesEnd.x, Sheet.staticLinesEnd.y + 100*elem), width=5)


    def draw_productinfo(self, screen, product):


        source = Sheet.staticBigFont.render(product.name, True, (205, 92, 92))
        dest = source.get_rect(center=(Sheet.staticRect.left+205, Sheet.staticRect.top+65))

        scores = [product.sante, product.environemental, product.budget]
        scoresRender, scoresRect = [], []

        for elem in range(len(scores)):
            scoresRender.append(Sheet.staticFont.render(str(scores[elem]), True, "Black"))
            scoresRect.append(scoresRender[elem].get_rect(center=(Sheet.staticTextPos[0] + 120, Sheet.staticTextPos[1] + elem * 100)))


        for elem in range(len(scoresRender)):
            screen.blit(scoresRender[elem], scoresRect[elem])

        screen.blit(source, dest)
        screen.blit(pygame.transform.scale(product.sprite,(100,100)), (Sheet.staticRect.left+10,  Sheet.staticRect.top+20))

        mouse_pos = pygame.mouse.get_pos()

        for elem in range(2):
            Sheet.staticButtons[elem].changeColor(mouse_pos)
            Sheet.staticButtons[elem].update(screen)

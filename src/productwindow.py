from typing import List

import pygame
from src.menu import Button


class Sheet:
    pygame.init()

    window_w, window_h = 1080, 720

    staticRect = pygame.Rect(window_w/2 - 300/2, 150, 300, 500)
    staticFont = pygame.font.Font("resources/fonts/Dunkin.otf", 50)
    staticTextToShow = ["Nutri : ", "Envir : ", "Price : "]
    staticTextPos = (window_w/2, 300)
    staticTextRender, staticTextRect = [], []

    staticLinesStart = pygame.Vector2(staticTextPos[0] - 125, staticTextPos[1]+50)
    staticLinesEnd = pygame.Vector2(staticTextPos[0] + 125, staticTextPos[1]+50)

    for elem in range(len(staticTextToShow)):
        staticTextRender.append(staticFont.render(staticTextToShow[elem], True, "Black"))
        staticTextRect.append(staticTextRender[elem].get_rect(center=(staticTextPos[0], staticTextPos[1] + elem*100)))

    staticButton = Button(color=(205, 92, 92), size=(200, 90), radius=10,
                             pos=(window_w/2, 620),
                             text_input="ADD", font_type="resources/fonts/Dunkin.otf", base_color="White",
                             hovering_color="Grey")

    staticExit = Button(color=(205, 92, 92), size=(40, 40), radius=5,
                          pos=(window_w/2 + 300/2 - 10, 160),
                          text_input="X", font_type="resources/fonts/Dunkin.otf", base_color="White",
                          hovering_color="Grey")

    buttons = [staticButton, staticExit]

    @staticmethod
    def draw_background(screen):

        pygame.draw.rect(screen, 'White', Sheet.staticRect, 0, 20)

        for elem in range(len(Sheet.staticTextRender)):
            screen.blit(Sheet.staticTextRender[elem], Sheet.staticTextRect[elem])

        for elem in range(3):
            pygame.draw.line(screen, 'Black',(Sheet.staticLinesStart.x, Sheet.staticLinesStart.y + 100*elem) , (Sheet.staticLinesEnd.x, Sheet.staticLinesEnd.y + 100*elem), width=5)

    def draw_productinfo(self, screen, product):
        self.draw_background(screen)

        sourceName = Sheet.staticFont.render(product.name, True, "Black")
        destName = sourceName.get_rect(center=(self.window_w/2 + 50, 200))

        scores = [product.sante, product.environemental, product.budget]
        scoresRender, scoresRect = [], []

        for elem in range(len(scores)):
            scoresRender.append(Sheet.staticFont.render(str(scores[elem]), True, "Black"))
            scoresRect.append(scoresRender[elem].get_rect(center=(Sheet.staticTextPos[0] + 120, Sheet.staticTextPos[1] + elem * 100)))

        for elem in range(len(scoresRender)):
            screen.blit(scoresRender[elem], scoresRect[elem])

        screen.blit(sourceName, destName)
        screen.blit(pygame.transform.scale(product.sprite, (128, 128)), (self.window_w/2 - 150, 140))

        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.staticButton.checkForInput(mouse_pos):
                    return 1
                if self.staticExit.checkForInput(mouse_pos):
                    return -1

        return 0

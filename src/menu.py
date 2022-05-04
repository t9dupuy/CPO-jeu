import pygame

class Menu():

    def __init__(self):
        pygame.init()

        self.background = pygame.image.load("resources/wallpaper/market.jpg")

    def get_font(self, size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("resources/assets/font.ttf", size)

    def run(self):

        width = 1080
        length = 720

        font_= pygame.font.Font("resources/assets/font.ttf", 75)

        pygame.display.set_caption("Menu")
        screen = pygame.display.set_mode((width, length))

        running = True
        while running:

            screen.blit(self.background, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = pygame.font.Font("resources/assets/font.ttf", 100).render("MENU", True, "Black")
            menu_rect = menu_text.get_rect(center=(width / 2, length / 5))

            play_button = Button(image=pygame.image.load("resources/assets/Play Rect.png"), pos=(width/2, 2*length/5),
                                 text_input="PLAY", font=font_, base_color="Black", hovering_color="Grey")
            options_button = Button(image=pygame.image.load("resources/assets/Options Rect.png"), pos=(width/2, 3*length/5),
                                    text_input="OPTIONS", font=font_, base_color="Black",
                                    hovering_color="Grey")
            quit_button = Button(image=pygame.image.load("resources/assets/Quit Rect.png"), pos=(width/2, 4*length/5),
                                 text_input="QUIT", font=font_, base_color="Black", hovering_color="Grey")

            screen.blit(menu_text, menu_rect)

            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(screen)

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                    if options_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()



            pygame.display.flip()


        pygame.quit()

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
import pygame


class Menu:
    def __init__(self):
        self.background = pygame.image.load("resources/wallpaper/menu.jpg")
        self.background = pygame.transform.scale(self.background, (1080, 720))

    def run(self, screen):
        from __main__ import State

        width, height = screen.get_size()

        menu_text = pygame.font.Font("resources/fonts/pixels.ttf", 100).render("MENU", True, "White")
        menu_rect = menu_text.get_rect(center=(width / 2, height / 5))

        play_button = Button(color=(205, 92, 92), size=(width/2, height/7), radius=5, pos=(width/2, 2*height/5),
                             text_input="PLAY", font_type="resources/fonts/pixels.ttf", base_color="White",
                             hovering_color="Grey")
        options_button = Button(color=(205, 92, 92), size=(width/2, height/7), radius=5, pos=(width/2, 3*height/5),
                                text_input="OPTIONS", font_type="resources/fonts/pixels.ttf", base_color="White",
                                hovering_color="Grey")
        quit_button = Button(color=(205, 92, 92), size=(width/2, height/7), radius=5, pos=(width/2, 4*height/5),
                             text_input="QUIT", font_type="resources/fonts/pixels.ttf", base_color="White",
                             hovering_color="Grey")

        buttons = [play_button, options_button, quit_button]

        running = True
        while running:

            clk = pygame.time.Clock()

            screen.blit(self.background, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()

            screen.blit(menu_text, menu_rect)

            for button in buttons:
                button.changeColor(menu_mouse_pos)
                button.update(screen)

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        return State.GAME
                    if options_button.checkForInput(menu_mouse_pos):
                        return State.PARAM
                    if quit_button.checkForInput(menu_mouse_pos):
                        return None

            pygame.display.update()

            clk.tick(60)


class Button:
    def __init__(self, color, size, radius, pos, text_input, font_type, base_color, hovering_color):
        self.r_color, self.g_color, self.b_color = color
        self.x_size, self.y_size = size
        self.radius = radius
        self.x_pos, self.y_pos = pos
        self.base_color, self.hovering_color = base_color, hovering_color

        self.font = pygame.font.Font(font_type, int(self.y_size - 20))

        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        self.x_corner = self.x_pos - (self.x_size/2)
        self.y_corner = self.y_pos - (self.y_size/2)

        self.color_rect = pygame.Color(self.r_color, self.g_color, self.b_color)
        self.rect = pygame.Rect(self.x_corner, self.y_corner, self.x_size, self.y_size)

        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        pygame.draw.rect(screen, self.color_rect, self.rect, 0, self.radius)
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

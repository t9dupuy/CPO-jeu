import pygame
from src.menu import Button


class Param:

    def __init__(self):
        self.difficulte = 1
        self.music = True
        pygame.mixer.music.load("resources/music/track.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def draw(self):
        # pygame.init() will initialize all
        # imported module
        from __main__ import State

        clock = pygame.time.Clock()

        # creation screen
        screen = pygame.display.set_mode([1080, 720])

        # creation font
        base_font = pygame.font.Font("resources/assets/font.ttf", 40)
        base_font_titre = pygame.font.Font("resources/assets/font.ttf", 60)
        base_font.set_bold(True)
        base_font_titre.set_bold(True)

        # import image de fond et adaptation taille
        image_fond = pygame.image.load("resources/wallpaper/param.jpg")
        image_fond = pygame.transform.scale(image_fond, [1400, 720])

        # creation titre
        titre = base_font_titre.render("Paramètres", True, pygame.Color("black"))
        recttitre = titre.get_rect()
        recttitre.center = (500, 50)

        # creation difficultÃ©
        dif = base_font.render("Difficulté", True, pygame.Color("black"))
        rectdif = dif.get_rect()
        rectdif.center = (250, 240)

        # creation music
        music = base_font.render("Musique", True, pygame.Color("black"))
        rectmusic = music.get_rect()
        rectmusic.center = (750, 240)

        # creation liste de bouton
        list_button = []
        # create button difficulte
        button_dif_color = (100, 150, 200)

        button_dif_1 = Button(color=button_dif_color, size=(100, 100), radius=5, pos=(100, 320), text_input="1", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_dif_1)
        button_dif_2 = Button(color=button_dif_color, size=(100, 100), radius=5, pos=(220, 320), text_input="2", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_dif_2)
        button_dif_3 = Button(color=button_dif_color, size=(100, 100), radius=5, pos=(340, 320), text_input="3", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_dif_3)

        # create button music
        button_music_color = (255, 0, 0)
        button_music_active = Button(color=button_music_color, size=(250, 100), radius=5, pos=(750, 320), text_input="AVEC", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_music_active)
        button_music_inactive = Button(color=button_music_color, size=(250, 100), radius=5, pos=(750, 450), text_input="SANS", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_music_inactive)

        # create button quit
        button_quit = Button(color=(0, 0, 0), size=(400, 100), radius=5, pos=(250, 600), text_input="QUITTER", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
        list_button.append(button_quit)

        while True:

            # recup position souris
            menu_mouse_pos = pygame.mouse.get_pos()

            # activation des boutons Ã  l'Ã©tat actuel
            if self.difficulte == 1:
                button_dif_1.color_rect = pygame.Color(0, 0, 0)
            elif self.difficulte == 2:
                button_dif_2.color_rect = pygame.Color(0, 0, 0)
            else:
                button_dif_3.color_rect = pygame.Color(0, 0, 0)

            if self.music:
                button_music_active.color_rect = pygame.Color(150, 0, 0)
            else:
                button_music_inactive.color_rect = pygame.Color(150, 0, 0)

            for event in pygame.event.get():

                # if user types QUIT then the screen will close
                if event.type == pygame.QUIT:
                    return None

                # gestion des Ã©venements de la souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_dif_1.checkForInput(menu_mouse_pos):
                        self.difficulte = 1
                        button_dif_1.color_rect = pygame.Color(0, 0, 0)
                        button_dif_2.color_rect = button_dif_color
                        button_dif_3.color_rect = button_dif_color
                    if button_dif_2.checkForInput(menu_mouse_pos):
                        self.difficulte = 2
                        button_dif_2.color_rect = pygame.Color(0, 0, 0)
                        button_dif_1.color_rect = button_dif_color
                        button_dif_3.color_rect = button_dif_color
                    if button_dif_3.checkForInput(menu_mouse_pos):
                        self.difficulte = 3
                        button_dif_3.color_rect = pygame.Color(0, 0, 0)
                        button_dif_2.color_rect = button_dif_color
                        button_dif_1.color_rect = button_dif_color
                    if button_music_active.checkForInput(menu_mouse_pos):
                        pygame.mixer.music.unpause()
                        self.music = True
                        button_music_active.color_rect = pygame.Color(150, 0, 0)
                        button_music_inactive.color_rect = button_music_color
                    if button_music_inactive.checkForInput(menu_mouse_pos):
                        pygame.mixer.music.pause()
                        self.music = False
                        button_music_inactive.color_rect = pygame.Color(150, 0, 0)
                        button_music_active.color_rect = button_music_color
                    if button_quit.checkForInput(menu_mouse_pos):
                        return State.MAIN_MENU

            # affichage fond d'Ã©cran
            screen.blit(image_fond, (0, 0))

            # print title, difficulte, music
            screen.blit(titre, recttitre)
            screen.blit(dif, rectdif)
            screen.blit(music, rectmusic)

            # affichage bouton
            for button in list_button:
                button.changeColor(menu_mouse_pos)
                button.update(screen)

            # display.flip() will update only a portion of the
            # screen to updated, not full area
            pygame.display.flip()

            # clock.tick(60) means that for every second at most
            # 60 frames should be passed.
            clock.tick(60)

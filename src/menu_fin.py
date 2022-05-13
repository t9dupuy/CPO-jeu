import pygame
from src.menu import Button


def draw(score):
    from __main__ import State
    # pygame.init() will initialize all
    # imported module
    clock = pygame.time.Clock()

    # creation screen
    screen = pygame.display.set_mode([1080, 720])

    # creation font
    base_font = pygame.font.Font("resources/assets/font.ttf", 40)
    base_font_titre = pygame.font.Font("resources/assets/font.ttf", 60)
    base_font.set_bold(True)
    base_font_titre.set_bold(True)

    # import image de fond et adaptation taille
    image_fond = pygame.image.load("resources/wallpaper/1.jpg")
    image_fond = pygame.transform.scale(image_fond, [1080, 720])

    # creation titre
    titre = base_font_titre.render("FIN DE PARTIE", True, pygame.Color("black"))
    recttitre = titre.get_rect()
    recttitre.center = (500, 50)

    # creation affichage score
    af_score = base_font_titre.render("SCORE : ", True, pygame.Color("black"))
    rectscore = af_score.get_rect()
    rectscore.center = (400, 200)
    score_final = score[0]+score[1]+score[2]
    af_score_2 = base_font_titre.render(str(score_final), True, pygame.Color("black"))
    rectscore_2 = af_score_2.get_rect()
    rectscore_2.center = (650, 200)

    list_button = []
    # create button quit
    button_quit = Button(color=(0, 0, 0), size=(400, 100), radius=5, pos=(500, 600), text_input="QUITTER", font_type="resources/fonts/pixels.ttf", base_color="White", hovering_color="Grey")
    list_button.append(button_quit)

    while True:

        # recup position souris
        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit.checkForInput(menu_mouse_pos):
                    return State.MAIN_MENU

        # affichage fond d'écran
        screen.blit(image_fond, (0, 0))

        screen.blit(titre, recttitre)
        screen.blit(af_score, rectscore)
        screen.blit(af_score_2, rectscore_2)

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

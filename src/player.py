import pygame


class Player:
    """
    A class used to represent a player.

    Attributes
    ----------
    sprites : dict[str, list[pygame.image]]
        a dictionary with all the sprites needed to draw the player and its trolley.
    pos_rel : list[float, 2]
        position of the player relative to the screen/window (used to draw the player).
    facing : str
        direction the player is currently facing. Possible values are {'front', 'back', 'left', 'right'}.
    walking : bool
        whether the player is walking or not (idle).

    Methods
    -------
    draw(screen):
        Draw the player and its trolley on the specified screen.
    """
    def __init__(self):
        # Dictionary of sprites
        self.sprites: dict[str, list[pygame.image]] = dict()
        self.__load_images()

        # Position relative to the screen
        self.pos_rel: list[float, 2] = [500, 600]

        # Information about the player
        self.facing: str = 'back'
        self.walking: bool = False

        # Counter for sprites (animation of the player)
        self.__count: int = 0

    def __load_images(self):
        """
        Loads all the images of the player and its trolley in the 'sprites' dictionary.
        """
        front = [pygame.image.load("resources/player/p1/idle/front.png"),
                 pygame.image.load("resources/player/p1/push/front1.png"),
                 pygame.image.load("resources/player/p1/push/front2.png"),
                 pygame.image.load("resources/player/p1/push/front3.png"),
                 pygame.image.load("resources/player/p1/push/front4.png"),
                 pygame.image.load("resources/player/p1/push/front5.png"),
                 pygame.image.load("resources/player/p1/push/front6.png")]

        for i, image in enumerate(front):
            front[i] = pygame.transform.scale(image, (64, 128))

        front.append(pygame.transform.scale(pygame.image.load("resources/cart/front.png"), (128, 128)))

        self.sprites['front'] = front

        back = [pygame.image.load("resources/player/p1/idle/back.png"),
                pygame.image.load("resources/player/p1/push/back1.png"),
                pygame.image.load("resources/player/p1/push/back2.png"),
                pygame.image.load("resources/player/p1/push/back3.png"),
                pygame.image.load("resources/player/p1/push/back4.png"),
                pygame.image.load("resources/player/p1/push/back5.png"),
                pygame.image.load("resources/player/p1/push/back6.png")]

        for i, image in enumerate(back):
            back[i] = pygame.transform.scale(image, (64, 128))

        back.append(pygame.transform.scale(pygame.image.load("resources/cart/back.png"), (128, 128)))

        self.sprites['back'] = back

        left = [pygame.image.load("resources/player/p1/idle/left.png"),
                pygame.image.load("resources/player/p1/push/left1.png"),
                pygame.image.load("resources/player/p1/push/left2.png"),
                pygame.image.load("resources/player/p1/push/left3.png"),
                pygame.image.load("resources/player/p1/push/left4.png"),
                pygame.image.load("resources/player/p1/push/left5.png"),
                pygame.image.load("resources/player/p1/push/left6.png")]

        for i, image in enumerate(left):
            left[i] = pygame.transform.scale(image, (64, 128))

        left.append(pygame.transform.scale(pygame.image.load("resources/cart/left.png"), (128, 128)))

        self.sprites['left'] = left

        right = [pygame.image.load("resources/player/p1/idle/right.png"),
                 pygame.image.load("resources/player/p1/push/right1.png"),
                 pygame.image.load("resources/player/p1/push/right2.png"),
                 pygame.image.load("resources/player/p1/push/right3.png"),
                 pygame.image.load("resources/player/p1/push/right4.png"),
                 pygame.image.load("resources/player/p1/push/right5.png"),
                 pygame.image.load("resources/player/p1/push/right6.png")]

        for i, image in enumerate(right):
            right[i] = pygame.transform.scale(image, (64, 128))

        right.append(pygame.transform.scale(pygame.image.load("resources/cart/right.png"), (128, 128)))

        self.sprites['right'] = right

    def draw(self, screen: pygame.display):
        """
        Draw the player and its trolley on the specifier screen.

        :param screen: 'pygame.display' screen to render on.
        """
        # Trolley
        # when player is facing back (trolley has to be UNDER the player)
        if self.facing == 'back':
            screen.blit(self.sprites['back'][7], (self.pos_rel[0] - 2, self.pos_rel[1] - 20))

        # Player
        if self.walking:
            # Rolling through all 6 animation images (image changes every 'frame_per_image' frames).
            frame_per_image = 6
            self.__count += 1
            self.__count %= (6 * frame_per_image)
            screen.blit(self.sprites[self.facing][1 + int(self.__count / frame_per_image)], self.pos_rel)
        else:
            screen.blit(self.sprites[self.facing][0], self.pos_rel)

        # Trolley
        # when player is facing front
        if self.facing == 'front':
            screen.blit(self.sprites['front'][7], (self.pos_rel[0] - 7, self.pos_rel[1] + 70))
        # when player is facing left
        if self.facing == 'left':
            screen.blit(self.sprites['left'][7], (self.pos_rel[0] - 83, self.pos_rel[1] + 20))
        # when player is facing right
        if self.facing == 'right':
            screen.blit(self.sprites['right'][7], (self.pos_rel[0] + 58, self.pos_rel[1] + 20))

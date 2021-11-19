import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__() #inherit attributes from Sprite

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("./Images/alien.bmp")
        self.rect = self.image.get_rect()

    def update(self, Direction):
        """
        Move the aliens depending on the direction indicated
        :param Direction: The direction on the screen to move all the aliens in the group
        :return: None
        """

        if Direction == "Right":
            self.rect.right += 1

        if Direction == "Down":
            self.rect.bottom += 1

        if Direction == "Left":
            self.rect.left -= 1

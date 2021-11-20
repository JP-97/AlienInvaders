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

        #cast rect to floats so you can fine tune the speed
        # self.rect.right = float(self.rect.right)
        # self.rect.bottom = float(self.rect.bottom)
        # self.rect.left = float(self.rect.left)

    def update(self, Direction):
        """
        Move the aliens depending on the direction indicated
        :param Direction: The direction on the screen to move all the aliens in the group
        :return: None
        """

        if Direction == "Right":
            self.rect.right += self.ai_game.settings.alien_speed_left_to_right

        if Direction == "Down":
            self.rect.bottom += self.ai_game.settings.alien_drop_speed

        if Direction == "Left":
            self.rect.left -= self.ai_game.settings.alien_speed_left_to_right

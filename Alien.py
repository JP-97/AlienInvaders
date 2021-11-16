import pygame

class Alien():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("./Images/alien.bmp")
        self.rect = self.image.get_rect()

        ####update later - this aligns the alien rect with the display midtop
        self.rect.topleft = self.screen_rect.midtop

    def blitme(self):
        """
        Used to draw the aliens to the screen
        :return: None
        """
        self.screen.blit(self.image, self.rect)
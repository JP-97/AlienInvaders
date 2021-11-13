import pygame

class Ship:
    """
    This class will be used to manage the ship
    """

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect() #returns rect object corresponding to ship surface

        self.rect.midbottom = self.screen_rect.midbottom #align ship midbottom with AI screen midbottom

        self.speed = 10 #Adjust this to control the speed in which the ship moves
    def blitme(self):
        """
        Draw the ship at its current location
        """

        self.screen.blit(self.image, self.rect)

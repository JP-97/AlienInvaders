import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #need to inherit from Sprite so that we can leverage pygame.sprite.Group() class functionalities
    def __init__(self, ai_game):
        super().__init__() #inherit the properties of the sprite class

        self.ai_game = ai_game
        self.ship_rect = ai_game.ship.rect
        self.rect = pygame.Rect(self.ship_rect.midtop, (ai_game.settings.bullet_width, ai_game.settings.bullet_height))

    def blitme(self):
        """
        Draws a bullet on the AI screen
        :return: None
        """
        pygame.draw.rect(self.ai_game.screen, self.ai_game.settings.bullet_color, self.rect)

    def update(self):
        """
        Overrides the pygame.sprite.Group.update() method and applied update to all sprites in the bullets group

        Checks to see if the user fired the bullet. If so, updates the bullet's rect location accordingly
        :return: None
        """
        self.rect.y -= self.ai_game.settings.bullet_speed


    def reset_rect(self):
        """
        Draw the bullet such that it is aligned with the midtop of the ship
        :return: pygame.Rect()
        """
        self.rect = pygame.Rect(self.ship_rect.midtop, (self.ai_game.settings.bullet_width, self.ai_game.settings.bullet_height))
import pygame
from pygame.sprite import Sprite
import random

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

    def update(self, direction = 1):
        """
        Overrides the pygame.sprite.Group.update() method and applied update to all sprites in the bullets group

        Checks to see if the user fired the bullet. If so, updates the bullet's rect location accordingly
        :direction: 1 will cause the bullets to travel upwards, -1 will cause them to travel downwards
        :return: None
        """
        self.rect.y = self.rect.y - (direction * self.ai_game.settings.bullet_speed)


    def reset_rect(self):
        """
        Draw the bullet such that it is aligned with the midtop of the ship
        :return: pygame.Rect()
        """
        self.rect = pygame.Rect(self.ship_rect.midtop, (self.ai_game.settings.bullet_width, self.ai_game.settings.bullet_height))


class AlienBullet(Bullet):
    def __init__(self, ai_game):

        super().__init__(ai_game)
        self.ai_game = ai_game

        #randomly chose one of the aliens to fire the bullet
        alien_list = self.ai_game.aliens.sprites()
        rand_index = random.randint(0, len(alien_list) - 1)
        alien_rect = alien_list[rand_index].rect
        self.rect = pygame.Rect(alien_rect.midbottom, (self.ai_game.settings.alien_bullet_width, self.ai_game.settings.alien_bullet_height))


    def blitme_alien(self):
        """
        Draws a bullet being fired from one of the alien objects
        :return: None
        """

        pygame.draw.rect(self.ai_game.screen, self.ai_game.settings.bullet_color, self.rect)
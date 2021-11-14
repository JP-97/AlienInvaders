import pygame

class Bullet():
    def __init__(self, ai_game):

        self.ai_game = ai_game
        self.ship_rect = ai_game.ship.rect
        self.rect = pygame.Rect(self.ship_rect.midtop, (ai_game.settings.bullet_width, ai_game.settings.bullet_height))
        self.fired = False

    def blitme(self):
        """
        Draws a bullet on the AI screen
        :return:
        """
        pygame.draw.rect(self.ai_game.screen, self.ai_game.settings.bullet_color, self.rect)

    def is_fired(self):
        """
        Checks to see if the user fired the bullet. If so, updates the bullet's rect location accordingly
        :return: None
        """
        if self.fired:
            self.rect.y -= 5
            print("Firing bullet")

        #reset the bullet once it has reached the top of the screen or if it has not been fired
        if self.rect.top <= 0 or not(self.fired):
            self.reset_rect()
            self.fired = False

    def reset_rect(self):
        """
        Draw the bullet such that it is aligned with the midtop of the ship
        :return: pygame.Rect()
        """
        self.rect = pygame.Rect(self.ship_rect.midtop, (self.ai_game.settings.bullet_width, self.ai_game.settings.bullet_height))
import pygame

class Bullet():
    def __init__(self, ai_game):

        self.ai_game = ai_game
        self.ship_rect = ai_game.ship.rect
        self.rect = pygame.Rect(self.ship_rect.midtop, (ai_game.settings.bullet_width, ai_game.settings.bullet_height))


    def blitme(self):
        """
        Draws a bullet on the AI screen
        :return:
        """
        # self.ai_game.screen.blit(self.rect, self.ship_rect)
        pygame.draw.rect(self.ai_game.screen, self.ai_game.settings.bullet_color, self.rect)

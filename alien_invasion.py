"""
Main module where Alien Invasion game is created

"""

import sys
import pygame
from settings import Settings
from Ship import Ship
from bullet import Bullet

class AlienInvasion:
    """
    Overall class to manage game assets and behaviour
    """

    def __init__(self):
        pygame.init()
        self.settings = Settings() #Create settings object
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #instantiate ship object
        self.bullet = Bullet(self) #instantiate bullet object

    def run_game(self):
        """
        Initiates the main loop that runs the game
        :return: None
        """
        while True:
            self._check_events() #execute event checking loop
            self._update_screen()

    def _check_events(self):
        """
        Helper method which responds to keypresses and mouse events.
        :return: None
        """
        pygame.key.set_repeat(35) #allows for the creations of continuous KEYDOWN events when key is held down

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and ((self.ship.rect.bottomright[0] + self.ship.speed) < self.ship.screen_rect.bottomright[0]): #conditional statement here just ensures that the ship can't go off the screen
                    self.ship.rect.x += self.ship.speed

                if event.key == pygame.K_LEFT and ((self.ship.rect.bottomleft[0] - self.ship.speed) > self.ship.screen_rect.bottomleft[0]):
                    self.ship.rect.x -= self.ship.speed

                if event.key == pygame.K_q: #enables quitting the game when pressing 'q'
                    sys.exit()

                if event.key == pygame.K_SPACE and not(self.bullet.fired): #check to see if the bullet has already been fired or not
                    self.bullet.fired = True


    def _update_screen(self):
        """
        Helper method which updates the screen
        :return: None
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Update the bullet
        self.bullet.is_fired()
        self.bullet.blitme()

        #Update the entire screen
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
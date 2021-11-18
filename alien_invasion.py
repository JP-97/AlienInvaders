"""
Main module where Alien Invasion game is created

"""

import sys
import pygame
from settings import Settings
from Ship import Ship
from bullet import Bullet
from Alien import Alien

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
        self.aliens_full = False  # will be used to indicate when the screen is full of aliens

        #instantiate groups for aliens and bullets
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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
                active_keys = pygame.key.get_pressed() #returns a list of all the actively pressed keys

                ####    Simultaneous Presses    ####
                if active_keys[pygame.K_RIGHT] and active_keys[pygame.K_SPACE]:
                    self.bullets.add(Bullet(self))
                    self.ship.update_pos('Right')

                elif active_keys[pygame.K_LEFT] and active_keys[pygame.K_SPACE]:
                    self.bullets.add(Bullet(self))
                    self.ship.update_pos('Left')

                ####    Individual Presses  ####
                elif event.key == pygame.K_q: #enables quitting the game when pressing 'q'
                    sys.exit()

                elif event.key == pygame.K_RIGHT:
                    self.ship.update_pos('Right')

                elif event.key == pygame.K_LEFT:
                    self.ship.update_pos('Left')

                elif event.key == pygame.K_SPACE:
                    self.bullets.add(Bullet(self)) #add a new bullet object to the active bullets group each time the spacebar is pressed

    def _create_fleet(self):
        alien = Alien(self)
        available_space_x = self.settings.screen_width
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        number_of_aliens = available_space_x//(2*alien_width) #floor division of screen by alien width to allow for margin

        for row in range(1, 5):
            for alien_number in range(number_of_aliens):
                alien = Alien(self)
                alien.rect.left = alien_number * 2 * alien_width
                alien.rect.top = row * 2 * alien_height
                self.aliens.add(alien)

    def _update_screen(self):
        """
        Helper method which updates the screen
        :return: None
        """
        #Add background color and draw ship
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        self._update_bullets()
        self.aliens.draw(self.screen)

        #Update the entire screen
        pygame.display.flip()

    def _update_bullets(self):
        """
        Take care of the bullet updates required in the _update_screen loop
        :return: None
        """
        # Update all bullet positions in bullets group. Automatically gets applied
        # to all sprites in the group
        self.bullets.update()

        # Draw all the bullets to the screen
        for bullet in self.bullets.sprites():
            bullet.blitme()

        # delete bullets off the screen to preserve memory. Need to use a copy of the bullets
        # group since you shouldn't modify a list size while iterating.
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                bullet.remove(self.bullets)


### Create the main game loop ###

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
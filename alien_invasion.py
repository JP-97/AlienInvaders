"""
Main module where Alien Invasion game is created

"""

import sys
import pygame
from settings import Settings
from Ship import Ship
from bullet import Bullet
from Alien import Alien
import time
from Screen import Screen
from bullet import AlienBullet


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

        #instantiate groups for aliens and bullets
        self.bullets = pygame.sprite.Group()

        #create aliens and draw the initial fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.end_screen = Screen()
        self.alien_bullets = pygame.sprite.Group()

        #initialize scoreboard
        self.score = 0
        self.scoreboard = Screen()
        self.scoreboard_surface = self.scoreboard.create_screen(str(self.score),size = 50, color=(0,0,0))
        self.scoreboard.rect = (1100,10)


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
                    self._fire_bullet()
                    self.ship.update_pos('Right')

                elif active_keys[pygame.K_LEFT] and active_keys[pygame.K_SPACE]:
                    self._fire_bullet()
                    self.ship.update_pos('Left')

                ####    Individual Presses  ####
                elif event.key == pygame.K_q: #enables quitting the game when pressing 'q'
                    sys.exit()

                elif event.key == pygame.K_RIGHT:
                    self.ship.update_pos('Right')

                elif event.key == pygame.K_LEFT:
                    self.ship.update_pos('Left')

                elif event.key == pygame.K_SPACE:
                    self._fire_bullet() #add a new bullet object to the active bullets group each time the spacebar is pressed

    def _create_fleet(self):
        """
        Helper function used to draw the initial fleet
        :return: None
        """
        alien = Alien(self)
        available_space_x = self.settings.screen_width
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        number_of_aliens = available_space_x//(4*alien_width) #floor division of screen by alien width to allow for margin

        for row in range(1, 5):
            for alien_number in range(number_of_aliens):
                alien = Alien(self)
                alien.rect.left = alien_number * 2 * alien_width
                alien.rect.top = row * 2 * alien_height
                self.aliens.add(alien)

    def _fire_bullet(self):
        """
        Helper method which checks to ensure that no two bullets are fired in too close of a succession
        :return: None
        """

        #ship bullets
        if time.time() - self.settings.bullet_timer > self.settings.bullet_fired_threshold:
            self.bullets.add(Bullet(self))
            self.settings.bullet_timer = time.time()  # reset the bullet timer

    def _move_fleet(self):
        """
        Move the fleet of aliens to the right until it hits the edge of the screen, then down, then to the left until:
        1. All the aliens have been shot down
        2. An alien collides with the ship
        3. An alien reaches the bottom of the screen
        :return: None
        """

        #find the rightmost alien in the group to use as reference for when the fleet hits the right side of the screen
        rightmost_alien = 0
        bottom_alien = 0
        leftmost_alien = 1200

        for alien in self.aliens:
            if alien.rect.right > rightmost_alien:
                rightmost_alien = alien.rect.right

            if alien.rect.bottom > bottom_alien:
                bottom_alien = alien.rect.bottom

            if alien.rect.left < leftmost_alien:
                leftmost_alien = alien.rect.left

        if self.settings.direction == 1:
            if rightmost_alien + 15 < self.settings.screen_width:
                self.aliens.update("Right")

            else:
                self.settings.direction = -1
                self.aliens.update("Down")

        elif self.settings.direction == -1:
            if leftmost_alien - 15 > 0:
                self.aliens.update("Left")

            else:
                self.aliens.update("Down")
                self.settings.direction = 1

        # Add alien bullets if time conditions are met
        if time.time() - self.settings.bullet_timer_alien > self.settings.bullet_fired_threshold_alien:
            self.alien_bullets.add(AlienBullet(self))
            self.settings.bullet_timer_alien = time.time() #reset the timer

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

    def _update_alien_bullets(self):
        """
        Update the bullets fired from the alien ships
        :return: None
        """

        self.alien_bullets.update(direction = -1)

        for bullet in self.alien_bullets.sprites():
            bullet.blitme_alien()

        for bullet in self.alien_bullets.copy():
            if bullet.rect.y >= 1200:
                bullet.remove(self.bullets)

    def _have_collided(self):
        """
        Helper method to detect collisions between:
        1. Bullets fired from ship and aliens
        2. Ship and aliens
        3. Alien bullets and ship (coming soon)
        :return: None
        """
        collided_aliens_and_bullets = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        collided_aliens_and_ship = pygame.sprite.spritecollide(self.ship,self.aliens, False)
        collided_alien_bullets_and_ship = pygame.sprite.spritecollide(self.ship, self.alien_bullets, False)

        if collided_aliens_and_ship:
            self._draw_end_screen()

        #10 points for each alien shot down
        if collided_aliens_and_bullets:
            self.score += 10
            # print(len(collided_aliens_and_bullets))
            print(self.score)

        if collided_alien_bullets_and_ship:
            self._draw_end_screen()

    def _draw_end_screen(self):
        """
        Logic required to apply a black background and print the scoreboard to the screen
        :return:
        """
        self.settings.bg_color = (0, 0, 0)
        self.screen.fill(self.settings.bg_color)
        self.end_screen_surface = self.end_screen.create_screen("GAME OVER", size = 75)
        self.scoreboard_surface = self.scoreboard.create_screen(f"YOUR FINAL SCORE WAS : {str(self.score)}", size=50, color=(255,255,255))
        self.scoreboard.rect = (350, 500)
        self.screen.blit(self.end_screen_surface, (350,300))
        self.screen.blit(self.scoreboard_surface, self.scoreboard.rect)

        #Note: We need to update the screen within this helper function so that we can exit
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """
        Helper method which updates the screen
        :return: None
        """
        # Add background color and draw ship
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        self._update_bullets()
        self._have_collided()
        self.aliens.draw(self.screen)
        self._update_alien_bullets()
        self._move_fleet()

        # update the score
        self.scoreboard_surface = self.scoreboard.create_screen(str(self.score), size=50, color=(0, 0, 0))
        self.screen.blit(self.scoreboard_surface, self.scoreboard.rect)

        # Update the entire screen
        pygame.display.flip()

### Create the main game loop ###

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
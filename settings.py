import time

class Settings:
    """
    This class will hold all of the relevant settings for the game instance
    """

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #bullet settings
        self.bullet_color = (0,0,0)
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.alien_bullet_width = 6
        self.alien_bullet_height = 20
        self.bullet_timer = time.time()
        self.bullet_timer_alien = time.time()
        self.bullet_fired_threshold = 0.5
        self.bullet_fired_threshold_alien = 2

        #alien settings
        self.direction = 1
        self.alien_speed_left_to_right = 1
        self.alien_drop_speed = 15
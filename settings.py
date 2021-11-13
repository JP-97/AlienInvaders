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
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
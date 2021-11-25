import pygame

class Screen:
    def __init__(self):
        self.font = None
        self.font_size = None
        self.font_surface = None
        self.color = None
        self.text = None
        self.style = None
        self.rect = (0,0)
        pygame.font.init()


    def create_screen(self, text, style= 'Comic Sans MS', size = 30, color = (255,255,255)):
        """
        Create and return font surface
        :param text: Text to be written to the screen
        :param font_size: Size of text to be written
        :param color: Color of text to be written
        :return: pygame.Surface() object
        """
        self.text = text
        self.font_size = size
        self.color = color
        self.style = style

        #create the Font object and corresponding Surface
        self.font = pygame.font.SysFont(self.style, self.font_size)
        self.font_surface = self.font.render(self.text, False, self.color)

        return self.font_surface
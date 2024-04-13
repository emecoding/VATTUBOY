import pygame

from VATTUBOY.resources.resource import Resource

class Font(Resource):
    def __init__(self, name, source_file, size, check_source=True):
        super().__init__(name)
        self.__source_file = source_file
        self.__size = size
        self.__pygame_font = pygame.font.Font(self._check_source(source_file) if check_source else source_file, self.__size)

    def create_text_surface_object(self, text, antialias, color, bg_color=None):
        return self.__pygame_font.render(text, antialias, color, bg_color)
    

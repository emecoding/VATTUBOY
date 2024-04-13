import pygame

from VATTUBOY.GUI.surface import Surface

class Window:
    def __init__(self, width, height, caption):
        self.__width = width
        self.__height = height
        self.__caption = caption

        self.__should_close = False

        self.__my_surfaces = []

        self.__display = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__caption)


    def set_surfaces(self, surfaces): #Every scene and game has its own surfaces.
        self.__my_surfaces = surfaces

    def update_window(self):
        pygame.display.update()

    def render_window(self):
        self.__display.fill((255, 255, 255))

        for surface in self.__my_surfaces:
            self.__display.blit(surface.get_pygame_surface(), (surface.get_pos()))
            surface.render()

    
    def set_should_close(self, val): self.__should_close = val

    def should_close(self): return self.__should_close
    def get_width(self): return self.__width
    def get_height(self): return self.__height

    def window_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.set_should_close(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_should_close(True)
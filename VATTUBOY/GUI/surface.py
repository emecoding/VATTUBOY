import pygame

from VATTUBOY.GUI.GUIComponent import GUIComponent

class Surface:
    def __init__(self, x, y, width, height, bg_color=(255, 255, 255)):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__bg_color = bg_color

        self.__my_gui_components = []

        self.__m_Sufrace = pygame.Surface((self.__width, self.__height))

    def add_gui_component(self, x, y, width, height):
        component = GUIComponent(x, y, width, height)
        component.initialize()
        self.__my_gui_components.append(component)
        return component

    def set_bg_color(self, color): self.__bg_color = color

    def get_pos(self): return (self.__x, self.__y)
    def get_pygame_surface(self): return self.__m_Sufrace
    def get_gui_components(self): return self.__my_gui_components

    def render(self):
        self.__m_Sufrace.fill(self.__bg_color)
        
        for gui_component in self.__my_gui_components:
            gui_component.render(self.__m_Sufrace)
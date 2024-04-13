import pygame

import VATTUBOY.resources.resourceManager

class GUIComponent:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.is_interactable = True
        self.is_hovered_on = False

        self.idle_bg_color = (0, 0, 0)
        self.hover_bg_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.text_bg_color = (0, 0, 0)

        self.text = None
        self.antialias = False
        self.font_name = None

        self.map_to_button = None

    def initialize(self):
        self.font_name = VATTUBOY.resources.resourceManager.RESOURCES_CONFIG["default_font"]

    def render(self, pygame_surface):
        pygame.draw.rect(pygame_surface, self.get_current_color(), self.get_pygame_rect())
        if self.text != None:
            font = VATTUBOY.resources.resourceManager.get_resource(self.font_name)
            text_obj = font.create_text_surface_object(self.text, self.antialias, self.text_color, bg_color=self.text_bg_color)
            pygame_surface.blit(text_obj, self.get_text_rect(text_obj))

    def get_pygame_rect(self): return (self.x, self.y, self.width, self.height)
    def get_text_rect(self, text_obj): 
        text_rect = text_obj.get_rect()
        text_rect.center = (self.x + self.width/2, self.y + self.height/2)
        return text_rect

    def get_current_color(self): #Get the current color of the gui component based on wheter it is selected, hovered on or something else.
        if self.is_hovered_on:
            return self.hover_bg_color

        return self.idle_bg_color
    
        
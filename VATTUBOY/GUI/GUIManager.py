import pygame

from VATTUBOY.GUI.window import Window

from VATTUBOY.scenes.mainmenu import MainMenu
import VATTUBOY.input.inputManager

from debug import *

class GUIManager:
    def __init__(self, window_width, window_height, window_caption):
        pygame.init()

        self.window = Window(window_width, window_height, window_caption)

        self.__scenes = [MainMenu()] #When game chosen, load all the game scenes into the scenes list and play from there.
        self.__current_scene_index = 0

        self.__current_interacting_gui_component = 0

    def change_scene(self, index):
        self.__current_scene_index = int(index)
        if self.__current_scene_index >= len(self.__scenes):
            debug_error(f"invalid scene index: {self.__current_scene_index}")

        self.__scenes[self.__current_scene_index].initialize(self.window)


    def handle_interacting_with_GUI(self):
        interactable_gui_components = self.__scenes[self.__current_scene_index].get_interactable_gui_components()
        if len(interactable_gui_components) <= 0:
            return
        
        if not VATTUBOY.input.inputManager.atleast_one_joystick_is_connected():
            return
        
        gui_component_index = 0
        for gui_component in interactable_gui_components:
            if gui_component.map_to_button == None:
                continue
            
            if VATTUBOY.input.inputManager.get_joystick_button(0, gui_component.map_to_button):
                interactable_gui_components[self.__current_interacting_gui_component].is_hovered_on = False
                self.__current_interacting_gui_component = gui_component_index

            gui_component_index += 1

        if self.__current_interacting_gui_component >= len(interactable_gui_components) or self.__current_interacting_gui_component < 0:
            self.__current_interacting_gui_component = 0
        
        interactable_gui_components[self.__current_interacting_gui_component].is_hovered_on = True
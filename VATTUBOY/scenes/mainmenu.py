from VATTUBOY.scenes.scene import Scene

from VATTUBOY.input.inputManager import CROSS_BUTTON, OPTIONS_BUTTON, CIRCLE_BUTTON

class MainMenu(Scene):
    def __init__(self):
        super().__init__("Main Menu")
        
    def initialize(self, window):
        super().initialize(window)

        window_width = window.get_width()
        window_height = window.get_height()

        main_surface = self.add_surface(0, 0, window_width, window_height)

        button_width = 300
        button_height = 40

        games_button = main_surface.add_gui_component(window_width/2-button_width/2, window_height/3-button_height/2, button_width, button_height)
        games_button.text = "Games"
        games_button.map_to_button(CROSS_BUTTON, 17)

        settings_button = main_surface.add_gui_component(window_width/2-button_width/2, window_height/2-button_height/2, button_width, button_height)
        settings_button.text = "Settings"
        settings_button.map_to_button(OPTIONS_BUTTON, 33)

        exit_button = main_surface.add_gui_component(window_width/2-button_width/2, window_height-window_height/3-button_height/2, button_width, button_height)
        exit_button.text = "Exit"
        exit_button.map_to_button(CIRCLE_BUTTON, 20)

        self._change_window_surfaces_to_scene_surfaces(window)


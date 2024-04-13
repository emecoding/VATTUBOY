from VATTUBOY.scenes.scene import Scene



class GamesMenu(Scene):
    def __init__(self, gui_manager):
        super().__init__("Games Menu", gui_manager)
        
    def initialize(self, window):
        super().initialize(window)

        window_width = window.get_width()
        window_height = window.get_height()

        main_surface = self.add_surface(0, 0, window_width, window_height)

        self._change_window_surfaces_to_scene_surfaces(window)

        


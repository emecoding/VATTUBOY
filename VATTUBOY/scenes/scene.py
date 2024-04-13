from VATTUBOY.GUI.surface import Surface

class Scene:
    def __init__(self, name, gui_manager):
        self.__name = name
        self.__my_scene_surfaces = []
        self._gui_manager = gui_manager

    def initialize(self, window):
        pass

    def add_surface(self, x, y, width, height):
        surface = Surface(x, y, width, height)
        self.__my_scene_surfaces.append(surface)
        return surface
    
    def get_interactable_gui_components(self):
        interactable_gui_components = []
        for scene_surface in self.__my_scene_surfaces:
            for gui_component in scene_surface.get_gui_components():
                if gui_component.is_interactable:
                    interactable_gui_components.append(gui_component)

        return interactable_gui_components

    def _change_window_surfaces_to_scene_surfaces(self, window):
        window.set_surfaces(self.__my_scene_surfaces)
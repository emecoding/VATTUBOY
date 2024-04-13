from debug import *
from VATTUBOY.GUI.GUIManager import GUIManager
import VATTUBOY.resources.resourceManager
import VATTUBOY.input.inputManager
import VATTUBOY.time.time


class Application:
    def __init__(self, config_parser):
        self.__config_parser = config_parser

        self.__m_GUI_Manager = GUIManager(int(self.__config_parser["WINDOW"]["width"]), int(self.__config_parser["WINDOW"]["height"]), self.__config_parser["WINDOW"]["caption"])

    def initialize(self):
        version = self.__config_parser["APPLICATION"]["version"]
        debug_log(f"starting vattyboy version {version}")

        VATTUBOY.resources.resourceManager.load_resources_on_start(self.__config_parser)

        self.__m_GUI_Manager.change_scene(self.__config_parser["SCENES"]["main_menu"])

    def run(self):
        while not self.__m_GUI_Manager.window.should_close():
            VATTUBOY.input.inputManager.check_if_any_joysticks_are_connected()
            self.__m_GUI_Manager.window.render_window()
            self.__m_GUI_Manager.window.update_window()
            self.__m_GUI_Manager.window.window_input()
            VATTUBOY.input.inputManager.keep_count_of_joysticks()
            self.__m_GUI_Manager.handle_interacting_with_GUI()
            VATTUBOY.time.time.tick_clock()
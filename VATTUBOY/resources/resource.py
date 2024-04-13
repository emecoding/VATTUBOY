import os
from debug import *

class Resource:
    def __init__(self, name):
        self.__name = name

    def get_name(self): return self.__name

    def _check_source(self, file):
        if os.path.exists(file):
            debug_log(f"'{file}' exsists...", is_silent=True)
            return file
        else:
            debug_error(f"invalid file: '{file}'")
            
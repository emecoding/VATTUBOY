import pygame, os
from debug import *

from VATTUBOY.resources.font import Font
from VATTUBOY.resources.spritesheet import SpriteSheet

RESOURCES = []
RESOURCES_CONFIG = None

def get_resource(name):
    global RESOURCES
    for resource in RESOURCES:
        if resource.get_name() == name:
            return resource
        
def add_resource(resource):
    global RESOURCES
    RESOURCES.append(resource)

def load_resources_on_start(config_parser): #VATTUBOY/res will have all the pictures, sounds ect... 
    global add_resource
    global RESOURCES, RESOURCES_CONFIG

    RESOURCES_CONFIG = config_parser["RESOURCES"]

    res_dir = check_source(RESOURCES_CONFIG["res_dir"])

    resources_to_load = os.listdir(res_dir)
    for resource_to_load in resources_to_load:
        file_name, file_type = get_file_name_and_type(resource_to_load)
        
        new_resource = None
        source_file = f"{res_dir}/{resource_to_load}"

        if file_type in RESOURCES_CONFIG["accepted_font_types"]:
            new_resource = Font(file_name, source_file, int(RESOURCES_CONFIG["default_font_size"]))
            
        if file_type in RESOURCES_CONFIG["accepted_sprite_sheet_types"]:
            new_resource = SpriteSheet(file_name, source_file, int(RESOURCES_CONFIG["default_sprite_width"]), int(RESOURCES_CONFIG["default_sprite_height"]))

        if new_resource != None: add_resource(new_resource)
        
    debug_log(f"Loaded {len(RESOURCES)} resource(s) from '{res_dir}'", is_silent=True)

def get_resource(resource_name):
    global RESOURCES
    for resource in RESOURCES:
        if resource.get_name() == resource_name:
            return resource
    
    debug_error(f"no resource called '{resource_name}'", raise_error=True)
    return None


def get_file_name_and_type(file):
    splitted = file.split(".")
    return splitted[0], splitted[-1]

def check_source(file):
    if os.path.exists(file):
        debug_log(f"'{file}' exists...", is_silent=True)
        return file
    else:
        debug_error(f"invalid file: '{file}'")
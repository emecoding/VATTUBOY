import pygame, os
from debug import *

from VATTUBOY.resources.font import Font

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

    res_dir = check_source(config_parser["RESOURCES"]["res_dir"])

    resources_to_load = os.listdir(res_dir)
    for resource_to_load in resources_to_load:
        file_name, file_type = get_file_name_and_type(resource_to_load)
        
        new_resource = None

        if file_type in config_parser["RESOURCES"]["accepted_font_types"]:
            new_resource = Font(file_name, f"{res_dir}/{resource_to_load}", int(config_parser["RESOURCES"]["default_font_size"]))
            

        if new_resource != None: add_resource(new_resource)
        
    debug_log(f"Loaded {len(RESOURCES)} resource(s) from '{res_dir}'", is_silent=True)


def get_file_name_and_type(file):
    splitted = file.split(".")
    return splitted[0], splitted[-1]

def check_source(file):
    if os.path.exists(file):
        debug_log(f"'{file}' exists...", is_silent=True)
        return file
    else:
        debug_error(f"invalid file: '{file}'")
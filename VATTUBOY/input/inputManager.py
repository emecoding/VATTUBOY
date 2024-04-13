import pygame
from debug import *


JOYSTICKS = []

CROSS_BUTTON = 0
CIRCLE_BUTTON = 1
TRIANGLE_BUTTON = 2
SQUARE_BUTTON = 3

L1_BUTTON = 4
R1_BUTTON = 5
L2_BUTTON = 6
R2_BUTTON = 7

SHARE_BUTTON = 8
OPTIONS_BUTTON = 9

L_STICK_BUTTON = 11
R_STICK_BUTTON = 12


def keep_count_of_joysticks():
    global JOYSTICKS
    JOYSTICKS = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

def check_if_any_joysticks_are_connected():
    global JOYSTICKS
    if not atleast_one_joystick_is_connected():
        debug_log("No joysticks are connected...", is_silent=True)
    

def atleast_one_joystick_is_connected():
    global JOYSTICKS
    return True if len(JOYSTICKS) > 0 else False

def get_joystick_button(joystick_index, button):
    global JOYSTICKS
    if len(JOYSTICKS) == 0:
        debug_log("no joysticks found")
    if joystick_index < len(JOYSTICKS):
        return JOYSTICKS[joystick_index].get_button(button)
    
def get_joystick_axis(joystick_index, axis):
    global JOYSTICKS
    if len(JOYSTICKS) == 0:
        debug_log("no joysticks found")
    if joystick_index < len(JOYSTICKS):
        return JOYSTICKS[joystick_index].get_axis(axis)
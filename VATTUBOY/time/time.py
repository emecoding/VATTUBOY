import pygame

FPS = 60

CLOCK = pygame.time.Clock()

def tick_clock():
    global CLOCK, FPS
    CLOCK.tick(FPS)
# -*- coding: utf-8 -*-
"""
Module initializing screen object and screen values.
"""
import pygame
import ctypes
from .path import *

# Change "neuropsydia.screen" to "__main__" When building API documentation. This is to avoid sphinx to run this code, otherwise the documentations fails to be built. "neuropsydia.screen" to make it work.

if __name__ == "neuropsydia.screen":

    yes = ctypes.windll.user32.SetProcessDPIAware()
    resolution = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))


    # Add icon to the window
    pygame.display.set_icon(pygame.image.load(Path.logo() + 'icon.png'))

    # Create screen
    screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

    # Name the screen
    pygame.display.set_caption('Neuropsydia')

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Initialize monitor diagonal size
    monitor_diagonal = 24  # inch

else:
    screen = "Placeholder"
    screen_width, screen_height = 0, 0
    monitor_diagonal = 24
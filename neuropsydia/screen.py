# -*- coding: utf-8 -*-
"""
Module initializing screen object and screen values.
"""
import pygame

screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen_width, screen_height = screen.get_size()

monitor_diagonal = 24  # inch

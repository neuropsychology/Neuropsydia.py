# -*- coding: utf-8 -*-
import pygame

screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen_width, screen_height = screen.get_size()

monitor_diagonal = 24 # inch

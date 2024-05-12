import pygame

# Fullscreen flag
fullscreen_flag = False

# Screen
if fullscreen_flag:
    SCREEN_WIDTH = 2560
    SCREEN_HEIGHT = 1600
    SCALE = SCREEN_HEIGHT / 800
else:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    SCALE = SCREEN_HEIGHT / 800


# Players sprite group
players = pygame.sprite.Group()

# Guns sprite group
guns = pygame.sprite.Group()

# Enemies sprite group
enemies = pygame.sprite.Group()

# Enemies laser guns sprite group
enemies_laser_guns = pygame.sprite.Group()

# Bonuses sprite group
bonuses = pygame.sprite.Group()

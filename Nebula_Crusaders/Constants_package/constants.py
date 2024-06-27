import pygame

# Fullscreen flag
fullscreen_flag = False

# Screen
if fullscreen_flag:
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    SCALE = SCREEN_HEIGHT / 540
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

# Joystick buttons
PS_Cross = 0
PS_Circle = 1
PS_Square = 2
PS_Triangle = 3
PS_Start = 6
PS_L1 = 9
PS_R1 = 10
PS_UP = 11
PS_DOWN = 12
PS_LEFT = 13
PS_RIGHT = 14

# Joystick axes
PS_AXIS_LEFT_X = 0  # Left stick left-right
PS_AXIS_LEFT_Y = 1  # Left stick up-down

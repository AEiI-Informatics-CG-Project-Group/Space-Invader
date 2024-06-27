import pygame
import random
from Constants_package.constants import SCREEN_WIDTH

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet_01 = pygame.image.load('Graphics/planets/Planet1.png').convert_alpha()
        self.planet_02 = pygame.image.load('Graphics/planets/Planet2.png').convert_alpha()
        self.planet_03 = pygame.image.load('Graphics/planets/Planet3.png').convert_alpha()
        self.planet_04 = pygame.image.load('Graphics/planets/Planet4.png').convert_alpha()
        self.planet_05 = pygame.image.load('Graphics/planets/Planet5.png').convert_alpha()
        self.planet_06 = pygame.image.load('Graphics/planets/Planet6.png').convert_alpha()
        self.planet_07 = pygame.image.load('Graphics/planets/Planet7.png').convert_alpha()
        self.planet_08 = pygame.image.load('Graphics/planets/Planet8.png').convert_alpha()
        self.planet_09 = pygame.image.load('Graphics/planets/Planet9.png').convert_alpha()
        self.planet_10 = pygame.image.load('Graphics/planets/Planet10.png').convert_alpha()
        self.planet_11 = pygame.image.load('Graphics/planets/Planet11.png').convert_alpha()
        self.planet_12 = pygame.image.load('Graphics/planets/Planet12.png').convert_alpha()

        self.img_planets = [
            self.planet_01, self.planet_02, self.planet_03, self.planet_04, self.planet_05, self.planet_06,
            self.planet_07, self.planet_08, self.planet_09, self.planet_10, self.planet_11, self.planet_12
        ]
        self.num_planets = len(self.img_planets)
        self.img_index = random.randrange(0, self.num_planets - 1)
        self.image = self.img_planets[self.img_index]
        self.scale_value = random.uniform(0.1, 0.3)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_value),
                                                         int(self.image.get_height() * self.scale_value)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.pos_y = 0 - self.rect.height
        self.vel_x = 0
        self.vel_y = random.uniform(0.1, 1.5)

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

import pygame
import random

from Constants_package.constants import SCALE


# Define the abstract Gun class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__()

        # Stats
        self.damage = 0 * damage_multiplier
        self.fire_rate = 0 * fire_rate_multiplier
        self.bullet_speed = 0 * SCALE
        self.bonus_probability = random.randrange(0, 100)

        # Image data
        self.width = 0 * SCALE
        self.height = 0 * SCALE
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def movement_service(self):
        pass

    def killing_enemy_service(self, enemy):
        pass

    def collision_with_enemy_service(self):
        pass

    def update(self):
        self.movement_service()
        self.collision_with_enemy_service()

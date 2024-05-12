import pygame

from Weapons_package.laser_type_weapon_package.laser_type_weapon import Laser_type_weapon

from Constants_package.constants import SCALE


# Define the Laser_rifle class
class Laser_rifle(Laser_type_weapon):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.1 * damage_multiplier
        self.fire_rate = 60 * fire_rate_multiplier
        self.bullet_speed = 15 * SCALE

        # Image data
        self.width = 8 * SCALE
        self.height = 17 * SCALE
        self.color = '#83EAFF'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/laser_rifle.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.y += -self.bullet_speed
        if self.rect.y < -100:
            self.kill()

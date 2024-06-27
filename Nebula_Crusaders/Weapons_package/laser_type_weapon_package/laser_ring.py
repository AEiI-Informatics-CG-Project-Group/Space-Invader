import pygame

from Weapons_package.laser_type_weapon_package.laser_type_weapon import Laser_type_weapon

from Constants_package.constants import SCALE, fullscreen_flag


# Define the Laser_ring class
class Laser_ring(Laser_type_weapon):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.5 * damage_multiplier
        self.fire_rate = 60 * fire_rate_multiplier
        self.bullet_speed = 10 * SCALE
        self.range_timer_max = 100 * SCALE
        self.range_timer_min = 0

        # Image data
        self.width = 350 * SCALE
        self.height = 350 * SCALE


        # Image
        self.image = pygame.image.load('Graphics/shield.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (700, 680))
        else:
            self.image = pygame.transform.scale(self.image, (350, 340))
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Audio/laser_ring.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.y += -self.bullet_speed
        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100

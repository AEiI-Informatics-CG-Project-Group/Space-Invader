import pygame

from Weapons_package.bullet_type_weapon_package.bullet_type_gun import Bullet_type_weapon

from Constants_package.constants import SCALE, fullscreen_flag


# Define the Rocket_launcher class
class Rocket_launcher(Bullet_type_weapon):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 70 * damage_multiplier
        self.fire_rate = 10000 * fire_rate_multiplier
        self.bullet_speed = 10 * SCALE

        # Image data


        # Image
        self.image = pygame.image.load('Graphics/rocket.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (40, 70))
        else:
            self.image = pygame.transform.scale(self.image, (20, 35))
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Audio/rocket_launcher.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

import pygame
import random


from Bonuses_package.bonus import Bonus

from Constants_package.constants import players, SCALE, fullscreen_flag


# Define the Stats_bonus class
class Stats_bonus(Bonus):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.speed = 2 * SCALE
        self.score_bonus = 50

        # Image data

        # Image
        self.image_damage_up = pygame.image.load('Graphics/damage_bonus.png').convert_alpha()
        self.image_fire_rate_up = pygame.image.load('Graphics/fire_rate_bonus.png').convert_alpha()
        self.image_speed_up = pygame.image.load('Graphics/speed_bonus.png').convert_alpha()
        if fullscreen_flag:
            self.image_damage_up = pygame.transform.scale(self.image, (62, 60))
            self.image_fire_rate_up = pygame.transform.scale(self.image, (62, 60))
            self.image_speed_up = pygame.transform.scale(self.image, (62, 60))
        else:
            self.image_damage_up = pygame.transform.scale(self.image, (31, 30))
            self.image_fire_rate_up = pygame.transform.scale(self.image, (31, 30))
            self.image_speed_up = pygame.transform.scale(self.image, (31, 30))
        self.rect = self.image.get_rect()

        # Set bonus
        self.bonus_type = random.randint(1, 3)
        if self.bonus_type == 1:
            self.image_damage_up = pygame.image.load('Graphics/damage_bonus.png').convert_alpha()
        if self.bonus_type == 2:
            self.image_fire_rate_up = pygame.image.load('Graphics/fire_rate_bonus.png').convert_alpha()
        if self.bonus_type == 3:
            self.image_speed_up = pygame.image.load('Graphics/speed_bonus.png').convert_alpha()

        # Position
        self.rect.center = center

    def collision_with_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                if self.bonus_type == 1:
                    if player.gun_damage_multiplier <= 20:
                        player.gun_damage_multiplier += 0.5
                    elif player.gun_fire_rate_multiplier >= 0.1:
                        player.gun_fire_rate_multiplier += -0.05
                    elif player.speed <= 25 * SCALE:
                        player.speed += 1 * SCALE
                    else:
                        player.score += self.score_bonus*2
                if self.bonus_type == 2:
                    if player.gun_fire_rate_multiplier >= 0.1:
                        player.gun_fire_rate_multiplier += -0.05
                    elif player.gun_damage_multiplier <= 20:
                        player.gun_damage_multiplier += 0.5
                    elif player.speed <= 25 * SCALE:
                        player.speed += 1 * SCALE
                    else:
                        player.score += self.score_bonus*2
                if self.bonus_type == 3:
                    if player.speed <= 25 * SCALE:
                        player.speed += 1 * SCALE
                    elif player.gun_damage_multiplier <= 20:
                        player.gun_damage_multiplier += 0.5
                    elif player.gun_fire_rate_multiplier >= 0.1:
                        player.gun_fire_rate_multiplier += -0.05
                    else:
                        player.score += self.score_bonus*2
                self.kill()
                player.score += self.score_bonus
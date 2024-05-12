import pygame
import random


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_gun_package.enemy_gun import Enemy_gun

from Constants_package.constants import players, enemies_laser_guns, SCREEN_WIDTH, SCALE


# Define the Star_lord class
class Star_lord(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 120
        self.speed_x = 3 * SCALE
        self.speed_y = 5 * SCALE
        self.acceleration = 1
        self.damage = 1

        # Timer
        self.star_lord_timer = 0

        # Image data
        self.width = 120 * SCALE
        self.height = 50 * SCALE
        self.color = '#2EA33B'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(100 * SCALE, SCREEN_WIDTH - 100 * SCALE)
        self.rect.y = 100 * SCALE

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/star_lord.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.x += self.speed_x * self.acceleration
        self.rect.y += self.speed_y
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.bottom >= 300 * SCALE:
            self.speed_y = self.speed_y * -1

        if self.rect.top <= 0:
            self.speed_y = self.speed_y * -1

        if self.rect.centery <= 150:
            self.acceleration = 5
        else:
            self.acceleration = 1

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        if self.star_lord_timer <= 0:
            enemy_laser_gun = Enemy_gun(self.rect.center, 1.5, 2500, 10, 40, 65, "#FE1E1E")
            enemies_laser_guns.add(enemy_laser_gun)
            self.star_lord_timer = enemy_laser_gun.fire_rate
        self.star_lord_timer += -100

    def hp_service(self):
        if self.hp <= 60:
            self.image.fill('#A3702E')
        if self.hp <= 30:
            self.image.fill('#A3402E')

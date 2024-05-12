import pygame
import random


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_gun_package.galactic_devourer_laser_ring import Galactic_devourer_laser_ring

from Constants_package.constants import players, enemies_laser_guns, SCREEN_WIDTH, SCREEN_HEIGHT, SCALE


# Define the Galactic_devourer class
class Galactic_devourer(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.damage = 1
        self.hp = 800
        self.acceleration = 1

        self.one_neg = [-1, 1]
        self.random_direction = random.choice(self.one_neg)

        self.speed_x = random.randrange(2, 3) * self.random_direction * SCALE
        self.speed_y = random.randrange(2, 3) * self.random_direction * SCALE

        # Timer
        self.galactic_devourer_timer = 0
        self.galactic_devourer_overheating_timer = 20001
        self.galactic_devourer_overheating_timer_max = 20000
        self.galactic_devourer_overheating_timer_2 = 20000
        self.overheating_passed = True

        # Image data
        self.width = 100 * SCALE
        self.height = 100 * SCALE
        self.color = '#EE2659'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(200 * SCALE, SCREEN_WIDTH - 200 * SCALE)
        self.rect.y = 200 * SCALE

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/galactic_devourer.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.x += self.speed_x * 2 * self.acceleration
        self.rect.y += self.speed_y * self.acceleration
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed_x *= -1
        if self.rect.bottom >= SCREEN_HEIGHT or self.rect.top <= 0:
            self.speed_y *= -1

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        if self.galactic_devourer_overheating_timer <= self.galactic_devourer_overheating_timer_max:

            if self.galactic_devourer_timer <= 0:
                galactic_devourer_laser_ring = Galactic_devourer_laser_ring(self.rect.center, 1, 200, 15, 250, 250,
                                                                            "#FF05D5")
                enemies_laser_guns.add(galactic_devourer_laser_ring)
                self.galactic_devourer_timer = galactic_devourer_laser_ring.fire_rate
                self.acceleration = 6

            self.galactic_devourer_timer += -100
            self.galactic_devourer_overheating_timer += 100
            self.galactic_devourer_overheating_timer_2 = 0

        else:
            self.acceleration = 1
            if self.galactic_devourer_overheating_timer_2 >= self.galactic_devourer_overheating_timer_max * 2:
                self.galactic_devourer_overheating_timer = 0

            self.galactic_devourer_overheating_timer_2 += 100

    def hp_service(self):
        if self.hp <= 400:
            self.image.fill('#A3702E')
        if self.hp <= 200:
            self.image.fill('#A3402E')

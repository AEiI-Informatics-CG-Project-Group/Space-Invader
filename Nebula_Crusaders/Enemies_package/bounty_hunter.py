import pygame
import math


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_gun_package.enemy_gun import Enemy_gun

from Constants_package.constants import players, enemies_laser_guns, SCREEN_WIDTH, SCREEN_HEIGHT, SCALE, fullscreen_flag


# Define the Bounty_hunter class
class Bounty_hunter(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 240
        self.speed_x = 300 * SCALE
        self.speed_y = 3 * SCALE
        self.damage = 1
        self.radius = 100 * SCALE
        self.angle = 0

        # Flags
        self.jumped_right = False
        self.jumped_left = False

        # Timer
        self.bounty_hunter_timer = 0
        self.bounty_hunter_overheating_timer = 0
        self.bounty_hunter_overheating_timer_max = 20000
        self.bounty_hunter_overheating_timer_2 = 0
        self.overheating_passed = True

        # Image
        self.image = pygame.image.load('Graphics/bounty_hunter.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (163, 140))
        else:
            self.image = pygame.transform.scale(self.image, (126, 108))
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (SCREEN_WIDTH / 2 - self.radius / 2, SCREEN_HEIGHT / 10)

        # Audio
        self.audio = pygame.mixer.Sound("Audio/bounty_hunter.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):

        self.angle += 0.1
        if self.hp >= 160:
            self.rect.x = SCREEN_WIDTH / 2 - self.radius + self.radius * math.cos(self.angle)
            self.rect.y = SCREEN_HEIGHT / 7 + self.radius * math.sin(self.angle)

        if 160 > self.hp >= 80:
            self.rect.x = SCREEN_WIDTH / 4 + self.radius * math.cos(self.angle)
            self.rect.y = SCREEN_HEIGHT / 7 + self.radius * math.sin(self.angle)

        if self.hp < 80:
            self.rect.x = SCREEN_WIDTH * 3 / 4 + self.radius * math.cos(self.angle)
            self.rect.y = SCREEN_HEIGHT / 7 + self.radius * math.sin(self.angle)

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        if self.bounty_hunter_overheating_timer <= self.bounty_hunter_overheating_timer_max:

            if self.bounty_hunter_timer <= 0:
                enemy_laser_gun = Enemy_gun(self.rect.center, 1, 1250, 15, 40, 55, 'Graphics/laserGreen.png')
                enemies_laser_guns.add(enemy_laser_gun)
                self.bounty_hunter_timer = enemy_laser_gun.fire_rate

            self.bounty_hunter_timer += -100
            self.bounty_hunter_overheating_timer += 100
            self.bounty_hunter_overheating_timer_2 = 0

        else:

            if self.bounty_hunter_overheating_timer_2 >= self.bounty_hunter_overheating_timer_max:
                self.bounty_hunter_overheating_timer = 0

            self.bounty_hunter_overheating_timer_2 += 100


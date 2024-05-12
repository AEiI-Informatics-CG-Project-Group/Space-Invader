import pygame
import threading


from Weapons_package.bullet_type_weapon_package.minigun import Minigun
from Weapons_package.laser_type_weapon_package.laser_rifle import Laser_rifle
from Weapons_package.bullet_type_weapon_package.rocket_launcher import Rocket_launcher
from Weapons_package.laser_type_weapon_package.laser_ring import Laser_ring
from Weapons_package.bullet_type_weapon_package.sniper_rifle import Sniper_rifle
from Weapons_package.laser_type_weapon_package.laser_thrower import Laser_thrower

from Constants_package.constants import guns, SCALE, SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen_flag


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.gun_damage_multiplier = 1
        self.gun_fire_rate_multiplier = 1
        self.speed = 10 * SCALE
        self.hp = 3

        # Info
        self.score = 0

        # Equipment
        self.gun_list = ["Minigun", "Laser Rifle", "Rocket Launcher", "Laser Ring", "Sniper Rifle", "Laser Thrower"]
        self.gun_index = 0
        self.using_gun_type = self.gun_list[self.gun_index]

        # Obtained guns
        self.minigun = True
        self.laser_rifle = False
        self.rocket_launcher = False
        self.laser_ring = False
        self.sniper_rifle = False
        self.laser_thrower = False

        # Timer
        self.player_timer = 0

        # Image
        self.image = pygame.image.load('Additional_resources/Graphics/player.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (200, 200))
        else:
            self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - SCREEN_HEIGHT / 10)

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/player.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

        # Threads
        self.movement_thread = threading.Thread(target=self.movement_service)
        self.shooting_thread = threading.Thread(target=self.shooting_service)
        self.switching_gun_thread = threading.Thread(target=self.gun_switching_service)
        self.update_thread = threading.Thread(target=self.update)

        self.movement_thread.start()
        self.shooting_thread.start()
        self.switching_gun_thread.start()
        self.update_thread.start()

        # Mutex
        self.player_shooting_mutex = threading.Lock()

    def movement_service(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.right <= 0:
                self.rect.left = SCREEN_WIDTH
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.left >= SCREEN_WIDTH:
                self.rect.right = 0
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    def shooting_service(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.using_gun_type == 'Minigun' and self.player_timer <= 0:
            minigun = Minigun(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(minigun)
            self.player_shooting_mutex.release()
            self.player_timer = minigun.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser Rifle' and self.player_timer <= 0:
            laser_rifle = Laser_rifle(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(laser_rifle)
            self.player_shooting_mutex.release()
            self.player_timer = laser_rifle.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Rocket Launcher' and self.player_timer <= 0:
            rocket_launcher = Rocket_launcher(self.rect.center, self.gun_damage_multiplier,
                                              self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(rocket_launcher)
            self.player_shooting_mutex.release()
            self.player_timer = rocket_launcher.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser Ring' and self.player_timer <= 0:
            laser_ring = Laser_ring(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(laser_ring)
            self.player_shooting_mutex.release()
            self.player_timer = laser_ring.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Sniper Rifle' and self.player_timer <= 0:
            sniper_rifle = Sniper_rifle(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(sniper_rifle)
            self.player_shooting_mutex.release()
            self.player_timer = sniper_rifle.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser Thrower' and self.player_timer <= 0:
            laser_thrower = Laser_thrower(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            self.player_shooting_mutex.acquire()
            guns.add(laser_thrower)
            self.player_shooting_mutex.release()
            self.player_timer = laser_thrower.fire_rate

        self.player_timer += -100

    def gun_switching_service(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and self.minigun:
            self.using_gun_type = self.gun_list[0]

        if keys[pygame.K_2] and self.laser_rifle:
            self.using_gun_type = self.gun_list[1]

        if keys[pygame.K_3] and self.rocket_launcher:
            self.using_gun_type = self.gun_list[2]

        if keys[pygame.K_4] and self.laser_ring:
            self.using_gun_type = self.gun_list[3]

        if keys[pygame.K_5] and self.sniper_rifle:
            self.using_gun_type = self.gun_list[4]

        if keys[pygame.K_6] and self.laser_thrower:
            self.using_gun_type = self.gun_list[5]

    def update(self):
        self.movement_service()
        self.shooting_service()
        self.gun_switching_service()

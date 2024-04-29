import pygame
import threading

from Constants_package.constants import SCALE, SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen_flag


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.speed = 10 * SCALE
        self.hp = 3

        # Info
        self.score = 0

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
        self.update_thread = threading.Thread(target=self.update)

        self.movement_thread.start()
        self.update_thread.start()

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

    def update(self):
        self.movement_service()

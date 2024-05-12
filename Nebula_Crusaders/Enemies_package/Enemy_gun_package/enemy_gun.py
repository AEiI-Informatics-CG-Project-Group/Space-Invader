import pygame


from Constants_package.constants import players, enemies_laser_guns, SCREEN_HEIGHT, SCALE


class Enemy_gun(pygame.sprite.Sprite):
    def __init__(self, center, damage, fire_rate, bullet_speed, width, height, color):
        super().__init__()

        # Stats
        self.damage = damage
        self.fire_rate = fire_rate
        self.bullet_speed = bullet_speed * SCALE

        # Image data
        self.width = width * SCALE
        self.height = height * SCALE
        self.color = color

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/enemy_laser_gun.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.y += self.bullet_speed

        if self.rect.y > SCREEN_HEIGHT + 100:
            self.kill()

    def collision_and_killing_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                pygame.sprite.spritecollide(player, enemies_laser_guns, True)
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def update(self):
        self.movement_service()
        self.collision_and_killing_player_service()

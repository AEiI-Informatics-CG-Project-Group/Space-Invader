import pygame


from Enemies_package.Enemy_gun_package.enemy_gun import Enemy_gun
from Constants_package.constants import players, SCALE


class Galactic_devourer_laser_ring(Enemy_gun):
    def __init__(self, center, damage, fire_rate, bullet_speed, width, height, color):
        super().__init__(center, damage, fire_rate, bullet_speed, width, height, color)

        self.range_timer_max = 150 * SCALE
        self.range_timer_min = 0

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/devourer_gun.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.y += -self.bullet_speed

        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100

    def collision_and_killing_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

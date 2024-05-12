import pygame


from Bonuses_package.bonus import Bonus

from Constants_package.constants import players, SCALE


# Define the Gun_bonus class
class Gun_bonus(Bonus):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.speed = 2 * SCALE
        self.score_bonus = 150

        # Image data
        self.color = '#5100FF'
        self.height = 45 * SCALE
        self.width = 65 * SCALE

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def collision_with_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                if player.sniper_rifle:
                    player.laser_thrower = True

                if player.laser_ring:
                    player.sniper_rifle = True

                if player.rocket_launcher:
                    player.laser_ring = True

                if player.laser_rifle:
                    player.rocket_launcher = True

                if player.minigun:
                    player.laser_rifle = True

                if player.minigun and player.laser_rifle and player.rocket_launcher and player.laser_ring and player.sniper_rifle and player.laser_thrower:
                    player.score += self.score_bonus*2

                self.kill()
                player.score += self.score_bonus

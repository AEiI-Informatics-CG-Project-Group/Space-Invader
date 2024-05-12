import pygame


from Bonuses_package.bonus import Bonus

from Constants_package.constants import players, SCALE


# Define the Hp_Bonus class
class Hp_bonus(Bonus):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.speed = 2 * SCALE
        self.score_bonus = 50

        # Image data
        self.color = '#FA4CDA'
        self.height = 45 * SCALE
        self.width = 45 * SCALE

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
                if player.hp >= 10:
                    pass
                else:
                    if player.hp + 1 >= 10:
                        player.hp = 10
                    else:
                        player.hp += 1
                self.kill()
                player.score += self.score_bonus

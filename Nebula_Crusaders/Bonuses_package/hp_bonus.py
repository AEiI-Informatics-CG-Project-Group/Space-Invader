import pygame


from Bonuses_package.bonus import Bonus

from Constants_package.constants import players, SCALE, fullscreen_flag


# Define the Hp_Bonus class
class Hp_bonus(Bonus):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.speed = 2 * SCALE
        self.score_bonus = 50

        # Image data

        # Image
        self.image = pygame.image.load('Graphics/hp_bonus.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (60, 80))
        else:
            self.image = pygame.transform.scale(self.image, (30, 40))
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def collision_with_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                if player.hp >= 100:
                    pass
                else:
                    if player.hp + 1 >= 100:
                        player.hp = 100
                    else:
                        player.hp += 1
                self.kill()
                player.score += self.score_bonus